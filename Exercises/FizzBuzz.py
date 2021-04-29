'''
Seuraavaa tehtävää on käytetty yleisesti työhaastatteluissa ennakkotehtävänä:
Kirjoita funktio, joka ottaa parametrinaan numeron ja palauttaa joko
"Fizz", "Buzz" tai "FizzBuzz" seuraavien ehtojen perusteella: 
- Jos numero on jaollinen kolmella, funktio palauttaa "Fizz"
- Jos numero on jaollinen viidellä, funktio palauttaa "Buzz"
- Jos numero on jaollinen sekä kolmella että viidellä, funktio palauttaa "FizzBuzz"
- Jos numero ei ole jaollinen kolmella eikä viidellä, funktio palauttaa numeron itsensä string-muodossa.
Kiinnitä huomiota ratkaisun selkeyteen ja ylläpidettävyyteen.
'''

def fizz_buzz(number):
    try:
        number = int(number)
    except ValueError:
        print("Parameter is not an integer")
        return

    output = ""
    if number % 3 == 0:
        output += "Fizz"
    if number % 5 == 0:
        output += "Buzz"
    if number % 7 == 0: # New, added to the original FizzBuzz
        output += "Bazz"

    if output == "":
        output = str(number)

    return output

def main():
    for i in range(1,120):
        print(fizz_buzz(i))

if __name__ == "__main__":
    main()



# def FizzBuzz(n):
#     if n % 3 == 0 and n % 5 == 0:
#         return "Fizzbuzz"
#     elif n % 3 == 0:
#         return "Fizz"
#     elif n % 5 == 0:
#         return "Buzz"
#     else:
#         return str(n)

# print(FizzBuzz(5))
# print(FizzBuzz(9))
# print(FizzBuzz(17))
# print(FizzBuzz(15))




# def FizBuzz2(number):
#     # The range(int, int) is used to declare the lower limit and upper limit of the iteration
#     # of the numbers. + 1 so that it runs to the number I have set for it (21, and not till 20)
#     for i in range(1, number + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)

# FizBuzz2(21)