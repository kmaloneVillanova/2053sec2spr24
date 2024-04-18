print("hello world!")

# this is a comment

'''
this is one line of comments
this is another
'''

# Variables
x = 10 
print(x)
s = "hello"
x = s
print(x)

# Math operators
x = 100
y = 10
r = x / y
print(r)
r = int(x/y)
print(r)
r = x // y
print(r)

# math functions
m = min(200,20)
print(m)
r = pow(2, 4)
print(r)
r = 2**4
print(r)

# if statements
x = -1
y = 1
if x < 0:
    x = 1
    x += 10
    print("x was negative")

if x < 0 and y ==1:
    print("x is negative and y is 1")

if x < 0 or y == 1:
    print("x is negatvie or y is 1")

# Loops
nums = [10,20,30,40,50]
for i in range(len(nums)):
    print(nums[i])

for val in nums:
    val += 5
    print(val)
print(nums)

for i, val in enumerate(nums):
    print("i is", i, "and val is",val)

dogs=["boomer","rocky","daisy"]

nums=[1,2,3,4,5]
sum_nums=0
for num in nums:
    sum_nums += num
print("sum of nums is", sum_nums)
print(f"the sum of nums is {sum_nums}")

def hello(name="friend"):
    print("hello!",name)
hello("Bob")
hello()

platform_computing="platform computing"
platform = platform_computing[:8]
computing = platform_computing[9:]

nums = [0,3,8,5,4]
temp=nums[2]
nums[2]=nums[4]
nums[4]=temp
print(nums)










