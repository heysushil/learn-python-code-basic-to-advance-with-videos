# scope local | global

# local

# function ke angar koi bhi variabel funciton tak hi seemit hai means uska use function ke bahr nhi kar sakte hai.

# funciton ke bar ke varible ko fucntion ke andar use kar sakte hai.

x = 100


def userfun():
    # x is local varaibe of userfun()
    # gloable keyword use me make varibale gloable access
    global x
    x = 10
    print('inner function Local:' ,x)
    # def againfun():
    #     print('agin fun Local:' ,x)

    # againfun()

userfun()    

print('Outer Local: ',x)
# x = 100
# print('Outer Local: ',x)