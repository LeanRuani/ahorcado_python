palabra = input ("Ingrese palabra: ").upper()
errores = int(input("Ingrese cantidad de errores: "))+1
intentos = 0
error = 0

while error < errores:
    print ("errores", error)
    print ("intentos", intentos)
    print ("palabra", len(palabra))
    if len(palabra)!=0:
        intentos+=1
        ocurrencia = False
        letra = input ("Ingrese letra: ").upper()
        for i in palabra:
            if i == letra:
                palabra = palabra.replace(letra, "")
                ocurrencia = True
        if ocurrencia==False:
            error+=1
    else:
      print (intentos)
      break
else:
    if error == errores:
        print (0)
    else:
        print (intentos)