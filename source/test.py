from algorithms.LPRoutes import LPRoutes
from algorithms.opt_heuristic import LocalOptmizationHeuristics
from operator import itemgetter
import distances
import pprint
import geopy.distance

"""
defaultdict(<class 'dict'>, {1: {1: 0.0, 2: 7.1775194075460815, 3: 9.949631307115963, 4: 2.1475062822990223, 5: 7.4632435274471485}, 2: {1: 7.1775194075460815, 2: 0.0, 3: 9.337091839921769, 4: 7.129246305727056, 5: 2.965271023017161}, 3: {1: 9.949631307115963, 2: 9.337091839921769, 3: 0.0, 4: 7.912992117217642, 5: 6.4513541157706}, 4: {1: 2.1475062822990223, 2: 7.129246305727056, 3: 7.912992117217642, 4: 0.0, 5: 6.540207083450436}, 5: {1: 7.4632435274471485, 2: 2.965271023017161, 3: 6.4513541157706, 4: 6.540207083450436, 5: 0.0}})
5
[1, 2, 3, 4, 5]
{1: (20.9216725, -89.6658166), 2: (20.9858935, -89.6727756), 3: (20.9692005, -89.5846395), 4: (20.9268914, -89.6459093), 5: (20.9856876, -89.6442146)}


[   
	{   'destinos': {   0: {   'coordenadas': (21.0366944, -89.6276604),
                               'id': 0,
                               'index': 0,
                               'moda': 3},
                        1: {   'coordenadas': (21.0710793, -89.6562318),
                               'id': 1,
                               'index': 1,
                               'moda': 3},
                        2: {   'coordenadas': (21.0710793, -89.6562318),
                               'id': 2,
                               'index': 2,
                               'moda': 2},
                        3: {   'coordenadas': (21.0343356, -89.6257259),
                               'id': 3,
                               'index': 3,
                               'moda': 1},
                        4: {   'coordenadas': (21.0204019, -89.5986979),
                               'id': 4,
                               'index': 4,
                               'moda': 1}},
        'routes': [   {   'iter': 2,
                          'route': {   'dest': {   0: {   'coordenadas': (   21.0366944,
                                                                             -89.6276604),
                                                          'id': 0,
                                                          'index': 0,
                                                          'moda': 3},
                                                   4: {   'coordenadas': (   21.0204019,
                                                                             -89.5986979),
                                                          'id': 4,
                                                          'index': 4,
                                                          'moda': 1}},
                                       'peso': 69.95108522590621,
                                       'ruta': [   {   'assigned': True,
                                                       'coordenadas': (   21.0030254,
                                                                          -89.7179189),
                                                       'destino': 0,
                                                       'destiny': 10.096344803523522,
                                                       'distance': 13.121257046958108,
                                                       'turno': 1},
                                                   {   'assigned': True,
                                                       'coordenadas': (   21.0355766,
                                                                          -89.6382226),
                                                       'destino': 0,
                                                       'destiny': 1.1048450612820635,
                                                       'distance': 19.927676450814452,
                                                       'turno': 1},
                                                   {   'assigned': True,
                                                       'coordenadas': (   20.9516388,
                                                                          -89.6218666),
                                                       'destino': 0,
                                                       'destiny': 9.436344932857217,
                                                       'distance': 14.874034872579328,
                                                       'turno': 1},
                                                   {   'assigned': True,
                                                       'coordenadas': (   20.928956,
                                                                          -89.6172707),
                                                       'destino': 4,
                                                       'destiny': 10.307152142736033,
                                                       'distance': 14.312719372254529,
                                                       'turno': 1}]},
                          'taxista': 0},
                      {   'iter': 2,
                          'route': {   'dest': {   1: {   'coordenadas': (   21.0710793,
                                                                             -89.6562318),
                                                          'id': 1,
                                                          'index': 1,
                                                          'moda': 3}},
                                       'peso': 4.1467248888896275,
                                       'ruta': [   {   'assigned': True,
                                                       'coordenadas': (   21.081147,
                                                                          -89.6627502),
                                                       'destino': 1,
                                                       'destiny': 1.3043546398972927,
                                                       'distance': 23.15142793692559,
                                                       'turno': 1},
                                                   {   'assigned': True,
                                                       'coordenadas': (   21.0731314,
                                                                          -89.6587167),
                                                       'destino': 1,
                                                       'destiny': 0.3439556027356481,
                                                       'distance': 22.502986191115095,
                                                       'turno': 1},
                                                   {   'assigned': True,
                                                       'coordenadas': (   21.075004,
                                                                          -89.6631023),
                                                       'destino': 1,
                                                       'destiny': 0.8358162176556612,
                                                       'distance': 22.5099858533844,
                                                       'turno': 1}]},
                          'taxista': 1}]},
    {   'destinos': {   0: {   'coordenadas': (21.0366944, -89.6276604),
                               'id': 0,
                               'index': 0,
                               'moda': 3},
                        1: {   'coordenadas': (21.0710793, -89.6562318),
                               'id': 1,
                               'index': 1,
                               'moda': 3},
                        2: {   'coordenadas': (21.0710793, -89.6562318),
                               'id': 2,
                               'index': 2,
                               'moda': 2},
                        3: {   'coordenadas': (21.0343356, -89.6257259),
                               'id': 3,
                               'index': 3,
                               'moda': 1},
                        4: {   'coordenadas': (21.0204019, -89.5986979),
                               'id': 4,
                               'index': 4,
                               'moda': 1}},
        'routes': [   {   'iter': 3,
                          'route': {   'dest': {   2: {   'coordenadas': (   21.0710793,
                                                                             -89.6562318),
                                                          'id': 2,
                                                          'index': 2,
                                                          'moda': 2},
                                                   3: {   'coordenadas': (   21.0343356,
                                                                             -89.6257259),
                                                          'id': 3,
                                                          'index': 3,
                                                          'moda': 1}},
                                       'peso': 84.67326068756039,
                                       'ruta': [   {   'assigned': True,
                                                       'coordenadas': (   20.912927,
                                                                          -89.6019652),
                                                       'destino': 2,
                                                       'destiny': 18.39678642002499,
                                                       'distance': 15.415321489274449,
                                                       'turno': 1},
                                                   {   'assigned': True,
                                                       'coordenadas': (   21.067476,
                                                                          -89.6553769),
                                                       'destino': 2,
                                                       'destiny': 0.40872258385456794,
                                                       'distance': 22.08259196626246,
                                                       'turno': 1},
                                                   {   'assigned': True,
                                                       'coordenadas': (   21.031682,
                                                                          -89.6484788),
                                                       'destino': 3,
                                                       'destiny': 2.3832860786123766,
                                                       'distance': 18.974837977489802,
                                                       'turno': 1},
                                                   {   'assigned': True,
                                                       'coordenadas': (   20.998073,
                                                                          -89.6049088),
                                                       'destino': 3,
                                                       'destiny': 4.561012318392457,
                                                       'distance': 19.22231564443606,
                                                       'turno': 1}]},
                          'taxista': 0},
                      {   'iter': 3,
                          'route': {   'dest': {   3: {   'coordenadas': (   21.0343356,
                                                                             -89.6257259),
                                                          'id': 3,
                                                          'index': 3,
                                                          'moda': 1},
                                                   4: {   'coordenadas': (   21.0204019,
                                                                             -89.5986979),
                                                          'id': 4,
                                                          'index': 4,
                                                          'moda': 1}},
                                       'peso': 18.754588678045014,
                                       'ruta': [   {   'assigned': True,
                                                       'coordenadas': (   21.0347108,
                                                                          -89.6255674),
                                                       'destino': 3,
                                                       'destiny': 0.04468907803902329,
                                                       'distance': 20.632287679370943,
                                                       'turno': 1},
                                                   {   'assigned': True,
                                                       'coordenadas': (   20.988045,
                                                                          -89.5698762),
                                                       'destino': 4,
                                                       'destiny': 4.670455977381283,
                                                       'distance': 21.567956590838076,
                                                       'turno': 1}]},
                          'taxista': 1}]},
    {   'destinos': {   0: {   'coordenadas': (21.0366944, -89.6276604),
                               'id': 0,
                               'index': 0,
                               'moda': 3},
                        1: {   'coordenadas': (21.0710793, -89.6562318),
                               'id': 1,
                               'index': 1,
                               'moda': 3},
                        2: {   'coordenadas': (21.0710793, -89.6562318),
                               'id': 2,
                               'index': 2,
                               'moda': 2},
                        3: {   'coordenadas': (21.0343356, -89.6257259),
                               'id': 3,
                               'index': 3,
                               'moda': 1},
                        4: {   'coordenadas': (21.0204019, -89.5986979),
                               'id': 4,
                               'index': 4,
                               'moda': 1}},
        'routes': [   {   'iter': 4,
                          'route': {   'dest': {   4: {   'coordenadas': (   21.0204019,
                                                                             -89.5986979),
                                                          'id': 4,
                                                          'index': 4,
                                                          'moda': 1}},
                                       'peso': 5.005157733169497,
                                       'ruta': [   {   'assigned': True,
                                                       'coordenadas': (   20.977,
                                                                          -89.5852312),
                                                       'destino': 4,
                                                       'destiny': 5.005157733169497,
                                                       'distance': 19.57119464549679,
                                                       'turno': 1}]},
                          'taxista': 0}]}
]

"""
def removeLongest(arr):
	longest = 0
	longer = 0
	toDel = 0
	for i in range(0,len(arr)-1):
		longer = abs(arr)

