def point(x):
    if(x >= 0):
        if(x < 12):
            print("رد")
        elif(x < 17):
            print("عادی")
        elif(x <= 20):
            print("ممتاز")
        else:
            print("لطفا نمره کمتر از 20 باشه")
    else:
        print("لطفا نمره بزرگتر مساوی 0 باشه")
        
point(9.75)

input()