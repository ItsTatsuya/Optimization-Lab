import random
import math

n = 5

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_distance(path):
    dist = 0
    for i in range(1, len(path)):
        dist += distance(path[i-1], path[i])
    dist += distance(path[-1], path[0])
    return dist

def random_path():
    path = list(range(n))
    random.shuffle(path)
    return path


def swap(path):
    i, j = random.sample(range(n), 2)
    path[i], path[j] = path[j], path[i]
    return path

def anneal():
    path = random_path()
    T = 1.0
    T_min = 0.00001
    alpha = 0.9
    while T > T_min:
        i = 1
        while i <= 100:
            new_path = swap(path[:])
            old_dist = total_distance(path)
            new_dist = total_distance(new_path)
            ap = math.exp((old_dist - new_dist) / T)
            if ap > random.random():
                path = new_path
            i += 1
        T *= alpha
    return path

cities = [(random.randint(0, 100), random.randint(0, 100)) for i in range(n)]
print("Cities:", cities)
print("Path:", anneal())