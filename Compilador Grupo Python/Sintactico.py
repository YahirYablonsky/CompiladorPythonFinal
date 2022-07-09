# Para ejecutar
# [.....]\tp\venv\Scripts> python ..\..\src\Analizador_Sintactico_TP2.py
from operator import indexOf
import ply.yacc as yacc
import os
from Lexico import tokens
from Lexico import analizador
from Lexico import tablaDeSimbolos
from Clases import TablaDeSimbolos, Terceto
from Clases import Pila
from Clases import Pila
from Clases import TablaDeSimbolos
import Tercetos_to_assembler
from collections import OrderedDict
PATH_PRUEBAS = os.path.dirname(os.path.abspath(__file__))

#PASO 1. DEFINO LA PRECEDENCIA DE LOS OPERADORES
precedence = (
    ('right','ASSIGN'),
    ('left','NE','EQUAL'),
    ('left','LT','LTE','GT','GTE'),
    ('left','PLUS','MINUS'),
    ('left','MULT','DIVIDE','REST'),
    ('left','LBRA','RBRA'),
    ('left','COMMA')
    )

#PASO 2. DEFINO LA LISTA DE VARIABLES Y EL RESULTADO DE LA GRAMÁTICA
variables = {}
resultado_gramatica = []
reglas_aplicadas = []

#Definición de punteros


l_tercetos = []
d_pilas = {}
d_punteros = {}
contador_terceto = 0

def crear_terceto (puntero,valor1,valor2,valor3):
    global contador_terceto                       
    l_tercetos.append(Terceto(contador_terceto,valor1,valor2,valor3))
    d_punteros.update({puntero:contador_terceto})
    contador_terceto +=1

def f_puntero(puntero):
    return "["+str(puntero)+"]"

def actualizar_puntero(punteroActual,valor):
    d_punteros.update({punteroActual:d_punteros.get(valor)})

def d_apilar (nombrePila,valor):
    d_pilas.get(nombrePila).apilar(valor)

def d_desapilar (nombrePila):
    return d_pilas.get(nombrePila).desapilar()

def d_inicializar_pilas():
    d_pilas.update({"pl_expresion":Pila()})
    d_pilas.update({"pl_condicion":Pila()})
    d_pilas.update({"pl_salto":Pila()})
    d_pilas.update({"pl_op_logico":Pila()})
    d_pilas.update({"pl_tipo_dato":Pila()})
    d_pilas.update({"pl_id_dec":Pila()})
    d_pilas.update({"pl_ciclo":Pila()})
    d_pilas.update({"pl_op_while":Pila()})
    d_pilas.update({"pl_while":Pila()})

def modificar_terceto_valor2(puntero,valor):
    if(l_tercetos[puntero].get_valor2() == '_'):
        l_tercetos[puntero].set_valor2(f_puntero(valor))    
    
def get_tipo_salto(operador_logico):
    if(operador_logico== '<'):
        return "BGE"
    elif(operador_logico== '<='):
        return "BGT"
    elif(operador_logico== '>'):
        return "BLE"
    elif(operador_logico== '>='):
        return "BLT"
    elif(operador_logico== '!='):
        return "BEQ"
    elif(operador_logico== '='):
        return "BNE"      

def find_element_tabla_simbolos(elemento):
    for i in tablaDeSimbolos:
        if(elemento == i.get_nombre()):
            return i
    return None



d_inicializar_pilas();
#START VA A SER "PROGRAM"
def p_program(p):
                    ''' programa : bloque'''
                    global tablaDeSimbolos
                    reglas_aplicadas.append('Entro en Regla 01: P->B')
                    d_punteros.update({'p_programa':d_punteros.get("p_bloque")})
                    actualizar_puntero("p_bloque","p_program")
                   
                    Tercetos_to_assembler.genera_assembler(l_tercetos)

#UN BLOQUE ES UN CONJUNTO DE SENTENCIAS O UNA SENTENCIA
def p_bloque_1(p):
                        ''' bloque : bloque sentencia ENDL'''
                        reglas_aplicadas.append('Entro en Regla 02: B-> B S')
                        actualizar_puntero("p_bloque","p_sentencia")

#UN BLOQUE ES UN CONJUNTO DE SENTENCIAS O UNA SENTENCIA
def p_bloque_2(p):
                        ''' bloque : sentencia ENDL'''
                        reglas_aplicadas.append('Entro en Regla 02: B-> S')
                        actualizar_puntero("p_bloque","p_sentencia")

#UNA SENTENCIA ES: UNA SENT_WHILE, SENT_ASIG, SENT_COND, SENT_DECL, SENT_WRITE, SENT_READ
def p_sentencia_1(p):
                        ''' sentencia : asignacion''' 
                        reglas_aplicadas.append("Entro en Regla 05: S -> SA")
                        actualizar_puntero("p_sentencia","p_asignacion")

