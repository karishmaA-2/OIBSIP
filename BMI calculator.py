#Taking inputs from the user
#Height in inches and weight in kilograms

height=float(input("Enter height in inches:"))
weight=float(input("Enter weight in kilograms:"))

#Converting weight in metres
height=height*0.0254

#condition for bmi
def bmi(height,weight):
    BMI=weight/(height**2)
    if BMI < 16:
        return "underweight",BMI
    elif BMI >= 18.5 and BMI<25:
        return "normal weight",BMI
    elif BMI>=25 and BMI <=30:
        return "Overweight",BMI
    elif BMI>30:
        return "Obesity",BMI

quote,BMI=bmi(height,weight)
print("BMI result {} and category is {}".format(BMI,quote))

