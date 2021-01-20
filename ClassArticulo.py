class Articulo:
    articulos = []

    def __init__(self):
        self.idi = 0
        self.nombre = ""
        self.cantidad = 0
    
    def __repr__(self):
        return str(self.__dict__)

    def addArticulo(self, newarticulo):
        self.articulos.append(newarticulo)
    
    def getArticulos(self):
        return self.articulos

    def getArticulo(self, idi, nombre):
        if idi != None:
            for articulo in self.articulos:
                if(articulo.idi == idi):
                    return articulo
        elif nombre != None:
            for articulo in self.articulos:
                if(articulo.nombre == nombre):
                    return articulo

    def updateArticulosubtraction(self, idi, nombre, cantidad):
        if idi != None:
            for articulo in self.articulos:
                if(articulo.idi == idi and articulo.cantidad >= cantidad):
                    articulo.cantidad = articulo.cantidad - cantidad
                    return articulo
        elif nombre != None:
            for articulo in self.articulos:
                if(articulo.nombre == nombre and articulo.cantidad >= cantidad):
                    articulo.cantidad = articulo.cantidad - cantidad
                    return articulo
                    
    def updateArticulosum(self, idi, nombre, cantidad):
        if idi != None:
            for articulo in self.articulos:
                if(articulo.idi == idi):
                    articulo.cantidad = articulo.cantidad + cantidad
                    return articulo
        elif nombre != None:
            for articulo in self.articulos:
                if(articulo.nombre == nombre and articulo.cantidad >= cantidad):
                    articulo.cantidad = articulo.cantidad + cantidad
                    return articulo

    def getId(self, idi, nombre):
        if idi != None:
            for articulo in self.articulos:
                if(articulo.idi == idi):
                    return articulo.idi
        elif nombre != None:
            for articulo in self.articulos:
                if(articulo.nombre == nombre):
                    return articulo.idi

    def getNombre(self, idi, nombre):
        if idi != None:
            for articulo in self.articulos:
                if(articulo.idi == idi):
                    return articulo.nombre
        elif nombre != None:
            for articulo in self.articulos:
                if(articulo.nombre == nombre):
                    return articulo.nombre

    def getCantidad(self, idi, nombre):
        if idi != None:
            for articulo in self.articulos:
                if(articulo.idi == idi):
                    return articulo.cantidad
        elif nombre != None:
            for articulo in self.articulos:
                if(articulo.nombre == nombre):
                    return articulo.cantidad

 