num =int(input("Enter Number: "))

digits =0
sm = 0

while num > 0:
    rm = num %10 
    num = num // 10
    digits += 1
    sm = sm+rm
#     print("reminder {} number {}".format(rm,num))

print("Total digits: ",digits)
print("Sum: ",sm)
