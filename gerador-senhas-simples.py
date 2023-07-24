# Bem-vindo ao Gerador de Senhas Simples!
print("Bem-vindo ao Gerador de Senhas Simples")

import random
import string

# Digite o comprimento desejado da senha:
comprimento = int(input("Digite o comprimento da senha desejada: "))

# Incluir letras maiúsculas? (sim/não):
incluir_maiusculas = input("Incluir letras maiúsculas? (sim/não): ").lower() == "sim"

# Incluir letras minúsculas? (sim/não):
incluir_minusculas = input("Incluir letras minúsculas? (sim/não): ").lower() == "sim"

# Incluir números? (sim/não):
incluir_numeros = input("Incluir números? (sim/não): ").lower() == "sim"

# Incluir caracteres especiais? (sim/não):
incluir_especiais = input("Incluir caracteres especiais? (sim/não): ").lower() == "sim"

# Crie uma string contendo todos os caracteres possíveis com base nas escolhas do usuário
caracteres = ""
if incluir_maiusculas:
    caracteres += string.ascii_uppercase
if incluir_minusculas:
    caracteres += string.ascii_lowercase
if incluir_numeros:
    caracteres += string.digits
if incluir_especiais:
    caracteres += string.punctuation

# Gere a senha aleatória usando random.choices
senha_gerada = ''.join(random.choices(caracteres, k=comprimento))

# Exiba a senha gerada na tela
print("Senha gerada:", senha_gerada)
