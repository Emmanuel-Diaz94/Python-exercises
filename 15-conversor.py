print("CONVERSOR DE MONEDAS")
print("opciones_ 1- dolar. 2- euro, 3-peso mexicano")
convert_currency = int(input("elije la opcion a convertir"))
print("opciones_ 1- dolar. 2- euro, 3-peso mexicano")                    
convert_current_currency = int(input("elige tu moneda actual"))
                               
money_convert = float(input("ingresa la cantidad de dinero a convertir"))
                      
#si eligio dolares y su moneda es euros, entoces va a convertir de euros a dolares 
if money_convert == 1 and convert_current_currency == 2:
    convert =  money_convert * 0.97
    print("tu dinero en dolares es: " + str(convert))
#si eligoio dolares y su moneda son pesos mexicanos, entonces va a convertir a de pesos mexicanos a dolares
elif convert_currency == 1 and convert_current_currency == 3:
    convert = money_convert /20
    print("tu dinero en dolares es: " + str(convert))