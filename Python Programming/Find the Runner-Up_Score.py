if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # Find the Runner-Up Score! in Python - Hacker Rank Solution START
    print(sorted(list(set(arr)))[-2])
    # Find the Runner-Up Score! in Python - Hacker Rank Solution END