stay = True
action = input("First Action:")

def handle(action = action, stay = stay):
    match action:
        case ":q":
            stay = False
        case ":c":
            f = open("result.txt", "w")
            f.write("")
            f.close()
        case ":r":
            try:
                f = open("result.txt", "r")
                print(f.read())   
            except:
                print("No File Was Made")
            
        case _:
            f = open("result.txt", "a")
            f.write(action)
            f.close()
    return stay



handle()
stay = handle()
while(stay):
    action = input("Next Action:")
    stay = handle(action)


    


