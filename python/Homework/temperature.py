def farenheit(celcius):
    return (celcius * 9/5) + 32
def celcius(farenheit):
    return (farenheit - 32) * 5/9

print(":::THIS IS A TEMPERATURE CHECK PROGRAM:::")
choice = int(input("1.Celcius to Farenheit\n2.Farenheit to Celcius\nEnter your choice: "))
temperature = float(input("Enter Temperature: "))
if  choice == 1:
    print("Celcius: " + str(temperature) + " Farenheit: " + str(celcius(temperature)))
elif choice == 2:
    print("Farenheit: " + str(temperature) + " Celcius: " + str(farenheit(temperature)))