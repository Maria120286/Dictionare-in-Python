# dictionare
'''
-este o colectie de tip date de cheie-valoare
-este mutabil
-chele sunt unice,valorile se pot repeta
-cheile pot fi doar de tip int,str si tuplu
'''
persoana = {
    'nume': 'Vali',
    'prenume': 'Dan',
    'varsta': 30

}
print(f'persoana={persoana}')
# adaugam un element in dictionar
persoana['initiala tatalui'] = 'P'
print(persoana)
# modificare unui element exitent
persoana['initiala tatalui'] = 'L'
print(persoana)
# stergem un element din dictionar
persoana.pop('initiala tatalui')
print(persoana)

# lungimea dictionarului
lungime_dict = len(persoana)
print(lungime_dict)
# combinare a doua dictionare
d1 = {
    'a': 1,
    'b': 2
}
d2 = {
    'c': 3,
    'd': 4
}
d1.update(d2)
print(d1)
print(d2)
# stergem toate elemetele din dictionar
d1.clear()
print(d1)
# seturi
# elemente unice nu pot avea valori duplicat,elementele pot fi de tip diferit
# este mutabila
# valorile setului fiind unice sunt considerate chei
data_curenta = {2023, 'noiembrie', 9, 19, 30, 'PM'}
print(data_curenta)
data_curenta.add(2022)
print(data_curenta)
data_curenta.add(2022)
print(data_curenta)
lista_diversa = (1, 2, 3)
data_curenta.add(lista_diversa)
print(data_curenta)
data_curenta.remove(2023)
print(data_curenta)
print(len(data_curenta))
# tuple
'''
-este de un tip inmutabil,nu se pot sterge,adauga  sau muta valori
-sunt valori ordonate indexabile si pot exista mai multe valori duplicate

'''
tuple_numere = (1, 2, 3)
x = list(tuple_numere)
lista_litere = ['a', 'b', 'c', 'd']
lista_litere = tuple(lista_litere)
print(lista_litere)
print(type(lista_litere))
print(type(x))
lista_litere = list(lista_litere)
print(lista_litere)
'''
1. Declară o listă note_muzicale în care să pui do re mi etc până la do
Afișeaz-o.
Inversează ordinea folosind slicing și suprascrie această listă.
Printează varianta actuală (inversată).
Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz, deoarece metoda face asta automat.
Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.

'''
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale[::-1])
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)
'''
2. De câte ori apare ‘do’?

'''
print(note_muzicale.count('do'))
# 3. Transforma lista de mai sus intr-o tupla. Incearca sa adaugi o nota noua.
note_muzicale.append(2023)
print(note_muzicale)
note_muzicale = tuple(note_muzicale)
print(note_muzicale)
note_muzicale=note_muzicale+('da')
print(note_muzicale)
'''
4. Declara un dictionar cu notele muzicale de mai sus. Cheia va fi nota, iar valoarea un numar care arata de cate ori
 apare nota in gama. Afiseaza-l.

'''
note_muzica = {
    'do': 2, 're': 1, 'mi': 1, 'fa': 1, 'sol': 1, 'la': 1, 'si': 1, 'do': 2
}
print(note_muzica)
