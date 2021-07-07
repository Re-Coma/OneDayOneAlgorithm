def levenstein(str1: str, str2: str):
    # Init1
    # str1 가로축, str2 세로축
    str1_size = len(str1) + 1
    str2_size = len(str2) + 1
    matrix = [[0 for _ in range(str1_size)] for _ in range(str2_size)]

    # Init2
    
    
    for j in range(str1_size):
        matrix[0][j] = j
    
    for i in range(str2_size):
        matrix[i][0] = i
    

    # Start Checking
    
    for i in range(1, str2_size):
        for j in range(1, str1_size):
            if str1[j - 1] == str2[i - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
    
    
    for i in range(len(matrix)):
        print(matrix[i])

    return matrix[-1][-1]
r1 = levenstein("cats", "facts")
print(r1)