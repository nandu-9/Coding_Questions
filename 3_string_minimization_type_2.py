def minLength(s, stop_1_iter):
    i = 0
    j = len(s)-1

    # perform while till the string is not empty and
    # the first and last characters are same
    while((i < j) & (s[i] == s[j])):

        # Current character on left pointer
        d = s[i]

        # Shift i towards right
        while((i <= j) and (d == s[i])):
            i += 1

        # Shift j towards left
        while((i <= j) and (d == s[j])):
            j -= 1

        if (stop_1_iter == True):
            print(s[i:j])
            return (j-i)+1

    # Finally return the minimum possible length of the string
    print(s[i:j+1])
    return j - i + 1


val = str("aabcccabba")
print(minLength(val, stop_1_iter=False))
