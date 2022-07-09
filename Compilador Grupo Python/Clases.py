from operator import truediv


class Terceto:
    
    def __init__(self,nro_terceto,valor1,valor2,valor3):
        self.nro_terceto = nro_terceto
        self.valor1 = valor1
        self.valor2 = valor2
        self.valor3 = valor3
                
    def mostrar_terceto(self):
        return "["+str(self.nro_terceto)+"] ("+str(self.valor1)+","+str(self.valor2)+","+str(self.valor3)+")"

    def get_nro_terceto(self):
        return self.nro_terceto;

    def get_nombre_terceto(self):
        return "["+str(self.nro_terceto)+"]"

    def set_valor1(self,valor):
        self.valor1 = valor

    def set_valor2(self,valor):
        self.valor2 = valor

    def set_valor3(self,valor):
        self.valor3 = valor      

    def get_valor1(self):
        return self.valor1   

    def get_valor2(self):
        return self.valor2 

    def get_valor2_num(self):
        return str(self.valor2)[1:len(str(self.valor2))-1]

    def get_valor3(self):
        return self.valor3


  

class Pila:

    def __init__(self):
        """ Crea una pila vacía. """
        # La pila vacía se representa con una lista vacía
        self.items=[]

    def apilar(self, x):
    # Apilar es agregar al final de la lista.
        self.items.append(x)    

    def desapilar(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")
    
    def pila_vacia(self):
        if (len(self.items)==0):
            return True
        else : 
            return False         

class PilaPuntero:
    def __init__(self,nombrePila):
        self.pila = Pila()
        self.nombre = nombrePila

    def get_nombre(self):
        return self.nombre

    def get_pila (self):
        return self.pila

    
      
    


class TablaDeSimbolos:
    def __init__(self,nombre,tipo,valor,alias,limite,longitud):
        self.nombre = nombre
        self.tipo = tipo
        self.valor = valor
        self.alias = alias
        self.limite = limite
        self.longitud = longitud
    
    def get_nombre(self):
        return self.nombre

    def get_tipo(self):
        return self.tipo

    def get_valor(self):
        return self.valor    

    def set_tipo(self,tipo):
        self.tipo = tipo

    def set_valor(self,valor):
        self.tipo = valor

    def set_limite(self,limite):
        self.tipo = limite

    def set_longitud(self,longitud):
        self.tipo = longitud

    def get_tabla_simbolos(self):
        return  str("{:<30}|{:<7}|{:<30}|{:<15}|{:<10}|{:<10}".format(self.nombre,self.tipo,self.valor,self.alias,self.limite,self.longitud))






