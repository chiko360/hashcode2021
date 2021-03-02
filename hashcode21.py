def car_duration(car,streets):
  duration = 0
  i = 0
  for street in car :
      if (i==0): i=i+1
      else : duration += int(streets[street][2])
  return duration
 
def input_streets(id_int):
  strs = []
  for street in streets.items() :
      if street[1][1] == id_int :
          strs.append(street[0])
  return strs
 
def D90(D, cars, streets):
  cars90=[]
  value = 0.8*D
  for car in cars:
      if car_duration(car, streets) < value:
          cars90.append(car)
  return cars90
 
 
def add_num_cars_in_street(cars, streets):
   news = dict()
 
   for car in cars :
       for st in car :
           news[st] = news.get(st,0) + 1
   lis = list(streets.keys())
  
  
   for st in lis :
       if st not in news.keys() : continue
       news[st] = streets[st] + [news[st]]
  
   return news
 
def make_intersections(streets):
   inters = {}
   lis = list(streets.keys())
   for st in lis :
       print(st,streets[st])
       id_inter = streets[st][1]
       if id_inter in inters.keys() : continue
       inters[id_inter] = dict()
       list_sts = input_streets(id_inter)
       for street in list_sts:
           cur_st = streets[street]
           num_cars = cur_st[3]
           duration = cur_st[2]
           value = round(num_cars+4)
           if value == 0 : value = value+1
           #print(inters[id_inter])
 
           inters[id_inter].update({street:value})
   return inters
 
 
 
 
path = 'e.txt'
file = open(path).read()
data = file.split('\n')
first_ligne = data[0].split(' ')
duration = first_ligne[0]
nb_inter = first_ligne[1]
nb_streets = first_ligne[2]
nb_cars = first_ligne[3]
bonnus_points = first_ligne[4]
streets_0 = data[1:int(nb_streets)+1]
cars_0 = data[int(nb_streets)+1:]
streets = dict()
cars = []
for street in streets_0:
   street = street.split(' ')
   name = street.pop(2)
   streets[name]= street
for car in cars_0:
   cars.append(car.split(' ')[1:])
 
#cars = D90(int(duration),cars,streets)
#print(streets, '\n', cars)
#print(streets)
streets = add_num_cars_in_street(cars,streets)
#print(streets)
intersections = make_intersections(streets)
out = ''
out = out + str(len(intersections)) + '\n'
for id in (intersections.keys()):
   out = out + id + '\n' + str(len(intersections[id])) + '\n'
   for street in intersections[id].keys():
       out = out + street + ' ' + str(intersections[id][street]) + '\n'
outpath = 'out ' + path
outfile = open(outpath, 'w')
outfile.write(out)