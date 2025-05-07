def collatz_sequence(number):
    while True:
        if number != 1:
            if number % 2 == 0:
                number = number//2
                print(number)
            elif number % 2 == 1:
                number = 3 * number + 1
                print(number)
        else:
            break;

try:
    number = int(input("Enter the value:\n"))
    collatz_sequence(number)
except ValueError:
    print("Invalid input. Please enter a valid integer.") 
