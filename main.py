""""
Moeda - País - Valor em relação ao Lyodnik
Льодник (₴) - Aurória - 1.00 - Base
Marco Francês (ℳ) - Marselha - 0.75
Kremówka (Kℳ) - Polônia - 0.58
Schwarzler (Ś) - Áustria - 0.43
Korona-Víz (₭) - Hungria - 0.37
Monedă de Cupru (₥) - Romênia - 0.25
Zlato (ZŁ) - Sérvia - 0.18
Řezník (Ř) - Tchéquia - 0.10
"""
from time import sleep

sleep(1)
print(5*"=-", "Conversor de moedas", 5*"=-")
print("""[ 0 ] Льодник
[ 1 ] Marco Francês
[ 2 ] Kremówka
[ 3 ] Schwarzler
[ 4 ] Korona-Víz
[ 5 ] Monedă de Cupru
[ 6 ] Zlato
[ 7 ] Řezník """)
print(21*"=-")

moedas = ("Льодник",
        "Marco-Frances",
        "Kremówka",
        "Schwarzler",
        "Korona-Víz",
        "Monedă de Cupru",
        "Zlato",
        "Řezník")

taxas = {"Льодник": 10.00 , 
        "Marco-Frances": 7.50,
        "Kremówka": 5.80,
        "Schwarzler": 4.30,
        "Korona-Víz": 3.70,
        "Monedă de Cupru": 2.50,
        "Zlato":  1.80,
        "Řezník":  1.00}

sleep(1)
base = int(input("Converter de: "))
conversão = int(input("Converter para: "))
                        
print(f"Você escolheu converter de {base[moedas]} para {conversão[moedas]}")

