num = input("Enter a number : \n")
count = 0
if(num == 0 or num == 1):
    print("The number is not prime")
else :
    for i in range (1,num):
        if(num/i == 0):
            count += 1
    print(count)
    if(count >= 1):
        print("The number is not prime")
    else :
        print("The number is prime")
