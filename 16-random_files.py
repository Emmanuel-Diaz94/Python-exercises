import random 

for i in range(100):
    random_number = random.randint(1, 9999)
    file_name = "factura_" + str(random_number)+ ".doc"
    
    with open(file_name, "w") as file:
        file.write("contenido de la factura" + " " + str(random_number))
    
    print("archivo creado :", file_name)