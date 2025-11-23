print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to python")

def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("weight = " + str(weight))
    
    bmi = weight/(height*height)
    print("BMI = " + str(bmi))
    if bmi < 18.5:
        print("under weight")
    elif bmi > 25.0:
        print("Over weight")
    else:
        print("Normal Weight")
    
calculate_bmi(weight = 57, height = 1.73)