def p_sentencia_2(p):
                        ''' sentencia : sent_condicional''' 
                        reglas_aplicadas.append("Entro en Regla 05: S -> SC")

def p_sentencia_3(p):
                        ''' sentencia : sent_declaracion''' 
                        reglas_aplicadas.append("Entro en Regla 05: S -> SD")                        

def p_sentencia_4(p):
                        ''' sentencia : sent_write''' 
                        reglas_aplicadas.append("Entro en Regla 05: S -> SWR")

def p_sentencia_5(p):
                        ''' sentencia : sent_read''' 
                        reglas_aplicadas.append("Entro en Regla 05: S -> SR")                        

def p_sentencia_6(p):
                        ''' sentencia : sent_while''' 
                        reglas_aplicadas.append("Entro en Regla 05: S -> SW")   
                                                                        
#GRAMATICA DE ASIGNACION
def p_setencia_asig(p):
                        ''' asignacion : ID ASSIGN expresion'''
                        reglas_aplicadas.append("Entro en Regla 31: SA -> ID := E")
                        crear_terceto("p_asignacion",p[2],p[1],f_puntero(d_punteros.get("p_expresion")))




#-------------------------------EXPRESION----------------------------------------------------
def p_expresion_plus(p):
                        
                        ''' expresion : expresion PLUS termino'''
                        reglas_aplicadas.append("Entro en Regla 32: E -> E + T")
                        crear_terceto("p_expresion",p[2],f_puntero(d_punteros.get("p_expresion")),f_puntero(d_punteros.get("p_termino")))
def p_expresion_minus(p):
                        
                        ''' expresion : expresion MINUS termino'''
                        reglas_aplicadas.append("Entro en Regla 33: E -> E - T")
                        crear_terceto("p_expresion",p[2],f_puntero(d_punteros.get("p_expresion")),f_puntero(d_punteros.get("p_termino")))

def p_expresion_ter(p):
                        ''' expresion :  termino'''
                        reglas_aplicadas.append("Entro en Regla 34: E -> T")
                        actualizar_puntero("p_expresion","p_termino")


#------------------------.TERMINO-------------------------------------------------
def p_termino_mult(p):
                        
                        ''' termino : termino MULT factor'''
                        reglas_aplicadas.append("Entro en Regla 35: T -> T * F")
                        crear_terceto("p_termino",p[2],f_puntero(d_punteros.get("p_termino")),f_puntero(d_punteros.get("p_factor")))
def p_termino_divide(p):
                        
                        ''' termino : termino DIVIDE factor'''
                        reglas_aplicadas.append("Entro en Regla 36: T -> T / F")
                        crear_terceto("p_termino",p[2],f_puntero(d_punteros.get("p_termino")),f_puntero(d_punteros.get("p_factor")))
def p_termino_rest(p):
                        
                        ''' termino : termino REST factor'''
                        reglas_aplicadas.append('''Entro en Regla 37: T -> T  F''')
                        crear_terceto("p_termino",p[2],f_puntero(d_punteros.get("p_termino")),f_puntero(d_punteros.get("p_factor")))

def p_termino_factor(p):
                        ''' termino : factor'''
                        reglas_aplicadas.append("Entro en Regla 38: T -> F")
                        actualizar_puntero("p_termino","p_factor")

#-------------------------FACTOR-------------------------------------------------

    
def p_termino_const_int(p):
                        ''' factor : INTEGER'''
                        reglas_aplicadas.append("Entro en Regla 39: F-> INTEGER")
                        crear_terceto("p_factor","_"+str(p[1]),"_","_")

def p_termino_id(p):
                        ''' factor : ID '''
                        reglas_aplicadas.append("Entro en Regla 40: F-> ID")
                        crear_terceto("p_factor",p[1],"_","_")

def p_termino_const_float(p):
                        ''' factor : FLOATD'''
                        reglas_aplicadas.append("Entro en Regla 41: F-> FLOAT")
                        crear_terceto("p_factor","_"+str(p[1]),"_","_")
                        
                    

def p_termino_expr(p):
                        ''' factor : LBRA expresion RBRA '''
                        reglas_aplicadas.append("Entro en Regla 42: T-> (E)")
                        actualizar_puntero("p_factor","p_expresion")
                        


#GRAMATICA DE CONDICIÓN
def p_condicional1(p):
                            ''' sent_condicional : IF condicion fin_cond_verd OP_BRA bloque CL_BRA'''
                            reglas_aplicadas.append('''Entro en Regla 14: SC -> IF LC { LS }''' )
                            modificar_terceto_valor2(d_desapilar("pl_salto"),contador_terceto)
     
    
