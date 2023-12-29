from collections import deque

def find_shortest_path(maze):
    rows, cols = len(maze), len(maze[0])
    start, end = None, None

    # Find the starting and ending points in the maze
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)

    # Possible moves: up, down, left, right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        current, steps = queue.popleft()
        i, j = current

        if current == end:
            return steps

        for move in moves:
            new_i, new_j = i + move[0], j + move[1]

            if 0 <= new_i < rows and 0 <= new_j < cols and maze[new_i][new_j] == '.' and (new_i, new_j) not in visited:
                queue.append(((new_i, new_j), steps + 1))
                visited.add((new_i, new_j))

    return -1  # No valid path found