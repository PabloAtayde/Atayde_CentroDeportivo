from ClassPersona import *
from ClassArticulo import *
from ClassPrestamo import *
from datetime import datetime

listArticulos = Articulo()
listPersonaas = Persona()
listPrestamos = Prestamo()

idPersona = 0
idarticulo = 0
idprestamo = 0
time = datetime.now()
date = time.strftime("%Y-%m-%d+3 %H:%M:%S")

 

option = 1
while option != 0:

    print("\n")
    print("=== Menú ===")
    print("1.- Ingresar nuevo material.")
    print("2.- Crear nuevo usuario.")
    print("3.- Nuevo prestamo.")
    print("4.- Realizar devolución.")
    print("5.- Guardar lista de Personas.")
    print("6.- Guardar lista de materiales.")
    print("7.- Guardar lista de prestamos.")
    print("0.- Salir")
    option = int(input(" - Selecciona una opcion: "))
    print("\n")

    if option == 1:

        newarticulo = Articulo()
        
        print("------------ Registro de material ------------")
        print("\n")
        newarticulo.idi = idarticulo
        newarticulo.nombre = input("Nombre del material: ")
        newarticulo.cantidad = int(input("Cantidad a ingresar: "))

        listArticulos.addArticulo(newarticulo)

        idarticulo += 1

        print("\n")
        print(" - Registro exitoso! - ")
        print("\n")

        print("**** Lista de Material ****")
        articulos = listArticulos.getArticulos()
        for articulo in articulos:
            print('° '+articulo.nombre+' '+str(articulo.cantidad))


    elif option == 2:

        newPersona = Persona()

        print("------------ Registro de Persona ------------")
        newPersona.idp = idPersona
        newPersona.nombre = input("Nombre de la Persona: ")
        newPersona.apellido = input("Apellido de la Persona: ")
        newPersona.edad = int(input("Edad de la Persona: "))
        newPersona.contacto = int(input("Numero de telefóno de la Persona: "))
        newPersona.email = input("E - mail de la Persona: ")

        listPersonaas.addPersona(newPersona)

        idPersona += 1

        print("\n")
        print(" - Registro exitoso! - ")
        print("\n")

        print("**** Lista de Personas ****")
        Personaas = listPersonaas.getPersonaas()
        for Persona in Personaas:
            print('° '+Persona.nombre+' '+Persona.apellido+' '+str(Persona.edad)+' '+str(Persona.contact)+' '+Persona.email)

    elif option == 3:

        newPrestamo = Prestamo()

        idp = ""
        nombrePersona = ""
        contact = ""
        idi = ""
        nombreArticulo = ""
        cantidad = 0

        time = datetime.now()
        date = time.strftime("%Y-%m-%d+3 %H:%M:%S")

        print("------------ Registro de Prestamo ------------")
        print("\n")
        print("¿A traves de que quieres identificar a la Persona?")
        print("1.- Id")
        print("2.- Nombre")
        replyPersona = int(input("Selecciona una opción: "))

        if replyPersona == 1:

            idFind = int(input("Id de la Persona a registrar: "))
            idp = listPersonaas.getId(idFind, None)
            nombrePersona = listPersonaas.getnombre(idFind, None)
            contact = listPersonaas.getContact(idFind, None)


        elif replyPersona == 2:

            nombrePersonaFind = input("Nombre de la Persona a registrar: ")
            idp = listPersonaas.getId(None, nombrePersonaFind)
            nombrePersona = listPersonaas.getnombre(None, nombrePersonaFind)
            contact = listPersonaas.getContact(None, nombrePersonaFind)

        print("\n")
        print("¿A traves de que quieres identificar el material?")
        print("1.- Id")
        print("2.- Nombre")
        replyarticulo = int(input("Selecciona una opción: "))

        if replyarticulo == 1:

            idiFind = int(input("Id del material a prestar: "))
            idi = listArticulos.getId(idiFind, None)
            nombreArticulo = listArticulos.getNombre(idiFind, None)


        elif replyarticulo == 2:

            nombreArticuloFind = input("Nombre del material a prestar: ")
            idi = listArticulos.getId(None, nombreArticuloFind)
            nombreArticulo = listArticulos.getNombre(None, nombreArticuloFind)
            
        cantidad = int(input("Cantidad de material a prestar: "))
        
        newPrestamo.idt = idprestamo
        newPrestamo.PersonaId = idp
        newPrestamo.personaNombre = nombrePersona
        newPrestamo.personaContacto = contact
        newPrestamo.articuloId = idi
        newPrestamo.articuloNombre = nombreArticulo
        newPrestamo.articulocantidad = cantidad
        newPrestamo.date = date

        listPrestamos.addPrestamo(newPrestamo)

        articulosSub = listArticulos.updateArticulosubtraction(idi, None, int(cantidad))
        print(articulosSub)

        idprestamo += 1

        print("\n")
        print(" - Registro exitoso! - ")
        print("\n")
   
        print("**** Lista de Prestamos ****")
        prestamos = listPrestamos.getPrestamos()
        for prestamo in prestamos:
            print(prestamo.personaNombre+' '+str(prestamo.personaContactoo)+' '+prestamo.articuloNombre+' '+str(prestamo.articulocantidad)+' '+prestamo.date)


    elif option == 4:
        
        print("--------------- Devolver Prestamo ---------------")
        print("\n")
        print("**** Lista de Prestamos ****")
        prestamos = listPrestamos.getPrestamos()
        for prestamo in prestamos:
            print(str(prestamo.idt)+' '+prestamo.personaNombre+' '+str(prestamo.personaContactoo)+' '+prestamo.articuloNombre+' '+str(prestamo.articuloCantidad)+' '+prestamo.date)
        
        print("\n")
        idt = int(input("Ingrese el id del prestamo para la devolución: "))

        idiSum = 0
        cantidadSum = 0
        for prestamo in prestamos:
            if prestamo.idt == idt:
                prestamo.date_return = date
                idiSum = prestamo.articuloId
                cantidadSum = prestamo.articuloCantidad

        articulosum = listArticulos.updateArticulosum(idiSum,None,cantidadSum)
        print(articulosum)
        
        print("\n")
        print("**** Lista de Prestamos ****")
        for prestamo in prestamos:
            print(str(prestamo.idt)+' '+prestamo.personaNombre+' '+str(prestamo.personaContacto)+' '+prestamo.articuloNombre+' '+str(prestamo.articulocantidad)+' '+prestamo.date_return)

    elif option == 5:
        print("\n")
        print("**** Archivo Creado ****")
        filePersona = "filePersona.csv"
        csvp = open(filePersona,"w")
        titlesp = "Id,Nombre,Apellido,Edad,Contacto,Email\n"
        csvp.write(titlesp)  
        PersonaList = listPersonaas.getPersonaas()        
        for Persona in PersonaList:
            idP = str(Persona.idp)
            nombre = Persona.nombre
            apellido = Persona.apellido
            edad = str(Persona.edad)
            contact = str(Persona.contact)
            email = Persona.email
            rowsp = idP+","+nombre+","+apellido+","+edad+","+contact+","+email+"\n"
            csvp.write(rowsp)
            print(str(Persona.idp)+" "+Persona.nombre+" "+Persona.apellido+" "+str(Persona.edad)+" "+str(Persona.contacto)+" "+Persona.email)
    
    elif option == 6:
        print("\n")
        print("**** Archivo Creado ****")
        filearticulo = "filearticulo.csv"
        csvi = open(filearticulo,"w")
        titlesi = "Id,Nombre,Cantidad\n"
        csvi.write(titlesi)  
        articulosList = listArticulos.getArticulos()        
        for articulo in articulosList:
            idi = str(articulo.idi)
            nombre = articulo.nombre
            cantidad = str(articulo.cantidad)
            rowsi = idi+","+nombre+","+cantidad+"\n"
            csvi.write(rowsi)
            print(str(articulo.idi)+" "+articulo.nombre+" "+str(articulo.cantidad))
    
    elif option == 7:
        print("\n")
        print("**** Archivo Creado ****")
        fileprestamo = "fileprestamo.csv"
        csvt = open(fileprestamo,"w")
        titlest = "Id,Persona_Id,Persona_Nombre,Contacto,Material_Id,Material_Nombre,Cantidad,Fecha,Devolución\n"
        csvt.write(titlest)  
        prestamosList = listPrestamos.getPrestamos()
        for prestamo in prestamosList:
            idt = str(prestamo.idt)
            PersonaId = str(prestamo.PersonaId)
            personaNombre = prestamo.personaNombre
            personaContacto = str(prestamo.personaContacto)
            articuloId = str(prestamo.articuloId)
            articuloNombre = prestamo.articuloNombre
            articuloCantidad = str(prestamo.articuloCantidad)
            date = prestamo.date
            date_return = prestamo.date_return
            rowst = idt+","+PersonaId+","+personaNombre+","+personaContacto+","+articuloId+","+articuloNombre+","+articuloCantidad+","+date+","+date_return+"\n"
            csvt.write(rowst)
            print(str(prestamo.idt)+' '+prestamo.personaNombre+' '+str(prestamo.personaContacto)+' '+prestamo.articuloNombre+' '+str(prestamo.articuloCantidad)+' '+prestamo.date)