def check_available(destinos):
	pass

def generate_moda(destinos, rutas):
	dest = dict()
	for i in rutas:
		if i["destino"] not in dest.keys():
			dest[i["destino"]] = dict()
			dest[i["destino"]]["moda"] = 1
			dest[i["destino"]]["coordenadas"] = destinos[i["destino"]]["coordenadas"]
		else:
			dest[i["destino"]]["moda"] += 1
	return dest

def get_index_coordenada(tovisit, coordenada):
	for i in tovisit:
		if i["coordenadas"] == coordenada:
			return tovisit.index(i)

def get_routes():
	pp = pprint.PrettyPrinter(indent=4)
	rutas = distances.get_routes()
	routes = list()
	steps = list()
	tovisit = list()
	res = list()
	print("///////////////////////////////////////////////////////")
	pp.pprint(rutas)
	print("///////////////////////////////////////////////////////")
	for iteracion in rutas:
		for i in iteracion["routes"]:
			goal = generate_moda(iteracion["destinos"], i["route"]["ruta"])
			for j in i["route"]["ruta"]:
				j["assigned"] = False
				tovisit.append(j)
			first = tovisit[0]
			goal.get(first["destino"])["moda"] -= 1
			print("Anado el primero: " + str(first["coordenadas"]))
			steps.append(first["coordenadas"])
			ind = get_index_coordenada(tovisit, tovisit[0]["coordenadas"])
			if goal.get(tovisit[ind]["destino"])["moda"] == 0 or len(tovisit) == 0:
				print("Ya es cero: " + str(goal.get(tovisit[ind]["destino"])["coordenadas"]))
				steps.append(goal.get(tovisit[ind]["destino"])["coordenadas"])
			del tovisit[0]
			if len(tovisit) == 0:
				pass
			else:
				while len(tovisit) > 0:
					print("Nueva busqueda")
					intermediate = list()
					start = steps[len(steps)-1]
					for h in tovisit:
						inter = dict()
						inter["distancia"] = geopy.distance.distance(start, h["coordenadas"]).km
						inter["coordenada"] = h["coordenadas"]
						intermediate.append(inter)
					points = sorted(intermediate, key=itemgetter('distancia'), reverse=False)
					ind = get_index_coordenada(tovisit, points[0]["coordenada"])
					goal.get(tovisit[ind]["destino"])["moda"] -= 1
					print("Anado otro paso: " + str(tovisit[ind]["coordenadas"]))
					steps.append(tovisit[ind]["coordenadas"])
					if goal.get(tovisit[ind]["destino"])["moda"] == 0:
						print("Ya es cero: " + str(goal.get(tovisit[ind]["destino"])["coordenadas"]))
						steps.append(goal.get(tovisit[ind]["destino"])["coordenadas"])
					del tovisit[ind]
			print("-----------------------------------------------------------------------------------")
			routes.append(steps)
			tovisit = []
			steps = []
	for ruta in routes:
		res.append(tuple(ruta))
	print("******************************************************")
	pp.pprint(res)
	print("******************************************************")
	#Alter
	# routes = list()
	# steps = []
	# tovisit = list()
	# for iteracion in rutas:
	# 	destinos = iteracion["destinos"]
	# 	for i in iteracion["routes"]:
	# 		posibles = []
	# 		route = []
	# 		coords = {}
	# 		for j in i["route"]["ruta"]:
	# 			route.append(i["route"]["ruta"].index(j) + 1)
	# 			coords[i["route"]["ruta"].index(j) + 1] = j["coordenadas"]
	# 			if not j["destino"] in posibles:
	# 				posibles.append(j["destino"])
	# 		#route.append(len(route) + 1)
	# 		#coords[len(route)] = destinos.get(posibles[0])["coordenadas"]
	# 		destinies = {c: destinos.get(c)["coordenadas"] for c in posibles}
	# 		algo = LocalOptmizationHeuristics({"coords":coords, "route":route, "destinies":destinies})
	# 		steps.append(algo.pairwise_exchange())
	# pp.pprint(steps)
	return res

