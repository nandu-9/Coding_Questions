
# Minimization Function
def func(R, L):

    # Base Case
    if (L[0] != R[-1]):
        return

    L.pop(0)
    R.pop(-1)

    # Recurance
    func(R, L)
    return R, L


# Testing
val = "aabcccabba"
val = list(val)
left = val[:len(val)//2]
right = val[len(val)//2:]

print(left)
print(right)
print()

R, L = func(right, left)
print(L)
print(R)



# Testing full code
val_2 = "aabcccabba"
val_2 = list(val_2)
n = len(val)
minLength_dict = {}

# Note: i is the split index
for i in range(2,n-2):

    left = val_2[0:i]
    right = val_2[i:]

    final_right, final_left = func(left,right)
    
    total_word = final_left + final_right
    minLength_dict["".join(total_word)] = len(total_word)

print(minLength_dict)