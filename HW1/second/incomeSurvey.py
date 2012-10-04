from sys import argv
import csv
def import_text(filename, separator):
    for line in csv.reader(open(filename), delimiter=separator,
                           skipinitialspace=True):
        if line:
            yield line

incomeDistribution = { '1':5000,
 		       '2':12500,
 		       '3':17500,
 		       '4':22500,
                       '5':27500,
                       '6':35000,
                       '7':45000,
                       '8':62500,
		       '9':87500}

educationMultiplier = {'1': 11250,
		       '2': 14850,
		       '3': 22500,
                       '4': 33750,
                       '5': 56250,
                       '6': 67500}
#print("Reading the survey file\n");

script, filename= argv

variable = 0
education = {}

for data in import_text(filename, ' '):
    variable = variable+ 1
    educationEntry = data[4]
    
    if educationEntry in education:
        education[educationEntry] += 1
    else:
        education[educationEntry] = 1 
#print "Printing the education composition"
#print education

variable1= 0
totalGivenSalary = 0
totalPredictedSalary = 0
totalAvgGivenSalary = 0
dic_prediction = {}
print " Education Multiplier ", educationMultiplier
# Inserting a education modifier income
for data in import_text(filename, ' '):
    variable1 = variable1+ 1
    educationEntry = data[4]
    givenSalaryCode = data[1]
    occupation =data[6]
    predictedSalary = educationMultiplier[educationEntry]
    totalPredictedSalary = totalPredictedSalary+ predictedSalary
    avgGivenSalary = incomeDistribution[givenSalaryCode]
    totalAvgGivenSalary = totalAvgGivenSalary+avgGivenSalary
    dic_prediction[variable1] = [educationEntry, givenSalaryCode,occupation,avgGivenSalary,predictedSalary]
    
print dic_prediction[1]
print dic_prediction[200]

print totalPredictedSalary
print totalAvgGivenSalary
