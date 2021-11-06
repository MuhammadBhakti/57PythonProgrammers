import datetime

a = float(input("what is your age?"))
b = float(input("at what age would you like to retire?"))
c = b-a
now = datetime.datetime.now()
yr = int(now.year)
yr_retired = int(yr + c)
print("you have {} years left until you can retire. \n it's {} , so you retire in {}".format(c,yr,yr_retired))