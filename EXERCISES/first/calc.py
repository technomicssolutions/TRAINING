def calculator():
    choice = 0
    while(choice!=5):
        print "1.) addition"
        print "2.) subtraction"
        print "3.) multiplication"
        print "4.) division"
        print "5.) exit"
        choice = raw_input("enter your choice")
        if choice == "1":
            add()
        elif choice == "2":
            sub()
        elif choice == "3":
            mult()
        elif choice == "4":
            div()
        elif choice == "5":
            exit(0)  
def add():
    print "enter two numbers to add"
    a = int(raw_input("enter a:"))
    b = int(raw_input("enter b:"))
    c = a + b
    print c
def sub():
    print "enter two numbers to subtract"
    a = int(raw_input("enter a:"))
    b = int(raw_input("enter b:"))
    c = a - b
    print c
def mult():
    print "enter two numbers to multiply"
    a = int(raw_input("enter a:"))
    b = int(raw_input("enter b:"))
    c = a * b
    print c
def div():
    print "enter two numbers to divide"
    a = int(raw_input("enter a:"))
    b = int(raw_input("enter b:"))
    c = a / b
    print c
if __name__ == '__main__':
    calculator()        
