'''
Macros Calculator

MIT License

Copyright (c) 2018 Casey Chad Salvador

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. '''

## Variable
weight = float(input("Please enter your current weight: "))


## Create Protein Function
def protein(weight):
    fitnessLvl0 = .5
    fitnessLvl1 = .75
    fitnessLvl2 = 1
    fitnessLvl3 = 1.25
    fitnessLvl = int(input("Please enter your fitness level (i.e. 1 = New to Training, 2 = In Shape, 3 = Competing, 4 = No Training): "))
    if fitnessLvl == 4:
        pro = fitnessLvl0 * weight
        return pro
    elif fitnessLvl == 1:
        pro = fitnessLvl1 * weight
        return pro
    elif fitnessLvl == 2:
        pro = fitnessLvl2 * weight
        return pro
    elif  fitnessLvl == 3:
        pro = fitnessLvl3 * weight
        return pro

## Create Fat Function
def fat(weight):
    fat1 = .3
    fat2 = .35
    fat3 = .4
    fatLvl = int(input("Please enter your fat level (i.e. 1 = Love Carbs, 2 = Mix, 3 = Love Fat (nuts, peanut butter, etc): "))
    if fatLvl == 1:
        fats = fat1 * weight
        return fats
    elif fatLvl == 2:
        fats = fat2 * weight
        return fats
    elif fatLvl == 3:
        fats = fat3 * weight
        return fats

## Create Calorie Function
def calories(weight):
    cal1 = 14
    cal2 = 15
    cal3 = 16
    calLvl = int(input("Please enter your activity level (i.e. 1 = Less Movement, 2 = Moderately Moving, 3 = Actively Moving): "))
    if calLvl == 1:
        cal = cal1 * weight
        return cal
    elif calLvl == 2:
        cal = cal2 * weight
        return cal
    elif calLvl == 3:
        cal = cal3 * weight
        return cal

cals = calories(weight)

protein = round(protein(weight))

fat = round(fat(weight))

## Create New Physique
def physique(cals):
    shred = 500
    maintain = 0
    gain = 500
    phyLvl = input(str("Please enter your physique goal (i.e. shred, maintain, gain): "))
    if phyLvl == "shred":
        phy = cals - shred
        return phy
    elif phyLvl == "maintain":
        phy = cals - maintain
        return phy
    elif phyLvl == "gain":
        phy = cals + gain
        return phy

phyCal= physique(cals)

## Create Caloric Intake Function
# 4 x 9 x 4 Rule Applies Here
def cal(phyCal):
    calPro = protein * 4
    calFat = fat * 9
    sumProFat = calPro + calFat
    carbCal = phyCal - sumProFat
    return carbCal

carbCal = cal(phyCal)

## Create Carbs Function
def carbs(carbCal):
    carb = carbCal / 4
    return carb

carb = round(carbs(carbCal))

print("")

## Results
print("Macros")
print("Protein: " + str(protein) + "g")
print("Fat: " + str(fat) + "g")
print("Carbohydrate: " + str(carb) + "g")
print("Total Calories per day: " + str(round(phyCal)) + "cal")