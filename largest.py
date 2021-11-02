x = 0
for i in range(1, 5):
    number = int(input("Number please... "))
    print(number)
    if number > x:
        x = number
print("The largest number is", x)
