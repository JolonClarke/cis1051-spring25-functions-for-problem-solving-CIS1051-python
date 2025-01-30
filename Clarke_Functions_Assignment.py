#Part one:
weight = int(input("Insert weight in kilograms: "))
height = int(input("Insert height in centimeters: "))
age = int(input("Insert age in years: "))


def bmr_m():
    return (13.7516 * weight) + (5.0033 * height) - (6.755 * age) + 66.473

def bmr_f():
    return (9.5634 * weight) + (1.8496 * height) - (4.6756 * age) + 655.0955

bmr_male = bmr_m()
bmr_female = bmr_f()

#-------------------------------------------------------------------------------------
bar = 214

def num_of_bars():
    print("Number of chocolate bars for a man: " + str(bmr_male / bar))
    print("Number of chocolate bars for a woman: " + str(bmr_female / bar))

num_of_bars()



#-----------------------------------------------------------------
#Part 2

temp_C = int(input("Insert temperature in Celsius: "))
temp_F = temp_C * 9/5 + 32
print(str(temp_F) + " degrees Fahrenheit.")

#-------------------------------------------------------------------
#Part 3

secs1 = int(input("Insert number of seconds: "))
hours = int(secs1 / 3600)
secs2 = abs(hours * 3600 - secs1)
mins = int(secs2 / 60)
secs3 = abs(mins * 60 - secs2)

if hours == 1:
    if mins == 1:
        if secs3 == 1:
            print("Time: " + str(hours) + " hour, " + str(mins) + " minute, and " + str(secs3) + " second." )
        else:
            print("Time: " + str(hours) + " hour, " + str(mins) + " minute, and " + str(secs3) + " seconds." )
    elif secs3 == 1:
        print("Time: " + str(hours) + " hour, " + str(mins) + " minutes, and " + str(secs3) + " second." )
    else:
        print("Time: " + str(hours) + " hour, " + str(mins) + " minutes, and " + str(secs3) + " seconds." )
elif mins == 1:
        if secs3 == 1:
            print("Time: " + str(hours) + " hours, " + str(mins) + " minute, and " + str(secs3) + " second." )
        else:
            print("Time: " + str(hours) + " hours, " + str(mins) + " minute, and " + str(secs3) + " seconds." )
elif secs3 == 1:
    print("Time: " + str(hours) + " hours, " + str(mins) + " minutes, and " + str(secs3) + " second." )
else:
    print("Time: " + str(hours) + " hours, " + str(mins) + " minutes, and " + str(secs3) + " seconds." )
