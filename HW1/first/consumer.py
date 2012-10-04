from sys import argv
import matplotlib.pyplot as plt
import numpy as np 
import csv
import pylab as p
from pylab import *
# Initilize a static class with answers and corresponding scores
class Data:
    
    unix = {'I dont even understand the question': 0 ,
	    'I have no experience working in a terminal':1 ,
            'I have issued a few commands in a terminal based on given instructions':2,
            'I have written simple terminal commands or done some system work on the terminal':3, 
            'I have written complex commands done or have done deep system work':4 
           };

    database ={'I have never directly accessed a database': 0 ,
              'I have issued simple queries to a relational database based on given instructions':1 ,
              'I can write simple queries and issue them to a database':2,
              'I can write very complex queries when needed':3, 
              'I am a database hacker':4 
 	      };

    programming = {'I have never programmed before.': 0 ,
                   'I have written simple programs, based on instructions or a tutorial':1 , 
                   'I can write simple programs to accomplish tasks I encounter':2,
                   'I can write complex programs, am familiar with programming design patterns, software testing, system design, and algorithms.':3, 
                   'I am a hacker or have  senior-level programming experience':4 
		  }; 

print("Reading the survey file\n");

script, filename= argv

unixScore = 0;
databaseScore = 0;
programmingScore = 0;
student = 0;
answers = {}

def plotBarChart(data, chartName) :
    error = [0] * len(data)

    xlocations = np.array(range(len(data)))+0.5
    width = 0.5
    bar(xlocations, data, yerr=error, width=width)
    #yticks(range(0, 8))
    #xticks(xlocations+ width/2, labels)
    xlim(0, xlocations[-1]+width*2)
    title(chartName)
    gca().get_xaxis().tick_bottom()
    gca().get_yaxis().tick_left()
    p.show()


def convertDictToNumArr(answers) :
    myarray = np.empty((len(answers.keys()), 3), dtype=int) 
    for student in range(len(answers.keys())): 
        for question in range(3): 
            myarray[student, question] = answers[student+1][question]  

    return myarray 

def import_text(filename, separator):
    for line in csv.reader(open(filename), delimiter=separator, 
                           skipinitialspace=True):
        if line:
            yield line

# Reading the input file

for data in import_text(filename, '\t'):
    student = student + 1
    entry = data[0]    
    localUnixScore = Data.unix[entry.strip()]
    unixScore = unixScore+localUnixScore

    entry = data[1]
    localDatabaseScore = Data.database[entry.strip()]
    databaseScore = databaseScore + localDatabaseScore
   

    entry = data[2]
    localProgrammingScore = Data.programming[entry.strip()]
    programmingScore = programmingScore + localProgrammingScore 
    
    studentScore = [localUnixScore, localDatabaseScore, localProgrammingScore]
    answers[student]=studentScore

print("Cummulative scores :");

print("unixScore : %d" %unixScore)
print("databaseScore : %d "%databaseScore)
print("programmingScore : %d "%programmingScore)


# Converting the dictionary with the student and his scores to a numPyArray

numPyArray = convertDictToNumArr(answers)
studentsArray = np.arange(39)

# Get sorted unix scores

unixScores = sorted(numPyArray[:,0])

# Get sorted database scores

databaseScores = sorted(numPyArray[:,1])

# Get sorted programming scores

programmingScores = sorted(numPyArray[:,2])

#Display individual graphs

plt.plot(unixScores)
plt.ylabel('unixScores')
plt.xlabel('Students')
plt.show()

plt.plot(databaseScores)
plt.ylabel('databaseScores')
plt.xlabel('Students')
plt.show()

plt.plot(programmingScores)
plt.ylabel('programmingScores')
plt.xlabel('Students')
plt.show()

#Display the combined graph

plt.plot(studentsArray, unixScores, 'r',studentsArray, databaseScores,'b', studentsArray, programmingScores,'g')
plt.legend( ('databaseScores', 'programmingScores', 'unixScores'), loc='upper left')
plt.show()

# Bar plot

plotBarChart(unixScores, "Unix Scores")
plotBarChart(databaseScores, "Database Scores")
plotBarChart(programmingScores, "Programming Scores")
