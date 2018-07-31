import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from reader import reader as TSPLIB
import config

tour = 'tour_0'

def main():
    tsp_reader = TSPLIB(config.test_path)
    cities_raw = TSPLIB.cities[:]
    cities = get_cities(tsp_reader)

    #print(tsp_reader.cities[0])
    route = get_tour(cities_raw)

    draw_graph(cities, route)

def get_distance(a, b):
    dist = np.sqrt( (a['x'] - b['x'])**2 + (a['y'] - b['y'])**2 )
    return dist

def get_tour(cities_raw):
    tour_file = config.folder + '\\' + config.test + '\\' + tour + '.tsp'
    tsp_tour = TSPLIB(tour_file)
    del tsp_tour.cities[:]
    tsp_tour = TSPLIB(tour_file)
    #print(len(tsp_tour.cities))
    
    x = []
    y = []
    for t in tsp_tour.cities:
        #print(t)
        if t['index'] == -1:
            break
        for c in cities_raw:
            #print(c)
            if c['index'] == t['index']:
                x.append(c['x'])
                y.append(c['y'])
                break

    total_distance = 0
    for i in range(len(x)-1):
        a = {'x': x[i], 'y': y[i]}
        b = {'x': x[i+1], 'y': y[i+1]}
        total_distance += get_distance(a,b)
    total_distance += get_distance({'x': x[0], 'y': y[0]},{'x': x[-1], 'y': y[-1]})
    print(total_distance)
    #print(len(x))
    return {'x':x, 'y': y}

def get_cities(tsp_reader):
    cities_x = []
    cities_y = []
    for c in tsp_reader.cities:
        #print(c)
        cities_x.append(float(c['x']))
        cities_y.append(float(c['y']))

    return {'x': cities_x, 'y':cities_y}

def draw_graph(cities, route):

    #plt.scatter(cities['x'],cities['y'], marker='x')
    plt.plot(route['x'], route['y'])
    plt.tight_layout()
    plt.axis('off')
    plt.show()

main()

