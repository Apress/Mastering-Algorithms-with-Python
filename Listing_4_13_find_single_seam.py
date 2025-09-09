def find_single_seam_from_cumu_energy(cumu_E):
    R, C = len(cumu_E), len(cumu_E[0])
    col_indexes_to_be_removed = []
    # index to be removed at last row
    last_col_index = cumu_E[-1].index(min(cumu_E[-1]))
    col_indexes_to_be_removed.append(last_col_index)
    for r in range(R-1, 0, -1):
        if last_col_index == 0:
            if cumu_E[r-1][0] <= cumu_E[r-1][1]:
                second_last_index = 0
            else:
                second_last_index = 1
        elif last_col_index == C - 1:
            if cumu_E[r-1][C-2] <= cumu_E[r-1][C-1]:
                second_last_index = C-2
            else:
                second_last_index = C-1
        else:
            cumu_energy_second_last = [(cumu_E[r-1][last_col_index -1], last_col_index -1),  
                                       (cumu_E[r-1][last_col_index], last_col_index), 
                                       (cumu_E[r-1][last_col_index + 1],last_col_index + 1)]
            cumu_energy_second_last.sort()
            second_last_index = cumu_energy_second_last[0][1]
        last_col_index = second_last_index
        col_indexes_to_be_removed.append(last_col_index)
    seam_pixels_indexes = [(r, c) for r, c in zip(range(R), col_indexes_to_be_removed[::-1])]
    return seam_pixels_indexes

if __name__ =="__main__":
    cumu_E =[[5, 1, 2, 4, 3], [2, 9, 4, 4, 8], [3, 5, 8, 6, 12]]
    print (find_single_seam_from_cumu_energy(cumu_E))