import time

inicio = time.time()
lista = [i for i in range(10000000) if i%2 ==0]

fin = time.time()
print(fin-inicio)