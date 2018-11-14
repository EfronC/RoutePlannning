from collections import OrderedDict
from threading import Lock
from flask import Blueprint, Flask, jsonify, render_template, request, session
from flask_socketio import emit, SocketIO
from json import load
from os.path import abspath, dirname, join, pardir
from sqlalchemy import exc as sql_exception
from werkzeug.utils import secure_filename
from xlrd import open_workbook
import sys

sys.dont_write_bytecode = True
path_app = dirname(abspath(__file__))
path_parent = abspath(join(path_app, pardir))
if path_app not in sys.path:
    sys.path.append(path_app)

from algorithms.pytsp import pyTSP
from database import db, create_database
from models import City

from test import get_routes, get_destinies

bp = Blueprint('tsp_app', __name__)


def allowed_file(name, allowed_extensions):
    allowed_syntax = '.' in name
    allowed_extension = name.rsplit('.', 1)[1].lower() in allowed_extensions
    return allowed_syntax and allowed_extension


@bp.route('/', methods=['GET', 'POST'])
def index():
    if 'file' in request.files:
        filename = request.files['file'].filename
        if allowed_file(filename, {'xls', 'xlsx'}):
            filename = secure_filename(filename)
            filepath = join(path_app, 'data', filename)
            request.files['file'].save(filepath)
            sheet = open_workbook(filepath).sheet_by_index(0)
            properties = sheet.row_values(0)
            db.session.query(City).delete()
            for row_index in range(1, sheet.nrows):
                city_dict = dict(zip(properties, sheet.row_values(row_index)))
                city = City(**city_dict)
                db.session.add(city)
            db.session.commit()
            tsp.update_data()
    session['best'] = float('inf')
    session['crossover'], session['mutation'] = 'OC', 'Swap'
    view = request.form['view'] if 'view' in request.form else '2D'
    cities = {
        city.id: OrderedDict([
            (property, getattr(city, property))
            for property in City.properties
        ])
        for city in City.query.all()
    }
    return render_template(
        'index.html',
        view=view,
        cities=cities,
        async_mode=socketio.async_mode
    )

@bp.route('/test', methods=['GET', 'POST'])
def test():
    session['best'] = float('inf')
    return jsonify(get_routes())

@bp.route('/destinies', methods=['GET'])
def destinies():
    session['best'] = float('inf')
    return jsonify(get_destinies())

@bp.route('/<algorithm>', methods=['POST'])
def algorithm(algorithm):
    session['best'] = float('inf')
    return jsonify(*getattr(tsp, algorithm)())


def configure_database(app):
    create_database()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()
    db.init_app(app)


def configure_socket(app):
    async_mode = None
    socketio = SocketIO(app, async_mode=async_mode)
    thread_lock = Lock()
    return socketio


def import_cities():
    with open(join(path_parent, 'data', 'test.json')) as data:
        for city_dict in load(data):
            if int(city_dict['population']) < 900000:
                continue
            city = City(**city_dict)
            db.session.add(city)
        try:
            db.session.commit()
        except sql_exception.IntegrityError:
            db.session.rollback()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'key'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(bp)
    configure_database(app)
    socketio = configure_socket(app)
    import_cities()
    tsp = pyTSP()
    return app, socketio, tsp


app, socketio, tsp = create_app()


@socketio.on('genetic_algorithm')
def genetic_algorithm(data):
    if 'generation' not in session:
        session['generation'] = []
    session['generation'], best, length = tsp.cycle(session['generation'], **data)
    if length < session['best']:
        session['best'] = length
        emit('draw', ([best], [length]))


if __name__ == '__main__':
    socketio.run(app)
