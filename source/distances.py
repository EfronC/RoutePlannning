import geopy.distance
from operator import itemgetter
import pprint
import itertools

def build_dict(seq, key):
    return dict((d[key], dict(d, index=index)) for (index, d) in enumerate(seq))

def eq(a, b):
	if a == b:
		return True
	else:
		return False

def check_available(lst):
	for i in lst:
		if not i["assigned"]:
			return True
	return False

def get_distance_nodes(origin, destiny):
	return geopy.distance.distance(origin, destiny).km

def get_nodes_same_destiny(csort, destiny, actual):
	res = list()
	for i in range(0,len(csort)):
		if csort[i]["destino"] == destiny and i != actual and not csort[i]["assigned"]:
			res.append(i)
	return res

def next_node(csort, actual):
	for i in range(actual+1, len(csort)):
		if not csort[i]["assigned"]:
			return i

def get_next_nodes(csort, actual, capacidad):
	lst = list()
	for i in range(actual+1, len(csort)):
		if capacidad > 0 and not csort[i]["assigned"]:
			lst.append(i)
			capacidad -= 1
	return lst

def get_prev_nodes(csort, actual, capacidad):
	lst = list()
	for i in reversed(range(actual-1, 0)):
		if capacidad > 0 and not csort[i]["assigned"]:
			lst.append(i)
			capacidad -= 1
	return lst


def search_near_nodes(csort, capacidad, actual, destinos, near):
	nodos = list()
	nodos.append(csort[actual])
	ind = near.index(csort[actual])
	weights = list()
	wtotal = get_distance_nodes(near[ind]["coordenadas"], destinos.get(near[ind]["destino"])["coordenadas"])
	if check_available(near):
		next_nodes = get_next_nodes(near, ind, capacidad)
		#prev_nodes = get_prev_nodes(near, ind, capacidad)
		same_dest = get_nodes_same_destiny(near, near[ind]["destino"], ind)
		nods = list(set(next_nodes).union(set(same_dest)))
		#nods = list(set(prev_nodes).union(set(nods)))
		for i in nods:
			w = get_distance_nodes(near[ind]["coordenadas"], near[i]["coordenadas"]) + get_distance_nodes(near[i]["coordenadas"], destinos.get(near[ind]["destino"])["coordenadas"]) + get_distance_nodes(destinos.get(near[i]["destino"])["coordenadas"], destinos.get(near[ind]["destino"])["coordenadas"])
			weights.append({"weight":w, "id":i})
		#for i in itertools.combinations(x,capacidad):
		wsorted = sorted(weights, key=itemgetter('weight'), reverse=False)
		#print(wsorted)
		for i in range(0, min(3, len(wsorted))):
			wtotal += wsorted[i]["weight"]
			#print(wsorted[i]["weight"])
			nodos.append(near[wsorted[i]["id"]])
			near[wsorted[i]["id"]]["assigned"] = True
			csort[csort.index(near[wsorted[i]["id"]])]["assigned"] = True
	else:
		dest = calculate_incidence(nodos, destinos)
		return {"ruta":nodos, "peso":wtotal, "dest":dest}
	dest = calculate_incidence(nodos, destinos)
	return {"ruta":nodos, "peso":wtotal, "dest":dest}

def search_routes(csort, taxistas, iteracion, destinos, near, history):
	pp = pprint.PrettyPrinter(indent=4)
	rutas = []
	for j in range(0, len(taxistas)):
		#print("taxista: " + str(taxistas[j]["id"]))
		if check_available(csort):
			for i in range(0, len(csort)):
				if not csort[i]["assigned"]:
					csort[i]["assigned"] = True
					capacidad = taxistas[j]["capacidad"]
					capacidad -= 1
					route_nodes = search_near_nodes(csort, capacidad, i, destinos, near)
					ruta = {"taxista":taxistas[j]["id"], "iter":iteracion-1, "route":route_nodes}
					history.append(route_nodes)
					rutas.append(ruta)
					break
	data = {}
	data["destinos"] = destinos
	data["routes"] = rutas
	return data

