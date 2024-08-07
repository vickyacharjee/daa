# Number of vertices
nV = 4
INF = 999

# Algorithm
def floyd(G):
    dist = [row[:] for row in G]  # Create a copy of the graph

    # Adding vertices individually
    for r in range(nV):
        for p in range(nV):
            for q in range(nV):
                dist[p][q] = min(dist[p][q], dist[p][r] + dist[r][q])
    
    sol(dist)

# Printing the output
def sol(dist):
    for p in range(nV):
        for q in range(nV):
            if dist[p][q] == INF:
                print("INF", end=" ")
            else:
                print(dist[p][q], end=" ")
        print()

# Input
G = [
    [0, 5, INF, INF],
    [50, 0, 15, 5],
    [30, INF, 0, 15],
    [15, INF, 5, 0]
]

floyd(G)
