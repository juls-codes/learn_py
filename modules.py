from datetime import datetime
import myUtilities as mu

#create a text file with dates
w = open('dates.txt','w')
w.write('07/16/1998\n04/07/2000\n04/14/2008\n')
w.close()

#read the text file and save the read data to a variable
r = open('dates.txt','r')
eachDate = r.readlines()
r.close()

#using the read data in a function
#first, create a text file for the output
o = open('dates_output.txt','w')

#then read each date, pass each data to func2(), and record the results into a new text file
for x in eachDate:
    x = x.replace('\n','') #takes out extra new line
    x = datetime.strptime(x, '%m/%d/%Y').date() #converts string from dates.txt into date objects
    ageResult = mu.age(x) #pass each date into age() and assign result to a variable
    oa = open('dates_output.txt','a') #open output file to append at each
    oa.write(f"The age based on {x} is {ageResult} years\n") #append to output file at each iteration
oa.close()
