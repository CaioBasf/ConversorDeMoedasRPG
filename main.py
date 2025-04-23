""""
Moeda - País - Valor em relação ao Lyodnik
Льодник (₴) - Aurória - 10.00
Marco Francês (ℳ) - Marselha - 7.50
Kremówka (Kℳ) - Polônia - 5.80
Schwarzler (Ś) - Áustria - 4.30
Korona-Víz (₭) - Hungria - 3.70
Monedă de Cupru (₥) - Romênia - 2.50
Zlato (ZŁ) - Sérvia - 1.80
Řezník (Ř) - Tchéquia - 1.00
"""
from time import sleep
import flet as ft

taxas = {"russo": 10.0, #Льодник
        "frances": 7.50, #Marco Francês
        "polonia": 5.80, # Kremówka
        "austria": 4.30, # Schwarzler
        "hungria": 3.70, # Korona-Víz
        "romenia": 2.50, # Monedă de Cupru 
        "servia":  1.80, # Zlato
        "tcheca":  1.00 # Řezník
}

# Valor que o usuario vai converter
valor = float(input("Valor a ser convertido: "))

# O usuario quer converter de
base = input("Converter de: ")
# para 
conversao = input("Converter para: ")

if base not in taxas or conversao not in taxas: 
    print("Moeda invalida!")
else:
    resultado = (valor * taxas[base]) / taxas[conversao]
    print(f" {valor} {base} = {resultado:.2f} {conversao} ")

