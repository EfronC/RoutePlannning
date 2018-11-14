from pykml import parser
from os import path
import googlemaps
from datetime import datetime
import pprint

kml_file = path.join('gasolinerasLodemored.kml')
pp = pprint.PrettyPrinter(indent=4)
vivesano = (20.990054,-89.5965152)

key = ""

gmaps = googlemaps.Client(key='')

# Request directions via public transit
now = datetime.now()
#directions_result = gmaps.directions(origin=vivesano,destination=(20.9903751,-89.5945818),departure_time=now)
#print(directions_result[0]["legs"][0]["distance"]["text"])
#pp.pprint(directions_result)

#20.885919,-89.5523507
#21.287271,-89.7602747

def isBetween(lon, lat):
  infr = (20.885919,-89.5523507)
  supl = (21.287271,-89.7602747)
  if abs(lat) < abs(supl[0]) and abs(lat) > abs(infr[0]) and abs(lon) < abs(supl[1]) and abs(lon) > abs(infr[1]):
    return True
  else:
    return False

with open(kml_file) as f:
  doc = parser.parse(f).getroot()

for e in doc.Document.Folder.Placemark:
  coor = e.Point.coordinates.text.split(',')
  if isBetween(float(coor[0]), float(coor[1])):
    print(e.name.text)
    print(coor)
    directions_result = gmaps.directions(origin=vivesano,destination=(float(coor[1]),float(coor[0])),departure_time=now)
    print(directions_result[0]["legs"][0]["distance"]["text"])

    print("")