def p_fin_cond_verd(p):
                            '''fin_cond_verd :'''
                            
                            while (not d_pilas.get("pl_expresion").pila_vacia()):
                                operador = d_desapilar("pl_op_logico")
                                expresion2 = d_desapilar("pl_expresion")
                                expresion1 = d_desapilar("pl_expresion")
                                crear_terceto("p_cmp","CMP",expresion1,expresion2)
                                crear_terceto("p_branch",get_tipo_salto(operador),"_","_")
                                d_apilar("pl_salto",d_punteros.get("p_branch"))
                         
def p_sentencia_cond_else(p):
                            ''' sent_condicional : IF condicion fin_cond_verd OP_BRA bloque CL_BRA fin_bloque_verd ELSE OP_BRA bloque CL_BRA '''
                            reglas_aplicadas.append('''Entro en Regla 16: SC -> IF LC { LS }  ELSE { LS }''' )
                            modificar_terceto_valor2(d_desapilar("pl_salto"),contador_terceto)
                           

def p_fin_bloque_verd (p):
                        '''fin_bloque_verd :'''
                        crear_terceto("p_else","BI","_","_")
                        while(not d_pilas.get("pl_salto").pila_vacia()):
                                modificar_terceto_valor2(d_desapilar("pl_salto"),contador_terceto)
                        d_apilar("pl_salto",d_punteros.get("p_else"))
                        
                    

def p_condicion(p): 
                        ''' condicion : expresion apilo_expresion op_logico expresion apilo_expresion'''
                        reglas_aplicadas.append('''Entro en Regla 22: C -> E OP_L E''' )
                        #crear_terceto("p_condicion","CMP",f_puntero(d_desapilar("pl_expresion")),f_puntero(d_punteros.get("p_expresion")))
                        


def p_apilo_expresion(p):
                        '''apilo_expresion :'''
                        d_apilar("pl_expresion",d_punteros.get("p_expresion"))
                        

def p_condicion_par(p):
                    ''' condicion : LBRA condicion RBRA '''          
                    reglas_aplicadas.append('''Entro en Regla 22: C -> (C)''' )              

def p_condicion_and(p): 
                        ''' condicion : condicion  AND condicion'''
                        reglas_aplicadas.append('''Entro en Regla 22: C -> C AND C''' )
                                      

def p_condicion_or(p): 
                        ''' condicion : condicion salto_opuesto OR condicion'''
                        reglas_aplicadas.append('''Entro en Regla 22: C -> C OR C''' )
                        modificar_terceto_valor2(d_punteros.get("p_or"),contador_terceto)
                        print(contador_terceto)


def p_salto_opuesto(p): 
                    ''' salto_opuesto :'''
                    actualizar_puntero("p_or","p_branch")

def p_op_logico(p):
                        ''' op_logico : NE 
                        | LT 
                        | LTE
                        | GT 
                        | GTE 
                        | EQUAL
                        '''
                        reglas_aplicadas.append('''Entro en Regla 25-30: OP_L -> NE | LT | LTE | GT | GTE | EQUAL''' )
                        d_apilar("pl_op_logico",p[1])
                      
##BETWEEN 
def p_condicion_between1(p):
                            ''' condicion_between : BETWEEN LBRA ID COMMA tupla RBRA '''
                            reglas_aplicadas.append('''Entro en Regla 58: CD_BTW -> BETWEEN ( tupla ) ''' )
                            global pt_condicion_between
                    
                            expresion2 = d_desapilar("pl_expresion")
                            expresion1 = d_desapilar("pl_expresion")

                            d_apilar("pl_expresion",p[3])
                            d_apilar("pl_expresion",expresion1)
                            d_apilar("pl_op_logico",">")
                            d_apilar("pl_expresion",p[3])
                            d_apilar("pl_expresion",expresion2)
                            d_apilar("pl_op_logico","<")



def p_tupla(p):
                            ''' tupla :  OP_BRC expresion apilo_expresion ENDL expresion apilo_expresion CL_BRC '''
                            reglas_aplicadas.append('''Entro en Regla 59: tupla -> [TI;TD] ''' )
                          
                                               
def p_condicion_between2(p):
                            ''' condicion : condicion_between '''
                            reglas_aplicadas.append('''Entro en Regla 62: C -> C_BTW''' )


#GRAMATICA DE WHILE
def p_sentencia_while(p):
                            ''' sent_while : WHILE pre_cond_wh condicion fin_cond_wh OP_BRA bloque CL_BRA'''
                            reglas_aplicadas.append('Entro en Regla 11: SW -> WHILE LC { LS } ' )
                            crear_terceto("p_while","BI",d_desapilar("pl_ciclo"),"_")
                            modificar_terceto_valor2(d_desapilar("pl_while"),contador_terceto) 
                            
