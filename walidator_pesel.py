import datetime

print("               _ _     _       _               ____  _____ ____  _____ _     ")
print("__      ____ _| (_) __| | __ _| |_ ___  _ __  |  _ \| ____/ ___|| ____| |    ")
print("\ \ /\ / / _` | | |/ _` |/ _` | __/ _ \| '__| | |_) |  _| \___ \|  _| | |    ")
print(" \ V  V / (_| | | | (_| | (_| | || (_) | |    |  __/| |___ ___) | |___| |___ ")
print("  \_/\_/ \__,_|_|_|\__,_|\__,_|\__\___/|_|    |_|   |_____|____/|_____|_____|")
# Generated on http://www.network-science.de/ascii/ (font: standard)

print('\nPodaj numer PESEL który chcesz sprawdzić:\n')
pesel = input()

# Sprwdzenie czy wprowadzono wyłącznie cyfry
if pesel.isdigit():
    pesel = list(map(int, str(pesel)))
else:
    print('Nieprawidłowy numer PESEL (Zawiera znaki inne niż cyfry)')
    quit()

# Sprawdzenie czy wprowadzono poprawną ilość znaków
if len(pesel) != 11:
    print('Nieprawidłowy numer PESEL (Nieprawidłowa długość)')
    quit()

# Sprawdzenie czy wprowadzona w PESELu data jest poprawna
if pesel[2] < 2:
    year = 1900 + pesel[0]*10 + pesel[1]
    month = pesel[2]*10 + pesel[3]
    day = pesel[4]*10 + pesel[5]
    try:
        datetime.datetime(year, month, day)
    except ValueError:
        print('Nieprawidłowy numer PESEL (Zła data)')
        quit()

elif pesel[2] == 2 or pesel[2] == 3:
    year = 2000 + pesel[0]*10 + pesel[1]
    month = (pesel[2]-2) * 10 + pesel[3]
    day = pesel[4] * 10 + pesel[5]
    try:
        datetime.datetime(year, month, day)
    except ValueError:
        print('Nieprawidłowy numer PESEL (Zła data)')
        quit()

# Sprawdzenie sumy kontrolnej
checksum = (9*pesel[0]+7*pesel[1]+3*pesel[2]+pesel[3]+9*pesel[4]+7*pesel[5]+3*pesel[6]+pesel[7]+9*pesel[8]
                  + 7*pesel[9]) % 10
if checksum == pesel[10]:
    print('Numer PESEL poprawny')
else:
    print('Nieprawidłowy numer PESEL (Nieprawidłowa suma kontrolna)')
