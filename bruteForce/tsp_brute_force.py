import itertools


class tsp_brute_force:
    file_path: str
    optimal_distance: int = 0
    optimal_route: list

    def __init__(self, file_path):
        self.file_path = file_path
        self.optimal_route = list()

    def build(self):
        cities, distances = self.parce_file()
        self.optimal_distance, self.optimal_route = self.brute_force_tsp(cities, distances)

    def parce_file(self):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            cities = set()
            distances = {}
            for line in lines:
                values = line.split()
                city1 = int(values[0])
                city2 = int(values[1])
                distance = int(values[2])
                cities.add(city1)
                cities.add(city2)
                key = tuple(sorted([city1, city2]))
                distances[key] = distance
        return cities, distances
    def calculate_distance(self, route, distances):
        distance = 0
        num_cities = len(route)
        for i in range(num_cities - 1):
            city1 = route[i]
            city2 = route[i + 1]
            key = tuple(sorted([city1, city2]))
            distance += distances[key]
        key = tuple(sorted([route[num_cities - 1], route[0]]))
        distance += distances[key]
        return distance

    def brute_force_tsp(self, cities, distances):
        min_distance = float('inf')
        optimal_route = None

        for permutation in itertools.permutations(cities):
            distance = self.calculate_distance(permutation, distances)
            if distance < min_distance:
                min_distance = distance
                optimal_route = permutation

        return min_distance, optimal_route
