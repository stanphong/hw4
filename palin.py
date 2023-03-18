def palindrome(list):
    i = 0
    j = len(list) - 1
    while (i < j):
        if (list[i] != list[j]):
            return False
        i += 1
        j -= 1
    return True
