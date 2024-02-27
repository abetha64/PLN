archivo =open("archivorandom.txt", "w")

archivo.write("ESTO ES TEXTO NUEVO \n")
archivo.write("ESTO TAMBIEN\n")
archivo.write("MIRA, PUEDO ESCRIBIR \" COMILLAS")
archivo.write("GRACIAS A BEBI \n")
archivo.close()

# abrir=open("fime2.txt","r")
# abrir = abrir.read()
# abrir.close()
#holasoyalba

archivo =open("archivorandom.txt")
texto= archivo.read()
print (texto)
archivo.close()


