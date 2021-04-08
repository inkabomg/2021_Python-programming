class ValueOutOfRangeError(ValueError):
    pass

def main ():
    exit = False

    while not exit:
        try:
            user_input = int(input("Input a number between [0 and 10] > "))

            if user_input < 0 or user_input > 10:
                raise ValueOutOfRangeError()

            exit = True
        except ValueOutOfRangeError:
            print("Value is not legal. Try again.")
        except ValueError:
            print("Invalid value.")
        except:
            print("Unknown error.")

if __name__ == "__main__":
    main()