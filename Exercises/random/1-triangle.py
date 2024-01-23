


def kkk(x, y, z):
    if(x+y>z and y+z>x and x+z>y ):
        return "exists"
    else:
        return "does not exist"


def bbb(alfa,beta,gamma):
    if (alfa+beta+gamma==180):
        return "exists"
    else:
        return "does not exist"
def bkb(x,beta,y):
    if (beta<180 and x*2>y and y*2>x):
        return "exists"
    else:
        return "does not exist"
def kbk(alfa,x,gamma):
    if (alfa+gamma<=180):
        return "exists"
    else:
        return "does not exist"

def triangle():
    print("chose mode:\n"
          "kkk:1\n"
          "kbk:2\n"
          "bkb:3\n"
          "bbb:4\n")
    mode = int(input("input mode here :"))
    x = int(input("first val: "))
    y = int(input("second val: "))
    z = int(input("third val: "))
    match(mode):

        case 1:
            print(kkk(x,y,z))

        case 2:
            print(kbk(x, y, z))
        case 3:
            print(bkb(x, y, z))
        case 4:
            print(bbb(x, y, z))

if(__name__ == "__main__"):
    triangle()


