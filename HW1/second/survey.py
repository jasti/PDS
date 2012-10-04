import csv

educationModifier = {"1" :-3,
		     "2" :-1,
                     "3" :0,
                     "4" :1,
                     "5" :3,
                     "6" :4}

occupationModifier = {"1" :2.5,
                      "2" :.6,
                      "3" :0,
                      "4" :.2,
                      "5" :-.5,
                      "6" :-1.5,
                      "7" :.3,
                      "8" :.8,
                      "9" : -2.5}

nominalModifier = 4
actualIncomeLevel = 0
occupationLevel = 0
runningSalaryFirst = 0
runningSalarySecond = 0
counter =0
reader = csv.reader(open("marketing.data","rb"),delimiter=' ',quoting=csv.QUOTE_NONE)
for entry in reader :
    educationLevel = entry[4]
    actualIncomeLevel = entry[0]
    occupationLevel = entry[5]
    individualEducationModifier = educationModifier.get(educationLevel)
    individualOccupationModifier = occupationModifier.get(occupationLevel)
    predictedSalaryFirst = nominalModifier +individualEducationModifier
    predictedSalarySecond = nominalModifier + individualEducationModifier+individualOccupationModifier
    differenceFirst = predictedSalaryFirst - int(actualIncomeLevel)
    differenceSecond = predictedSalarySecond - int(actualIncomeLevel)
    runningSalaryFirst = runningSalaryFirst + differenceFirst
    runningSalarySecond = runningSalarySecond + differenceSecond
    counter = counter + 1


print "Total Entries :", counter
print "Total differenceFirst : ", runningSalaryFirst
print "Total differenceSecond : ", runningSalarySecond
print "Average differenceFirst per user :", float(runningSalaryFirst)/float(counter)
print "Average differenceSecond per user :", float(runningSalarySecond)/float(counter)
 
