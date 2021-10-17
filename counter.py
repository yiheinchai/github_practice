user_input_valid = False

while user_input_valid == False:
    counter = int(input("Enter the number to start: "))
    if counter < 5:
        user_input_valid = True

while counter <= 5:
    print("hello", counter)
    counter += 1
