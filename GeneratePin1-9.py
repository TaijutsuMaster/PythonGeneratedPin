def my_func():
    print("""
Generate 1-9 Digit Pin
Not for Hacking Purposes
But Ethical Instead""")
    digit_pin = input("Input Digit Pin: ")
    if not digit_pin.isdigit():
        print("Invalid, Input a Number")
        my_func()
    elif digit_pin == "0":
        print("Invalid, Select from 1 to 9")
        my_func()
    else:
        count_limit = 9
        if int(digit_pin) <= count_limit:
            digit_range = int("9" * int(digit_pin))
            for n in range(digit_range + 1):
                number = str(n).zfill(int(digit_pin))
                print(number)
            back = str.lower(input("""Do you want generate another Pin? Y/N:  """))
            if back == "y":
                my_func()
            else:
                print("PIN generator terminated")
                quit()
        else:
            print("Invalid, Choose a Number from 1-9")
            my_func()
my_func()
