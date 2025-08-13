print("hola mundo desde python")
#variables numericas
edad = 25 #entero
altura=1.75 #flotante
bandera = True #boleano
nombre = "bruno Diaz "#string
print("\nprint tradicional")
print("----------------")
print ("mi nombre es:",nombre)
print ("mi edad es :",edad)
print ("mi altura es :",altura)
print ("estoy vivo xd",bandera)
#segunda forma de imprimir variables
print("\nprint moderno")
print("---------------")
print(f"mi nombre es {nombre}")
print(f"mi edad es : {edad}")
print(f"mi altura es :{altura}")
print(f"estoy vivo: {bandera}")
 

 #entrada de datos
print("\n entrada de datos")
print("----------------")
nombre=input("introduce tu nombre: ")
edad=int(input("ingresa tu edad:"))
altura=float(input("ingresa tu altura:"))
bandera = input("¿stas vivo?(true\false):")
#segunda forma de imprimir variables
print("\nprint moderno")
print("---------------")
print(f"mi nombre es {nombre}")
print(f"mi edad es : {edad}")
print(f"mi altura es :{altura}")
print(f"estoy vivo: {bandera}")