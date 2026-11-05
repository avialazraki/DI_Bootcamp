import datetime


def draw_cake():
    # 1. Ask for birthdate
    birthdate_str = input("Enter your birthdate (DD/MM/YYYY): ")

    # 2. Parse date and calculate age
    try:
        birth_date = datetime.datetime.strptime(birthdate_str, "%d/%m/%Y").date()
        today = datetime.date.today()

        # Calculate accurate age
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        # 3. Get last number of age for candles
        candles = age % 10
        print(f"You are {age} years old! Let's add {candles} candles.")
    except ValueError:
        print("Invalid format. Please use DD/MM/YYYY.")
        return

    # 4. Generate the cake
    # Create the top candles based on the last digit of age
    candle_layer = "i" * candles

    # Ensuring the top is centered properly for the cake structure
    print(f"___({candle_layer})___")
    print(" |:H:a:p:p:y:|")
    print("__|___________|__")
    print("|^^^^^^^^^^^^^^^^^|")
    print("|:B:i:r:t:h:d:a:y:|")
    print("|                 |")
    print("~~~~~~~~~~~~~~~~~~~")


# Run the function
draw_cake()