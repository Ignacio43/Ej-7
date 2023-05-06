import csv


if __name__=='__main__':
    p=[]
    p=listadeviajeros()
   
    
    v5=p[2]
    h= v5==100
    print(f"el resultado de la operacion al comparar {v5.cantidadTotalMillas()} y 100 es {h} \n")
    print(200==v5)
    

    v6=p[3]
    print(f"valor actual de millas de un objeto de viajero frecuente en millas: {v6.cantidadTotalMillas()} \n")
    v6=100 + v6
    print(f"el resultado luego e sumar 100 millas {v6.cantidadTotalMillas()} \n")
    
    v7=p[4]
    print(f"valor actual de millas antes dle canje: {v7.cantidadTotalMillas()} \n")
    v7=100 - v7
    if v7:
        print(f"el numero de millas despues del canje es de {v7.cantidadTotalMillas()} \n")