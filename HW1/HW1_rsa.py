# HW1
# Group 001

bearcatii = {" ": 0}

def constr_bearcatii():
    for i in range(26):
        char = ord('a') + i
        bearcatii[chr(char)] = i + 1
constr_bearcatii()

# Converts a string to bearcatii
def convert_S_to_B(s):
    b = []
    for c in s:
        b.append(bearcatii[c])
    return b

# Converts a list of numbers from base pow to base 10
def to_base_ten(list_of_nums, pow=27):
    sum = list_of_nums[0]
    for num in list_of_nums[1:]:
        sum = sum*pow + num
    return sum

# Converts a number from decimal to base in list form
def from_base_ten(num, base=27):
    nums = []
    while num > 0:
        mod = num % base
        nums.append(mod)
        num = num // base
    return nums[::-1]


test = convert_S_to_B("test")
print(test)
test_ten = to_base_ten(test)
print(test_ten)
test_from = from_base_ten(test_ten)
print(test_from)

# TO-DO: Miller-Rabin
# TO-DO: main()
