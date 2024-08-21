import time
def mide_tiempo(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        print(time.time() - inicio)
        return c
    return funcion_medida


@mide_tiempo
def calcula_pares(n):
    return [i for i in range(n) if i% 2 == 0]

calcula_pares(10000000)