def knight_tour(initial_pos, R=8, C=8):
    target_level = R * C 
    directions = [(-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1)]
    stack = [(initial_pos[0], initial_pos[1], 1)] # level 1
    visited_positions = []
    while stack:
        prev_level = visited_positions[-1][-1] if visited_positions else 1 
        x, y, cur_level = stack.pop()
        # backtrack --> update the visited
        if cur_level <= prev_level: 
            while visited_positions and visited_positions[-1][-1] >= cur_level:
                visited_positions.pop()
        # add to visited 
        visited_positions.append((x, y, cur_level))
        # add children to stack
        for direction_x, direction_y in directions[::-1]:
            new_x = x + direction_x
            new_y = y + direction_y
            if 0 <= new_x < R and 0<= new_y < C: 
                if not any(new_x == pos_x and new_y == pos_y for pos_x, pos_y, _ in visited_positions):
                    stack.append((new_x, new_y, cur_level + 1))
        if cur_level == target_level:
            return visited_positions
    return "Cannot tour the board"

if __name__ == "__main__":
    print (knight_tour((2,2), R=5, C=5))
    #print (knight_tour((2,3), R=8, C=8))