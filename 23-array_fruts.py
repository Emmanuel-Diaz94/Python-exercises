fruts = ["manzana", "platano", "sandia", "fresa"]


print("lista completa de frutas:" , fruts)

print("la primera fruta es" , fruts[0])

print("la ultima fruta es" , fruts[-1])

fruts.append("melon")

print("lista completa de frutas", fruts)

fruts.remove("sandia")

print("lista completa de frutas despues de remover sandia", fruts)

for my_frut in fruts:
    print(my_frut)
    
if "fresa" in fruts:
        print("la fresa esta en la lista")