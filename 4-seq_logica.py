# 4) Descubra a lógica e complete o próximo elemento:
# a) 1, 3, 5, 7, ___
# b) 2, 4, 8, 16, 32, 64, ____
# c) 0, 1, 4, 9, 16, 25, 36, ____
# d) 4, 16, 36, 64, ____
# e) 1, 1, 2, 3, 5, 8, ____
# f) 2,10, 12, 16, 17, 18, 19, ____

# letra a)
def letra_a():
    sequencia = [1, 3, 5, 7]
    numero = sequencia[-1] + 2
    sequencia.append(numero)
    print(sequencia)
def letra_b():
    sequencia = [2, 4, 8, 16, 32, 64]
    numero = sequencia[-1] * 2
    sequencia.append(numero)
    print(sequencia)
def letra_c():
    sequencia = [0, 1, 4, 9, 16, 25, 36]
    numero = sequencia[-1] + ((sequencia[-1] - sequencia[-2]) + 2)
    sequencia.append(numero)
    print(sequencia)
def letra_d():
    sequencia = [4, 16, 36, 64]
    numero = sequencia[-1] + ((sequencia[-1] - sequencia[-2]) + 8)
    sequencia.append(numero)
    print(sequencia)
def letra_e():
    sequencia = [1, 1, 2, 3, 5, 8]
    numero = sequencia[-1] + sequencia[-2]
    sequencia.append(numero)
    print(sequencia)
def letra_f():
    sequencia = [2, 10, 12, 16, 17, 18, 19]
    numero = 200
    sequencia.append(numero)
    print(sequencia)



print("letra A)")
letra_a()
print("letra B)")
letra_b()
print("letra C)")
letra_c()
print("letra D)")
letra_d()
print("letra E)")
letra_e()
print("letra F)")
letra_f()