#match====similar to switch in java
num=int(input("Enter a number"))
match num:
    case 1:
        print("you have entered 1")
    case 2:
        print("you have entered 2")
    case _: #nothing is matching,i will run(_)
        print("no idea")


