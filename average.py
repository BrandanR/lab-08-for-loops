average = 0
sum = 0

for i in range(0, 4):
    userinput = input("Number please... ")
    usernum = int(userinput)
    sum = sum + usernum
    print("User input is: " + str(usernum) + " and the current sum is: " + str(sum))

average = sum / 4
print("The average is: " + str(average))