def p_fin_cond_while(p):
                        "fin_cond_wh :"
                        
                        while (not d_pilas.get("pl_expresion").pila_vacia()):
                                operador = d_desapilar("pl_op_logico")
                                expresion2 = d_desapilar("pl_expresion")
                                expresion1 = d_desapilar("pl_expresion")
                                crear_terceto("p_cmp","CMP",expresion1,expresion2)
                                crear_terceto("p_branch",get_tipo_salto(operador),"_","_")
                                d_apilar("pl_while",d_punteros.get("p_branch"))
                        
                           

def p_pre_cond_while(p):
                            "pre_cond_wh :"
                            d_apilar("pl_ciclo",contador_terceto) 




#GRAMATICA DE DECLARACION
def p_sentencia_declaracion(p):
    ''' sent_declaracion : DECVAR lista_declaraciones ENDDEC'''
    reglas_aplicadas.append('''Entro en Regla 49: SD -> DECVAR LD ENDDEC ''' )


def p_lista_declaraciones_1(p):
    ''' lista_declaraciones : lista_declaraciones  declaracion'''
    reglas_aplicadas.append('''Entro en Regla 50: LD -> LD ; D ''' )
    

def p_lista_declaraciones_2(p):
    ''' lista_declaraciones : declaracion  '''
    reglas_aplicadas.append('''Entro en Regla 51: LD -> D ''' )
    

def p_declaracion(p):
    ''' declaracion : lista_id COLON tipo_dato ENDL'''
    reglas_aplicadas.append('''Entro en Regla 52: D -> LI COLON TIPO ENDL''' )
    tipo = d_desapilar("pl_tipo_dato")
    while (not d_pilas.get("pl_id_dec").pila_vacia()):
        id = d_desapilar("pl_id_dec")
        print(id)
        find_element_tabla_simbolos(id).set_tipo(tipo)
        
def p_lista_id1(p):
    ''' lista_id : lista_id COMMA ID '''
    reglas_aplicadas.append('''Entro en Regla 53: LI -> LI , ID ''' )
    d_apilar("pl_id_dec",p[3])
    
def p_lista_id2(p):
    ''' lista_id : ID '''
    reglas_aplicadas.append('''Entro en Regla 54: LI -> ID ''' )
    d_apilar("pl_id_dec",p[1])

def p_tipo_dato(p):
    ''' tipo_dato : FLOAT 
    | STRING 
    | INT 
    '''
    reglas_aplicadas.append('''Entro en Regla 55-57: tipo_dato -> FLOAT | STRING | INT''' )
    d_apilar("pl_tipo_dato",p[1])
    

#GRAMATICAS DE LECTURA Y ESCRITURA

def p_sentencia_write1 (p):
    ''' sent_write : WRITE expresion '''
    reglas_aplicadas.append('''Entro en Regla 43: SWRT -> WRITE E ''' )
    crear_terceto("p_write",p[1],f_puntero(d_punteros.get("p_expresion")),"_")
    
def p_sentencia_write2 (p):
    ''' sent_write : WRITE STRINGD '''
    reglas_aplicadas.append('''Entro en Regla 43: SWRT -> WRITE STRINGD ''' )
    crear_terceto("p_write",p[1],"_"+p[2][1:len(p[2])-1],"_")
    

def p_sentencia_read (p):
    ''' sent_read : READ ID '''
    reglas_aplicadas.append('''Entro en Regla 45: SRD -> READ ID ''' )
    crear_terceto("p_read",p[1],p[2],"_")





def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico:\n Token: {}\n Valor: {}\n linea:{}".format(  str(t.type),str(t.value), str(t.lexer.lineno))
        print(resultado)
    else:
        resultado = "Error sintactico {}".format(t)
        print('Inesperado cierre de sentencia')
    resultado_gramatica.append(resultado)



# instanciamos el analizador sistactico
parser = yacc.yacc()

def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()
    if data:
        gram = parser.parse(data)
        if gram:
            resultado_gramatica.append(str(gram))
    else: print("data vacia")

    return resultado_gramatica

if __name__ == '__main__':
    
    inputFile = open(PATH_PRUEBAS + '\Prueba.txt','r')
    outputFile = open(PATH_PRUEBAS + '\Reglas.txt','w')
    outputFileTS = open(PATH_PRUEBAS + '\TS.txt','w')
    outputFileInt = open(PATH_PRUEBAS + '\Intermedia.txt','w')
    
    
    file = ''
    while True:
        linea = inputFile.read() 
        if not linea:
            break   
        file = file + linea
        prueba_sintactica(file)
        for regla in reglas_aplicadas:
            print (regla)
            outputFile.write(regla + "\n")

    outputFile.close()       
    inputFile.close()

    for tb in tablaDeSimbolos:
       outputFileTS.write(str(tb.get_tabla_simbolos()) + "\n")
    
    outputFileTS.close()
    for terceto in l_tercetos:
        outputFileInt.write(terceto.mostrar_terceto()+"\n")


