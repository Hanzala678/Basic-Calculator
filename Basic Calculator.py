#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True:
    
    def add(x,y):
        z = x + y
        print(x,"+",y,"=",z)
    def subtract(x,y):
        z = x - y
        print(x,"-",y,"=",z)
    def multiply(x,y):
        z = x * y
        print(x,"x",y,"=",z)
    def divide(x,y):
        z = x / y
        print(x,"/",y,"=",z)


    def calculator(x,y,s):
        if s == '+':
            add(x,y)
        elif s == '-':
            subtract(x,y)
        elif s == '*':
            multiply(x,y)
        elif s == '/':
            divide(x,y)
        else:
            print("Invalid Syntax")
    
    flag_num = False
    flag_operator = False
    valid_operator = ['+','-','*','/']
    
    while not flag_num or not flag_operator:
        try:
            if flag_num == False:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                flag_num = True
            if flag_operator == False:
                operator = input("Enter the operator: ")
                if operator not in valid_operator:
                    raise Exception
                flag_operator = True
            break
        except ValueError:
            print("Enter values in integer or float")
            print("")
        except:
            print("Enter the correct operator (+,,*,/)")
            print("")
    
    calculator(num1, num2, operator)
    print()

    exit = input("Enter n/N to exit, any other key to continue: ")
    print()
    if exit == 'n' or exit == 'N':
        break


# In[ ]:




