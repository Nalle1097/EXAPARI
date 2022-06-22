n = True
while n:
    print("elige alguna de las  opciones")
    print("Opcion A. 270")
    print("Opcion B. 340")
    print("Opcion C. 390")
    print("Opcion D. SALIR")
    op = input()  ##variable por teclado
    
    if op == "A" or op == "a":
        print("La cantidad a pagar son 270 ")
        m = int(input()) ##parametro necesario
        p = 1
        suma=0
        while p <= m: ##utilizarlo 1 hasta m
            print("Dame el numero",p)
            num = int(input())
            if num % 2 == 0:
                suma =suma + num
            p = p + 1
        print("LA SUMA DE LOS NUMEROS  ES....",suma)
        
    if op == "B" or op == "b":
        print("La cantidad de numeros a sumar ")
        m = int(input()) 
        p = 1
        suma=0
        while p <= m: ##utilizarlo 1 hasta m
            print("Dame el numero",p)
            num = int(input())
            if num % 2 == 1:
                suma =suma + num
            p = p + 1
        print("LA SUMA DE LOS NUMEROS  ES....",suma)
        
    if op == "C" or op == "c":
        w = True
        while w:
            print("Dame un numero")
            num = int(input())
            suma = suma + num
            print("la suma es", suma)
            if suma >= 100:
                w = False
            print("Se detuvo el programa ")
    if op == "D" or op == "d":
        print("BYE , VUELVE PRONTO")
        n = False