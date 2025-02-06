with open("list_employes.txt", "r", encoding ="utf-8") as file:
  contenido =  file.read()
  if "Sergio" in contenido:
    print("Sergio si llego tarde")       