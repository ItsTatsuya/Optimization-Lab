#include <iostream>
#include <algorithm>
#include <climits>

const int MAX_CITIES = 10;

int calculateTotalDistance(int path[], int numCities, int graph[MAX_CITIES][MAX_CITIES]) {
    int totalDistance = 0;
    for (int i = 0; i < numCities - 1; ++i) {
        totalDistance += graph[path[i]][path[i + 1]];
    }
    totalDistance += graph[path[numCities - 1]][path[0]];
    return totalDistance;
}

void printPath(int path[], int numCities) {
    for (int i = 0; i < numCities; ++i) {
        std::cout << path[i] << " ";
    }
    std::cout << path[0]; // To show the return to the starting city
    std::cout << std::endl;
}

int main() {
    int numCities;
    std::cout << "Enter the number of cities: ";
    std::cin >> numCities;

    if (numCities > MAX_CITIES) {
        std::cout << "Exceeded maximum allowed cities." << std::endl;
        return 1;
    }

    int graph[MAX_CITIES][MAX_CITIES];

    std::cout << "Enter the adjacency matrix for the cities:\n";
    for (int i = 0; i < numCities; ++i) {
        for (int j = 0; j < numCities; ++j) {
            std::cin >> graph[i][j];
        }
    }

    int path[MAX_CITIES];
    for (int i = 0; i < numCities; ++i) {
        path[i] = i;
    }

    int minDistance = INT_MAX;

    do {
        int currentDistance = calculateTotalDistance(path, numCities, graph);
        if (currentDistance < minDistance) {
            minDistance = currentDistance;
            std::cout << "New minimum distance: " << minDistance << " - Path: ";
            printPath(path, numCities);
        }
    } while (std::next_permutation(path + 1, path + numCities));

    std::cout << "Minimum distance: " << minDistance << std::endl;

    return 0;
}