"""
[   
	(   
		[   
			[   
				(21.0030254, -89.7179189),
                (21.0355766, -89.6382226),
                (20.9516388, -89.6218666),
                (20.928956, -89.6172707),
                (21.0030254, -89.7179189)
            ]
        ],
        [34.38898170429924],
        {
        	0: (21.0366944, -89.6276604), 
        	4: (21.0204019, -89.5986979)
        }
    ),
    (   
    	[   
    		[   
    			(21.075004, -89.6631023),
                (21.0731314, -89.6587167),
                (21.081147, -89.6627502),
                (21.075004, -89.6631023)
            ]
        ],
        [2.1691204650256313],
        {
        	1: (21.0710793, -89.6562318)
        }
    ),
    (   
    	[   
    		[   
    			(21.067476, -89.6553769),
                (20.998073, -89.6049088),
                (20.912927, -89.6019652),
                (21.031682, -89.6484788),
                (21.067476, -89.6553769)
            ]
        ],
        [36.90403319384603],
        {
        	2: (21.0710793, -89.6562318), 
        	3: (21.0343356, -89.6257259)
        }
    ),
    (   
    	[   
    		[   
    			(21.0347108, -89.6255674),
                (20.988045, -89.5698762),
                (21.0347108, -89.6255674)
            ]
        ],
        [15.536242977084056],
        {
        	3: (21.0343356, -89.6257259), 
        	4: (21.0204019, -89.5986979)
        }
    ),
    (   
    	[
    		[
    			(20.977, -89.5852312), (20.977, -89.5852312)
    		]
    	],
        [0.0],
        {
        	4: (21.0204019, -89.5986979)
        }
    )
]
"""

def get_destinies():
	destinos = distances.get_destinies()
	return destinos