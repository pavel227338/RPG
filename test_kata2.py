#https://www.codewars.com/kata/550554fd08b86f84fe000a58/train/python
a1 = ["ive", "a", "stong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
def in_array(array1, array2):
    r = []
    for i in array1:
        for k in array2:
            if i in k and not i in r:
                r.append(i)
    return sorted(r)
print(in_array(a1,a2))