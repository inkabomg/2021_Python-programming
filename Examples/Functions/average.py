# def keyword defines function
# Function's parameter(s) = input.

# Variable initialized outside the function, so it is a global variable.
isAverageRun = False

def main():
    # Python does not support overloading functions 
    # def sum(num1, num2):
    #     pass

    # def sum(num1, num2, num3):
    #     pass

    numbers = [1, 2, 3, 4, 5]
    # print("Variable before:", isAverageRun)
    avg = average(numbers, False)
    # print("Variable after:", isAverageRun)

    print("Average:", avg, sep="\t", end="---")

    numbers2 = [9, 8, 7, 6, 5]
    avg = average(numbers2, False)

    print("Average:", avg)

    # Python supports parameters' defaults. The default value of a parameter is
    # used if it is not assigned a value when the function is called. 
def average(numbers, printResult: bool = True):
    # global keyword used if you want to change the value of global variable's value
    global isAverageRun
    isAverageRun = True

    result = 0
    for number in numbers:
        if result == 0:
            index = 0
        else:
            index += 1
        result += number

    # Even though index has been specified within the loop, you
    # can also get to it outside the loop
    # print(index)

    average = result / len(numbers)

    if printResult:
        print(average)

    return average # Function's return value = output.

avg = average ([1, 2, 3, 4])

# Python does not support main function but with the code below we can 
# implement a similar functionality 
if __name__ == "__main__":
    main()

