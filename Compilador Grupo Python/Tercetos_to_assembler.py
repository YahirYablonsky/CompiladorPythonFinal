import os
from Sintactico import tablaDeSimbolos
from Clases import Pila
from Clases import Terceto

pila_operandos = Pila()


PATH_PRUEBAS = os.path.dirname(os.path.abspath(__file__))
def genera_assembler(l_tercetos):
    outputAssembler = open(PATH_PRUEBAS + '\Assembler.asm','w')
    outputAssembler.write("\ninclude macros2.asm")
    outputAssembler.write("\ninclude number.asm")

    outputAssembler.write("\n.MODEL LARGE");
    outputAssembler.write("\n.386");
    outputAssembler.write("\n.STACK 200h");
    outputAssembler.write("\n.DATA");

    
    for registro in tablaDeSimbolos:
        if(registro.get_nombre() == "Nombre"):
            outputAssembler.write("\n")
        
        elif(registro.get_tipo()=="STRING"):
             outputAssembler.write(str("\n{:<30} db {:<30};".format(registro.get_nombre(),registro.get_valor())))  
        else:
            outputAssembler.write(str("\n{:<30} dd {:<30};".format(registro.get_nombre(),registro.get_valor())))  

    outputAssembler.write("\n\n.CODE");
    outputAssembler.write("\nMOV EAX,@DATA");
    outputAssembler.write("\nMOV DS,EAX");
    outputAssembler.write("\nMOV ES,EAX;\n\n");
    
    outputAssembler.write("\nInicio:\n");
    
    for terceto in l_tercetos:
        outputAssembler.write("\nEtiq_"+str(terceto.get_nro_terceto())+":\n")
        
        if((terceto.get_valor2() == "_") and (terceto.get_valor2() == "_")):
            outputAssembler.write("FLD "+str(terceto.get_valor1())+"\n")

        if(terceto.get_valor1() == ":="):
            outputAssembler.write("FSTP "+str(terceto.get_valor2())+"\n\n")

        if(terceto.get_valor1() == "+"):
            outputAssembler.write("FXCH \n")
            outputAssembler.write("FADD \n\n")

        if(terceto.get_valor1() == "-"):
            outputAssembler.write("FXCH \n")
            outputAssembler.write("FSUB \n\n")

        if(terceto.get_valor1() == "*"):
            outputAssembler.write("FXCH \n")
            outputAssembler.write("FMUL \n\n") 

        if(terceto.get_valor1() == "/"):    
            outputAssembler.write("FXCH \n")
            outputAssembler.write("FDIV \n\n")  

        if(terceto.get_valor1() == "CMP"):
            outputAssembler.write("FXCH \n")
            outputAssembler.write("FCOM\n")
            outputAssembler.write("FSTSW AX\n")
            outputAssembler.write("SAHF\n\n") 
           
       

        if(terceto.get_valor1() == "BNE"):
           outputAssembler.write("JNE Etiq"+str(terceto.get_valor2_num())+"\n")
        if(terceto.get_valor1() == "BEQ"):
            outputAssembler.write("JE Etiq"+str(terceto.get_valor2_num())+"\n")
        if(terceto.get_valor1() == "BLE"):
            outputAssembler.write("JG Etiq"+str(terceto.get_valor2_num())+"\n")
        if(terceto.get_valor1() == "BGE"):
            outputAssembler.write("JL Etiq"+str(terceto.get_valor2_num())+"\n")
        if(terceto.get_valor1() == "BLT"):
            outputAssembler.write("JGE Etiq"+str(terceto.get_valor2_num())+"\n")
        if(terceto.get_valor1() == "BGT"):
            outputAssembler.write("JLE Etiq"+str(terceto.get_valor2_num())+"\n")
        if(terceto.get_valor1() == "BI"):
            outputAssembler.write("JMP Etiq"+str(terceto.get_valor2_num())+"\n")

        if(terceto.get_valor1() == 'write'):
            outputAssembler.write("mov dx,OFFSET "+terceto.get_valor2()+"\n")
            outputAssembler.write("mov ah,9\n")
            outputAssembler.write("int 21h\n")


    
    outputAssembler.write("\nmov ax,4c00h")
    outputAssembler.write("\nint 21h")
    outputAssembler.write("\nEnd")
        