# ************************************************

# Relaxation ***********************************

def search_element(complete, element):
	for i in history:
		for j in i["routes"]:
			for k in j["route"]["ruta"]:
				if k == element:
					return(history.index(i), i["routes"].index(j), j["route"]["ruta"].index(k))
	return False

def check_same_destiny(element):
	for i in range(1, len(element)):
		if element[i]["destino"] != element[i-1]["destino"]:
			return False
	return True

def relax(complete, history, destinos):
	hist = sorted(history, key=itemgetter('peso'), reverse=True)
	for i in history["ruta"]:
		if not check_same_destiny(i):
			pass

# ********************************************

def calculate_incidence(coords, destinos):
	dest = dict()
	for i in coords:
		dest[i["destino"]] = destinos.get(i["destino"])
	for i in dest:
		dest[i]["moda"] = 0
	for i in coords:
		dest.get(i["destino"])["moda"] += 1
	return dest
					
def get_routes():
	iteracion = 0
	history = []
	pp = pprint.PrettyPrinter(indent=4)
	res = []
	resv = []
	referencia = (20.8878656,-89.7477136)
	coords = [
		{"coordenadas":(21.0030254,-89.7179189), "destino":0, "turno":1}, 
		{"coordenadas":(21.0336801,-89.6225203), "destino":0, "turno":0}, 
		{"coordenadas":(21.0355766,-89.6382226), "destino":0, "turno":1}, 
		{"coordenadas":(21.0463467,-89.6242708), "destino":0, "turno":0}, 
		{"coordenadas":(20.9516388,-89.6218666), "destino":0, "turno":1},
		{"coordenadas":(21.081147,-89.6627502), "destino":1, "turno":1},
		{"coordenadas":(21.0857024,-89.6621047), "destino":1, "turno":0},
		{"coordenadas":(21.0731314,-89.6587167), "destino":1, "turno":1},
		{"coordenadas":(21.07243,-89.6498347), "destino":1, "turno":0},
		{"coordenadas":(21.075004,-89.6631023), "destino":1, "turno":1},
		{"coordenadas":(21.068018,-89.6465914), "destino":2, "turno":0},
		{"coordenadas":(20.912927,-89.6019652), "destino":2, "turno":1},
		{"coordenadas":(21.067111,-89.6459344), "destino":2, "turno":0},
		{"coordenadas":(21.067476,-89.6553769), "destino":2, "turno":1},
		{"coordenadas":(21.031682,-89.6484788), "destino":3, "turno":1},
		{"coordenadas":(21.003769,-89.7057727), "destino":3, "turno":0},
		{"coordenadas":(20.998073,-89.6049088), "destino":3, "turno":1},
		{"coordenadas":(21.0438388,-89.6294418), "destino":3, "turno":0},
		{"coordenadas":(21.0347108,-89.6255674), "destino":3, "turno":1},
		{"coordenadas":(21.0123555,-89.568962), "destino":4, "turno":0},
		{"coordenadas":(20.977,-89.5852312), "destino":4, "turno":1},
		{"coordenadas":(20.95589,-89.6290147), "destino":4, "turno":0},
		{"coordenadas":(20.928956,-89.6172707), "destino":4, "turno":1},
		{"coordenadas":(20.9709102,-89.5784312), "destino":4, "turno":0},
		{"coordenadas":(20.988045,-89.5698762), "destino":4, "turno":0},
	]
	destinos = [{"id":0, "coordenadas":(21.0366944,-89.6276604)}, {"id":1, "coordenadas":(21.0710793,-89.6562318)}, {"id":2, "coordenadas":(21.0696466,-89.6471215)}, {"id":3, "coordenadas":(21.0343356,-89.6257259)}, {"id":4, "coordenadas":(21.0204019,-89.5986979)}]
	taxistas = [{"id":0, "inicio":(20.97232,-89.6401428), "capacidad":4}, {"id":1, "inicio":(20.97232,-89.6401428), "capacidad":4}]
	destinos = build_dict(destinos, key="id")

	#tom_info = destinos.get(0)

	for i in coords:
		destino = destinos.get(i["destino"])
		destino = destino["coordenadas"]
		i["destiny"] = geopy.distance.distance(destino, i["coordenadas"]).km
		i["distance"] = geopy.distance.distance(referencia, i["coordenadas"]).km
		i["assigned"] = False

	matutino = [x for x in coords if x["turno"] == 0]
	vespertino = [x for x in coords if x["turno"] == 1]

	mcsort = sorted(matutino, key=itemgetter('destino'), reverse=False)
	mnear = sorted(matutino, key=itemgetter('distance'), reverse=False)

	#calculate_incidence(matutino, destinos)
	#print(destinos)

	while check_available(mcsort):
		iteracion += 1
		it = search_routes(mcsort, taxistas, iteracion, destinos, mnear, history)
		res.append(it)

	vcsort = sorted(vespertino, key=itemgetter('destino'), reverse=False)
	vnear = sorted(vespertino, key=itemgetter('distance'), reverse=False)

	#calculate_incidence(vespertino, destinos)
	#print(destinos)

	while check_available(vcsort):
		iteracion += 1
		it = search_routes(vcsort, taxistas, iteracion, destinos, vnear, history)
		resv.append(it)
	#return(resv)
	return(resv)

