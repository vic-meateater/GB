numb = int(input("~#: ").replace('.', ''))

die_summe = 0

while numb > 0:
    die_summe += numb % 10
    numb //= 10

print(die_summe)
