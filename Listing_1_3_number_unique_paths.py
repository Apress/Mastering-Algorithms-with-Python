def count_unique_paths(m, n):
    if m == 1 or n == 1:
        return 1
    return count_unique_paths(m-1, n) + count_unique_paths(m, n-1)

if __name__ == "__main__":
    print (count_unique_paths(7,4))
