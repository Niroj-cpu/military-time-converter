x = int (input ("what time is it?"))
x = x%24
if x>12:
    print("Do you mean " + str(x%12) + " o'clock PM?")
elif x<12:
    print("Do you mean " + str(x) + " o'clock AM?")
elif x==12:
    print("Do you mean 12 noon?")
else:
    print("Do you mean midnight?")
