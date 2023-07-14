from tcp_test import TspTestGenerator
from bruteForce import tsp_brute_force
from Christophides import Chritophides

if __name__ == "__main__":
    file = 'tcp_test/inputData/graph.txt'
    test_generator = TspTestGenerator.TspTestGenerator(file)
    bruteForce = tsp_brute_force.tsp_brute_force(file)
    christophides = Chritophides.Christophides(file)

    for i in range(1, 100):
        test_generator.generate(5, 1, 100)
        bruteForce.build()
        christophides.findTraversal()
        if christophides.weight <= (bruteForce.optimal_distance * 3 / 2):
            print('good')
        else:
            print(bruteForce.optimal_distance)
            print(bruteForce.optimal_route)
            print(christophides.weight)
            print(christophides.traversal)
            print('bad')
            break