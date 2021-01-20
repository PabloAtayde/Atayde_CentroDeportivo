class Prestamo:
     prestamos = []

     def __init__(self):
          self.idt = 0
          self.personaId = ""
          self.personaNombre = ""
          self.personaContacto = ""
          self.articuloId = 0
          self.articuloNombre = ""
          self.articuloCantidad = 0
          self.date = ""
          self.date_return = ""
     
     def __repr__(self):
          return str(self.__dict__)
     
     def addPrestamo(self, newprestamo):
          self.prestamos.append(newprestamo)

     def getPrestamos(self):
          return self.prestamos
     
     def dropPrestamo(self, idt):
          index = 0
          if idt != None:
               for prestamo in self.prestamos:
                    if(prestamo.idt == idt):                   
                         self.prestamos.pop(index)
                         return self.prestamos
                    index += 1
