import random
def c() :
    a = ["1" , "2" , "3" , "4" , "5" , "6"]
    b = random.choice(a)
    if b=="1" :
        print("your turn is 1 ")
    elif b=="2" : 
        print("your turn is 2 ") 
    elif b=="3" : 
        print("your turn is 3 ")
    elif b=="4" : 
        print("your turn is 4 ")  
    elif b=="5" : 
        print("your turn is 5 ")
    elif b=="6" : 
        print("your turn is 6 ")    
    go = input("choose n to go next round : ")
    if go=="n" :
        c()
    else :
        print("your choose is incorrect")
        c()
c()    
