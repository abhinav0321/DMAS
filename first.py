print("Enter your name:- \n")
in1 = input()
def first():

    print("Hello ", in1, " what do you want to do? Press \n+ addition\n- subtraction"
                         "\n* multiplication\n/ division")
    in2=input()
    in3=int(input("Enter first no. \n"))
    in4=int(input("Enter second no. \n"))
    if in2=='+' :
        print("addition is ",in3+in4)
    elif in2=='-' :
        print("subtraction is ",in3-in4)
    elif in2=='*' :
        print("multiplication is ",in3*in4)
    elif in2=='/':
        print("division is ",in3/in4)

first()
def second():
    in5=input("Do you want to repeat ? [y/n]")
    if in5=='y':
        first()
    elif in5=='n':
        exit()
    else:
        second()
second()