def get_destinies():
	coords = [
		{"coordenadas":(21.0030254,-89.7179189), "destino":0}, 
		{"coordenadas":(21.0336801,-89.6225203), "destino":0}, 
		{"coordenadas":(21.0355766,-89.6382226), "destino":0}, 
		{"coordenadas":(21.0463467,-89.6242708), "destino":0}, 
		{"coordenadas":(20.9516388,-89.6218666), "destino":0},
		{"coordenadas":(21.081147,-89.6627502), "destino":1},
		{"coordenadas":(21.0857024,-89.6621047), "destino":1},
		{"coordenadas":(21.0731314,-89.6587167), "destino":1},
		{"coordenadas":(21.07243,-89.6498347), "destino":1},
		{"coordenadas":(21.075004,-89.6631023), "destino":1},
		{"coordenadas":(21.068018,-89.6465914), "destino":2},
		{"coordenadas":(20.912927,-89.6019652), "destino":2},
		{"coordenadas":(21.067111,-89.6459344), "destino":2},
		{"coordenadas":(21.067476,-89.6553769), "destino":2},
		{"coordenadas":(21.031682,-89.6484788), "destino":3},
		{"coordenadas":(21.003769,-89.7057727), "destino":3},
		{"coordenadas":(20.998073,-89.6049088), "destino":3},
		{"coordenadas":(21.0438388,-89.6294418), "destino":3},
		{"coordenadas":(21.0123555,-89.568962), "destino":4},
		{"coordenadas":(20.977,-89.5852312), "destino":4},
		{"coordenadas":(20.95589,-89.6290147), "destino":4},
		{"coordenadas":(20.928956,-89.6172707), "destino":4},
		{"coordenadas":(20.9709102,-89.5784312), "destino":4},
		{"coordenadas":(20.988045,-89.5698762), "destino":4},
		{"coordenadas":(21.0347108,-89.6255674), "destino":3}
	]
	destinos = [{"id":0, "coordenadas":(21.0366944,-89.6276604)}, {"id":1, "coordenadas":(21.0710793,-89.6562318)}, {"id":2, "coordenadas":(21.0696466,-89.6471215)}, {"id":3, "coordenadas":(21.0343356,-89.6257259)}, {"id":4, "coordenadas":(21.0204019,-89.5986979)}]
	destinos = build_dict(destinos, key="id")

	#tom_info = destinos.get(0)

	for i in coords:
		destino = destinos.get(i["destino"])
		destino = destino["coordenadas"]
		i["destiny"] = destino

	return(coords)

#pp.pprint(csort)
