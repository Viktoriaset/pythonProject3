import numpy as np
import random


class TspTestGenerator:

    file_path: str

    def __init__(self, file_path):
        self.file_path = file_path

    def generate(self, num_cities, min_distance, max_distance):
        test_case = self.generate_tsp_test(num_cities, min_distance, max_distance)
        self.write_test_to_file(test_case, self.file_path)

    def generate_tsp_test(self, num_cities, min_distance, max_distance):
        distances = np.zeros((num_cities, num_cities), dtype=int)

        for i in range(num_cities):
            for j in range(i + 1, num_cities):
                distance = random.randint(min_distance, max_distance)
                distances[i][j] = distance
                distances[j][i] = distance

        for k in range(num_cities):
            for i in range(num_cities):
                for j in range(num_cities):
                    if i != j and i != k and j != k:
                        distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

        test_case = ""
        for i in range(num_cities):
            for j in range(i + 1, num_cities):
                test_case += f"{i+1} {j+1} {distances[i][j]}\n"

        return test_case

    def write_test_to_file(self, test_case, file_path):
        with open(file_path, "w") as file:
            file.write(test_case)