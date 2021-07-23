if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    # Tuples in Python - Hacker Rank Solution START
    t = tuple(integer_list)
    print(hash(t));
    # Tuples in Python - Hacker Rank Solution END