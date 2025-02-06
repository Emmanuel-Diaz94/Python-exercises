def calc_area_rectangle(largo, ancho):
    area = largo * ancho
    print("El area del rectangulo es:" + str(area))


num1 = int(input("ingrese el largo del articulo: "))
num2 = int(input("ingrese el ancho del articulo: "))

calc_area_rectangle(num1,num2)