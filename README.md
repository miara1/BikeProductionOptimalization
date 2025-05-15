# Optymalizacja produkcji rowerów – firma Rowex

## 📋 Opis problemu

Spółka Rowex produkuje rowery dla chłopców i dziewczynek w dwóch rozmiarach: 16 i 20 cali. Celem jest ustalenie:

- ilu pracowników należy przypisać do produkcji i składania rowerów,
- ile rowerów danego typu wyprodukować w tygodniu,

tak aby **zmaksymalizować zysk** przy zachowaniu ograniczeń czasowych i minimalnych wymagań produkcyjnych.

## 🧮 Dane wejściowe

Dla każdego typu roweru podano:

| Typ roweru              | Zysk [PLN] | Minuty produkcji | Minuty składania |
|-------------------------|------------|------------------|------------------|
| 16 cali – chłopięcy     | 70         | 25               | 16               |
| 20 cali – chłopięcy     | 100        | 28               | 18               |
| 16 cali – dziewczęcy    | 90         | 24               | 25               |
| 20 cali – dziewczęcy    | 120        | 29               | 32               |

Dodatkowe warunki:
- Minimum 150 rowerów chłopięcych i 150 dziewczęcych tygodniowo.
- 20 pracowników, każdy pracuje 8h dziennie przez 5 dni (łącznie 2400 minut tygodniowo).
- Pracownicy mogą być przypisani tylko do produkcji lub składania.

## 💡 Rozwiązanie

Problem został zamodelowany jako **programowanie całkowitoliczbowe** i rozwiązany za pomocą biblioteki `PuLP`. Zmiennymi decyzyjnymi są:

- Liczba rowerów każdego typu do wyprodukowania (`ch16`, `ch20`, `dz16`, `dz20`)
- Liczba pracowników przypisanych do produkcji (`p`) i składania (`s`)

Funkcja celu:
```
Maximize: 70·ch16 + 100·ch20 + 90·dz16 + 120·dz20
```

Ograniczenia:
- `ch16 + ch20 ≥ 150` – chłopięce
- `dz16 + dz20 ≥ 150` – dziewczęce
- `p + s = 20` – łącznie 20 pracowników
- Czas produkcji nie przekracza `2400·p` minut
- Czas składania nie przekracza `2400·s` minut

## 🚀 Uruchamianie

Program wymaga biblioteki `PuLP`. Możesz ją zainstalować za pomocą:

```bash
pip install pulp
```

Następnie uruchom program:

```bash
python rowex.py
```

## 📈 Wynik

Program wypisuje:

- Status rozwiązania (np. Optimal)
- Maksymalny możliwy zysk
- Liczbę rowerów każdego typu do wyprodukowania
- Liczbę pracowników przypisanych do produkcji i składania

## 🛠️ Autor

Maciej Mierkiewicz
