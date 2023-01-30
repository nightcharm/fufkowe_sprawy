


jez=''' 
                  .|||||||||.    < fuf fuf >
           \     |||||||||||||
            \  /. `|||||||||||
             o__,_||||||||||'''

def wypisz_linijke(words):   #definicja funkcji to jest #Aby nasze funkcje mogły przyjmować wartości, wystarczy
    # zdefiniować zmienne wewnątrz nawiasów w definicji funkcji (po prostu określamy ich nazwy). Takie zmienne
    # nazywane są parametrami.
    size = max(len(word) for word in words)
    print("_" * (size + 4))
    for i in words:
        print("<" + " " + i + " " + ">")
    print("_" * (size + 4))



def zawijanie(string_name):
    print("_" * (dlugosc_linii + 4)+'\n<', end=' ')  #dlugosc_linii to długość kreseczek (no plus dwa)
    # print()
    numer_zmiennej = 0
    for element in string_name:
        print(element, end="")  #dzieki temu zabiegowi pojedyncze stringi cvzyli znaki drukuja sie kolo siebie
        numer_zmiennej = numer_zmiennej + 1  #dzieki temu tez
        ilosc_linii = numer_zmiennej // dlugosc_linii
        reszta = numer_zmiennej % dlugosc_linii

        if reszta == 0:
            #print('>', end= '')

            if numer_zmiennej == len(string_name):
                print(' >', end='')
            else:
                print(' >\n< ', end="")

    if reszta ==0:
        print('\n'+"_" * (dlugosc_linii + 4))
    if reszta >0:
        print(' >\n' +"_" * (dlugosc_linii + 4))

    # for dlugosc_linii in x:
    #     print('<' + '>')

dlugosc_linii = 8

print('Fuf!')
string_name = input('Co powinienem przekazać światu?\n')

# string_name = "jestem fufczastym fufkiem"


if len(string_name) <= dlugosc_linii:
    wypisz_linijke([string_name])
else:   #if len(string_name) > dlugosc_linii to to samo
    zawijanie(string_name)
print(jez)







