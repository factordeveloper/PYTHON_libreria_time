import timeit
tiempo = timeit.timeit('lista = [i for i in range(1000000) if i%2 ==0]', number =50)
print(tiempo/5)