# Maze Solver Project

This project implements three different algorithms to solve maze problems by finding the shortest path from a starting point (S) to a goal (G) while collecting the least amount of coins. Movement is allowed in 8 directions, including diagonals. 

- Github link to project: https://github.com/mrspacexx/MazeSolverProject

## Project Files

- maze_solver.py - Dijkstra algorithm
- astar_solver.py - A* algorithm
- greedy_solver.py - Greedy Best-First Search
- run_all.py - Runs all algorithms and saves output
- maze1.txt, maze2.txt, maze3.txt - Sample mazes
- results.txt - Output with coin totals and complexity
- README.md - Project description

## Group Members

- Efehan Aras 221ADB079
- Ataberk Akçin 211AIB121
- Babak Gasimzade 221ADB125

## Algorithms Used

Dijkstra:
- Guaranteed optimal path
- Explores based on actual cost

A*:
- Uses both path cost and estimated goal distance
- Faster than Dijkstra in many cases
- Still guarantees the optimal solution

Greedy Best-First Search:
- Uses only heuristic distance
- Very fast but may return suboptimal results

## Time and Space Complexity

Dijkstra:
- Time: O(V + E log V)
- Space: O(V)

A* Search:
- Time: O(V log V) (depends on heuristic accuracy)
- Space: O(V)

Greedy Best-First Search:
- Time: O(V log V)
- Space: O(V)
- Note: May return a solution with more coins

V = Total number of accessible (non-wall) cells in the maze.
E = Total number of possible valid movements between cells. Each cell can have up to 8 connections (including diagonal directions).

## How to Run

To run all algorithms and save results:

    python run_all.py

This will generate the results.txt file with coin totals and complexity info for each maze.

## Maze Format

Each maze is a text file using the following format:

- S = Start
- G = Goal
- X = Wall
- 0–9 = Coin value in that cell