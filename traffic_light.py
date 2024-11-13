choice='y'
while(choice=='y'):
    colour=input("Enter the colour...:")
    if(colour=="yellow" or colour=="YELLOW"):
        print("You need to wait until the green signal is shown!!!")
    elif(colour=="RED" or colour=="red"):
        print("You have to stop or you will be fined with Rs.10000")
    elif(colour=="GREEN" or colour=="green"):
        print("Now you can continue your journey .. Radhe Radhe!")
    else:
        print("Please enter a valid traffic light colour!")
    choice=input("Do you want to continue:(y/n)...:")
    if(choice=='y'):
        continue
    else:
        break