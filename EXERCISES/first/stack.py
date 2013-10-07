if __name__ == '__main__':
    stack = []
    choice=0
    while(choice!=3):
        print "1) Add value "
        print "2) Remove vale"
        print "3) exit"
        choice = raw_input("Enter ur choice")
        if choice == "1":
            s=raw_input("add new values to stack:")
            stack.append(s)
            print "stack after push is:",stack    
 
        elif choice == "2":
            if not stack:
                print "stack is empty,please add some values"
            else:    
                print "remove the value"
                top=stack.pop()
                print stack
            
        
        elif choice =="3":
            exit(0)
        else:
            print "wrong choice,please enter the right choice"

