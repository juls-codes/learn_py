
import datetime as dt

def getName():
    name = input("What is your name? ")
    return name

def func1():
    bd = input("When is your birthday? ")
    try:
        dateobj = dt.datetime.strptime(bd, "%m/%d/%Y")
    except ValueError as e:
        print("There is a ValueError. Please format as MM/DD/YYY") 
    except Exception as e:
        print(e)
    return dateobj

def func2(dateobj): 
    today = dt.datetime.today()
    age = today.year - dateobj.year - ((today.month, today.day) < (dateobj.month, dateobj.day))
    return age


    
