# Hooke’s law is an equation for how much force is required to compress or stretch a spring by a 
# certain amount: 
#HookesLaw function F = K*X
# A higher spring constant means that the spring is more difficult to  compress or stretch. Springs 
# can be combined in series or in parallel as shown in the diagram below. 
# Develop a Python function, Springs, that has the following input arguments: spring constants, the 
# total force, and the configuration (series or parallel). The function should check to make sure that 
# K1, K2, and Ftotal are positive numbers. For invalid inputs, the function should output an error 
# message to the user. For valid inputs, the program should return Keq, F1, F2, x1, x2, and xtotal. 
Configuration = input("Enter the configuration (series or parallel): ")
K1= input("Enter the spring constant for spring 1: ")
K2= input("Enter the spring constant for spring 2: ")
Ftotal= input("Enter the total force: ")
def Springs(K1, K2, Ftotal,Configuration):
    #if K1 > 0 and K2 > 0 and Ftotal > 0:
    if Configuration == "series":
            Keq = K1+K2
            F1 = Ftotal
            F2 = Ftotal
            X1 = F1/K1
            X2 = F2/K2
            Xtotal = X1+X2
            print(Keq,F1, F2, X1,X2, Xtotal)
    elif Configuration == "parallel":
            Keq = (K1*K2)/(K1+K2)
            F1 = (K2/K1)*Ftotal
            F2 = (K1/K2)*Ftotal
            X1 = F1/K1
            X2 = F2/K2
            Xtotal = X1+X2
            print(Keq,F1, F2, X1,X2, Xtotal)
    else:
            print("Invalid configuration")
    return Keq, F1, F2, X1, X2, Xtotal
print(Keq)  