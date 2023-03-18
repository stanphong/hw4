def cacti_number(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                if i == 0 or arr[i-1][j] == 0:
                    if j == 0 or arr[i][j-1] == 0:
                        if i == len(arr)-1 or arr[i+1][j] == 0:
                            if j == len(arr[0])-1 or arr[i][j+1] == 0:
                                count += 1
                                arr[i][j] = 1
    return count
