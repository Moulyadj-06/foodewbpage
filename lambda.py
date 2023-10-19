double = lambda x: x*2
add = lambda x,y: x+y

num = int(input("ENTER A NUMBER:"))
num1 = int(input("ENTER THE FIRST NUMBER:"))
num2 = int(input("ENTER THE SECOND NUMBER:"))

result1 = double(num)
result2 = add(num1, num2)

print("double of", num, "is", result1)
print("addition of", num1, "and", num2, "is", result2)

