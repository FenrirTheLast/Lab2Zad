# Zad.1
zdanie = input("Podaj swoje zdanie użytkowniku: ")
ilosc_slow = len(zdanie.split())
print("Ilość słów w Twoim zdaniu wynosi:", ilosc_slow)

# Zad.2
a = int(input("Podaj pierwszą liczbę całkowitą (a): "))
b = int(input("Podaj drugą liczbę całkowitą (b): "))
c = int(input("Podaj trzecią liczbę całkowitą (c): "))

wynik = a ** b + c

print("Wynik obliczenia a^b + c =", wynik)

# Zad.3
def is_palindrome(word):

    word = word.replace(" ", "").lower()

    return word == word[::-1]

user_input = input("Wpisz napis: ")

if is_palindrome(user_input):
    print("Podany napis jest palindromem.")
else:
    print("Podany napis nie jest palindromem.")
#
def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

with open("prime_check.txt", "w") as file:
    number = int(input("Podaj liczbę do sprawdzenia czy jest pierwszą: "))

    if is_prime(number):
        result = f"Liczba {number} jest liczbą pierwszą.\n"
        file.write(result)
        print(result)
    else:
        result = f"Liczba {number} nie jest liczbą pierwszą.\n"
        file.write(result)
        print(result)

print("Wynik został zapisany do pliku 'prime_check.txt'.")

# Zad.5
def find_perfect_numbers(limit):
    perfect_numbers = []
    for num in range(2, limit + 1):
        sum_of_divisors = sum([divisor for divisor in range(1, num) if num % divisor == 0])
        if sum_of_divisors == num:
            perfect_numbers.append(num)
    return perfect_numbers

perfect_numbers = find_perfect_numbers(1000)
number_of_perfect_numbers = len(perfect_numbers)

print(f"Ilość liczb doskonałych do liczby 1000: {number_of_perfect_numbers}")
print("Liczby doskonałe:")
print(perfect_numbers)


# Zad.6
with open("squared_numbers.txt", "w") as file:
    file.write("Lista po podniesieniu do kwadratu:\n")

    lista_liczb = [1, 2.5, 3, 4.7, 5, 6.2]

    for i, liczba in enumerate(lista_liczb):
        lista_liczb[i] = liczba ** 2
        file.write(f"{lista_liczb[i]}\n")
print("Lista po podniesieniu do kwadratu:")
print(lista_liczb)
print("Podniesione do kwadratu liczby zostały zapisane do pliku 'squared_numbers.txt'.")

# Zad.7
parzyste_liczby = []

i = 0
while i < 10:
    liczba = int(input("Podaj liczbę: "))
    if liczba % 2 == 0:
        parzyste_liczby.append(liczba)
    i += 1

print("Parzyste liczby:", parzyste_liczby)

print("Parzyste liczby zostały zapisane do pliku 'parzyste_liczby.txt'.")

# Zad.8
lista_elementow = [1, 'a', 2, 'b', 3, 'a', 1, 'c', 'b']

with open("lista_elementow.txt", "w") as file:
    file.write("Lista elementów:\n")
    for element in lista_elementow:
        file.write(str(element) + "\n")

slownik = {}

for element in lista_elementow:
    if element in slownik:
        slownik[element] += 1
    else:
        slownik[element] = 1

klucze_do_usuniecia = [klucz for klucz in slownik if not isinstance(klucz, (int, float))]
for klucz in klucze_do_usuniecia:
    del slownik[klucz]

with open("slownik_po_usunieciu.txt", "w") as file:
    file.write("Słownik po usunięciu elementów nie będących liczbami:\n")
    for key, value in slownik.items():
        file.write(f"{key}: {value}\n")

print("Słownik po usunięciu elementów nie będących liczbami:")
print(slownik)

print("Listę elementów oraz ostateczny słownik zostały zapisane do plików.")