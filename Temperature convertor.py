def temp_to_celsius(f):
    c = (f - 32) * (5/9)      
    return c

def temp_to_fahrenheit(c):
    f = c * (9/5) + 32
    return f

def main():
    t = float(input("Enter Temperature:"))

    temp = int(input("Choose 1 or 2 :\n1.Convert temperature to celsius\n2.Convert temperature to Fahrenheit\n"))

    if temp == 1:
        print(f'Temperature in celsius : %.2f Celsius'%(temp_to_celsius(t)))
    else:
        print(f'Temperature in Fahrenheit : %.2f Fahrenheit'%(temp_to_fahrenheit(t)))

main()
