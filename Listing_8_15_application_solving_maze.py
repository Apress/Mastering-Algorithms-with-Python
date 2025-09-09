def solve_maze(start_x, start_y, end_x, end_y, maze):
    R, C = len(maze), len(maze[0])
    level = 1
    stack = [(start_x, start_y, level)]
    visited = set()
    path = []
    while stack:
        print ('stack', stack)
        cur_x, cur_y, cur_level = stack.pop() 
        if cur_x == end_x and cur_y == end_y:
            path.append((cur_x, cur_y, cur_level))
            return path 

        visited.add((cur_x, cur_y))

        # update path
        while path:
            prev_level = path[-1][-1]
            if cur_level <= prev_level:
                path.pop()
            else:
                break 

        path.append((cur_x, cur_y, cur_level))
        print ('visited', visited)

        for direction_x, direction_y in [(0, 1),(0, -1),(1, 0),(-1, 0)]: # right, left, down, up  
            new_x = direction_x + cur_x
            new_y = direction_y + cur_y
            new_level = cur_level + 1
            if (0 <= new_x < R and 
                0 <= new_y < C and 
                maze[new_x][new_y] and  
                (new_x, new_y) not in visited):
                stack.append((new_x, new_y, new_level))

        print ("path", path)

if __name__ == "__main__":
    # 0 is wall; 1 is path
    maze = [[0,0,0,0,0], 
            [0,1,0,1,0],
            [0,1,1,1,0],
            [0,1,0,1,0],
            [0,0,0,1,0]]

    print (solve_maze(1, 1, 4, 3, maze))
