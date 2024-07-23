# 1st------------------------------------------------------------------

ages = {}
ages['Anton'] = 21
ages['Beth'] = ages['Anton'] + 6
ages['Chen'] = ages['Beth'] + 20
ages['Drew'] = ages['Chen'] + ages['Anton']
ages['Ethan'] = ages['Chen']
for name, age in ages.items():
    print(f"{name} is {age} years old.")

# 2nd------------------------------------------------------------------

name1:str = "Alice"
age1:int = 30
city:str = "New York"

print(f"{name1} is {age1} years old. He lives in {city}.")

# 3rd------------------------------------------------------------------

s = "hElLo WoRlD"
s = s.capitalize()

print(s)

s = "hElLo WoRlD"
s = s.upper()

print(s)

s = "hElLo WoRlD"
s = s.lower()

print(s)

# 4th------------------------------------------------------------------

s ="the quick brown fox jumps over the lazy dog"
index_fox = s.find("fox")
count_the = s.count("the")

print("Index of 'fox':", index_fox)
print("Occurrences of 'the':", count_the)

# 5th------------------------------------------------------------------

s ="I love programming in Python"
new_s = s.replace("Python", "Java")

print(new_s)

# 6th------------------------------------------------------------------

s = "apple,banana,cherry,dates"
s_list = s.split(",")
result = " ".join(s_list)

print(s_list)
print(result)

# 7th------------------------------------------------------------------

s ="   Python is fun!   "
s_stripped = s.strip()
s_left_justified = s.ljust(20, '*')
s_right_justified = s.rjust(20, '*')

print("Original string:", s)
print("After removing leading/trailing spaces:", s_stripped)
print("Left justified with '*':", s_left_justified)
print("Right justified with '*':", s_right_justified)

# 8th------------------------------------------------------------------

num:int = 45
binary_representation = bin(num)[2:]

print("Binary representation:", binary_representation)

# 9th------------------------------------------------------------------

base = 3
exponent = 4
result = pow(base, exponent)

print(result)

# 10th------------------------------------------------------------------

value:float = 12.34567
rounded_integer = round(value)
rounded_decimal = round(value, 2)

print("Rounded integer:", rounded_integer)
print("Rounded decimal:", rounded_decimal)
