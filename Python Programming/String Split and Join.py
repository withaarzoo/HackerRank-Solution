def split_and_join(line):
    # write your code here
    
    # String Split and Join in Python - HackerRank Solution START
    Output = line.split();
    Output = "-".join(Output)
    return Output;
    # String Split and Join in Python - HackerRank Solution END
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)