# Harjoitus 1:
#
# Kirjoita funktio, joka korottaa numeron x potenssiin n.
# Funktio ottaa vastaan kaksi parametria, kantaluvun x
# ja exponentin n. Älä käytä operaattoria ** tai
# funktiota pow. Ota huomioon myös negatiiviset exponentit.
#
# a) Kirjoita funktiosta silmukkaan perustuva versio.
# b) Kirjoita funktiosta rekursiivinen versio.


# a)

def power(num, power): 
    a = 1 
    for i in range(power): 
        a *= num
    return a 

print(power(4,5)) # 1024
print(power(3,2)) # 9


# b)

# def power2(num, power):
#     if (power == 0 or power == 1):
#         return num
#     else:
#         return (num * power (num, power - 1))

# num = 4
# power = 5

# print(power2 (num, power))


# Harjoitus 2:
# Kirjoita funktio, joka tulostaa kaikki alkuluvut luvusta 2
# parametrina välitettävään lukuun num asti.
#
# "Alkuluku on lukua 1 suurempi luonnollinen luku, joka ei ole
# jaollinen muilla positiivisilla kokonaisluvuilla kuin yhdellä
# ja itsellään" (Wikipedia, https://fi.wikipedia.org/wiki/Alkuluku)

def primeNumber(num):

    for num in range(2, num + 1):
    # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num, end=' ')


primeNumber(20) # Output: 2 3 5 7 11 13 17 19

print()
    