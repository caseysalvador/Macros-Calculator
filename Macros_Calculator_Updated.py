## Define Gender
# Male or Female
gender = str(input("Please enter your gender: "))
heightIN = float(input("Please enter your height: "))
weightLBs = float(input("Please enter your weight: "))

## Weight Conversion
# LBS to KG
def weightKG(weightLBs):
    kg = weightLBs*0.45
    return kg
# IN to CM
def heightCM(heightIN):
    cm = heightIN * 2.54
    return cm

## Basal Metabolic Rate (BMR)
def bmr(weight,height,age):
    bmr = (weight*10)+(height*6.25)-(age*5)
    return bmr

bmr = bmr(weight,height,age)

def genderBMR(gender):
    if gender == "male":
        malebmr = bmr + 5
    elif gender == "female":
        femalebmr = bmr - 161
    else:
        return "Please define your gender."

gBMR = genderBMR(gender)