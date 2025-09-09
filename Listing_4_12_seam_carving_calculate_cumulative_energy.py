def calculate_cumulative_energy(E):
    R, C = len(E), len(E[0])
    cumu_E = [[0 for _ in range(C)] for _ in range(R)]
    cumu_E[0] = E[0]
    for r in range(1, R):
        for c in range(C):
            if c == 0:
                cumu_E[r][c] = E[r][c] + min(cumu_E[r-1][c], cumu_E[r-1][c+1])
            elif c == C-1:
                cumu_E[r][c] = E[r][c] + min(cumu_E[r-1][c-1], cumu_E[r-1][c])
            else:
                cumu_E[r][c] = E[r][c] + min(cumu_E[r-1][c-1], cumu_E[r-1][c], cumu_E[r-1][c+1])
    return cumu_E

if __name__ == "__main__":
    E = [[5, 1, 2, 4, 3], [1, 8, 3, 2, 5], [1, 3, 4, 2, 8]]
    print (calculate_cumulative_energy(E))