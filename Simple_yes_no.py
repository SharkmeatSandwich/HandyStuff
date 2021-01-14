def yes_or_no():
    YesNo = input("Yes or No?")
    YesNo = YesNo.lower()
    if(YesNo == "yes" or "y"):
        return 1
    elif(YesNo == "no" or "n"):
        return 0
    else:
        print("Incorrect Selection, Please Try Again...")
        return yes_or_no()

answer = yes_or_no()

if(answer) == 1 :
    print("You said yeah!")
elif(answer) == 0 :
    print("You said nah!")
