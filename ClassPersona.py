class persona:
     
    personas = []

    def __init__(self):
        self.idp = 0
        self.nombre = ""
        self.apellido = ""
        self.edad = 0
        self.contacto = 0
        self.email = ""  
    
    def __repr__(self):
        return str(self.__dict__)
     
    def addPersonaa(self, newpersona):
        self.personas.append(newpersona)
        
    def getPersonaas(self):
        return self.personas

    def removePersona(self, idp, nombre):  
        index = 0
        if idp != None:
            for persona in self.personas:
                if(persona.idp == idp):                   
                    self.personas.pop(index)
                    return self.personas
                index += 1
        elif nombre != None:
            for persona in self.personas:
                if(persona.nombre == nombre):
                    self.personas.pop(index)
                    return self.personas
                index += 1

    def getPersona(self, idp = None, nombre = None):
        if idp != None:
            for persona in self.personas:
                if(persona.idp == idp):
                    return persona
        elif nombre != None:
            for persona in self.personas:
                if(persona.nombre == nombre):
                    return persona

    def getId(self, idp = None, nombre = None):
        if idp != None:
            for persona in self.personas:
                if(persona.idp == idp):
                    return persona.idp
        elif nombre != None:
            for persona in self.personas:
                if(persona.nombre == nombre):
                    return persona.idp

    def getNombre(self, idp = None, nombre = None):
        if idp != None:
            for persona in self.personas:
                if(persona.idp == idp):
                    return persona.nombre
        elif nombre != None:
            for persona in self.personas:
                if(persona.nombre == nombre):
                    return persona.nombre

    def getContacto(self, idp = None, nombre = None):
        if idp != None:
            for persona in self.personas:
                if(persona.idp == idp):
                    return persona.contacto
        elif nombre != None:
            for persona in self.personas:
                if(persona.nombre == nombre):
                    return persona.contacto