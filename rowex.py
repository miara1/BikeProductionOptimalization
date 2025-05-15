from pulp import *

# definiujemy problem programowania liniowego z maksymalizacją
problem = LpProblem("Rowex", LpMaximize)

# definiujemy zmienne decyzyjne
# zmienne przyjmują wartości całkowite
# co definiuje problem programowania całkowitoliczbowego
ch16 = LpVariable("ch16", 0, cat="Integer") # 16 cali chlopiecy
ch20 = LpVariable("ch20", 0, cat="Integer") # 20 cali chlopiecy
dz16 = LpVariable("dz16", 0, cat="Integer") # 16 cali dziewczecy
dz20 = LpVariable("dz20", 0, cat="Integer") # 20 cali dziewczecy

p = LpVariable("p", 0, 20, cat="Integer") # ilosc pracownikow produkcji
s = LpVariable("s", 0, 20, cat="Integer") # ilosc pracownikow skladania

# Funkcja celu - maksymalizacja zysku
problem += 70 * ch16 + 100 * ch20 + 90 * dz16 + 120 * dz20

# Ograniczenia
problem += ch16 + ch20 >= 150 # conajmniej 150 rowerow chlopiecych
problem += dz16 + dz20 >= 150 # conajmniej 150 rowerow dziewczecych

problem += p + s == 20 # 20 pracownikow łącznie

# calkowity czas produkcji rowerow musi byc mniejszy 
# niz 1200 minut na kazdego pracownika (5 dni po 8 godzin)
problem += 25 * ch16 + 28 * ch20 + 24 * dz16 + 29 * dz20 <= 1200 * p

# calkowity czas skladania rowerow musi byc mniejszy 
# niz 1200 minut na kazdego pracownika (5 dni po 8 godzin)
problem += 16 * ch16 + 18 * ch20 + 25 * dz16 + 32 * dz20 <= 1200 * s

# rozwiazanie problemu
problem.solve()

# wyswietlenie wynikow
print("Status:", LpStatus[problem.status])
print("Zysk maksymalny:", value(problem.objective))
print("ch16:", ch16.value())
print("ch20:", ch20.value())
print("dz16:", dz16.value())
print("dz20:", dz20.value())
print("p:", p.value())
print("s:", s.value())

