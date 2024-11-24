import addition
import subtration
import multiplication
import division



def math_calculation():
    math_cal=input("please enter your needs....")
    if math_cal.lower()=='addition':
        addition.add_calculation()
    elif math_cal.lower()=='subtraction':
        subtration.sub_calculation()
    elif math_cal.lower()=='multiplication':
        multiplication.mul_calculation()
    elif math_cal.lower()=='division':
        division.devision_calcultion()
    else :
            print('please provide me correct input')
            return math_calculation()




def end_continue():
    # here user will tell whether to continue or not
    end_cont=input("Whether you want to continue or not /n Yes or No please")
    if end_cont.lower()=='yes':
        math_calculation()
        try:
            
    else:
        print("Thank you for yourvaluable time")
        exit()