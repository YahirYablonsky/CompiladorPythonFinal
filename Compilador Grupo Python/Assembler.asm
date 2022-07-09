
include macros2.asm
include number.asm
.MODEL LARGE
.386
.STACK 200h
.DATA

varFloat1                      dd ?                             ;
varFloat2                      dd ?                             ;
varString                      db ?                             ;
varInteger1                    dd ?                             ;
varInteger2                    dd ?                             ;
_0                             dd 0                             ;
_0.95                          dd 0.95                          ;
_1                             dd 1                             ;
_3                             dd 3                             ;
_2                             dd 2                             ;
_10                            dd 10                            ;
_15                            dd 15                            ;
_5                             dd 5                             ;
_Paso_por_el_IF_ANIDADO        db "Paso por el IF ANIDADO"      ;
_Paso_por_el_IF                db "Paso por el IF"              ;
_Paso_por_el_ELSE              db "Paso por el ELSE"            ;

.CODE
MOV EAX,@DATA
MOV DS,EAX
MOV ES,EAX;


Inicio:

Etiq_0:
FLD _0

Etiq_1:
FSTP varInteger1


Etiq_2:
FLD _0

Etiq_3:
FSTP varInteger2


Etiq_4:
FLD _0.95

Etiq_5:
FSTP varFloat1


Etiq_6:
FLD _0

Etiq_7:
FLD _1

Etiq_8:
FLD _3

Etiq_9:
FLD _2

Etiq_10:
FXCH 
FMUL 


Etiq_11:
FXCH 
FADD 


Etiq_12:
FXCH 
FCOM
FSTSW AX
SAHF


Etiq_13:
JL Etiq47

Etiq_14:
FXCH 
FCOM
FSTSW AX
SAHF


Etiq_15:
JG Etiq17

Etiq_16:

Etiq_17:
FLD varInteger1

Etiq_18:
FLD _10

Etiq_19:
FXCH 
FCOM
FSTSW AX
SAHF


Etiq_20:
JNE Etiq53

Etiq_21:
FLD varInteger2

Etiq_22:
FLD _10

Etiq_23:
FXCH 
FCOM
FSTSW AX
SAHF


Etiq_24:
JL Etiq30

Etiq_25:
FLD varInteger2

Etiq_26:
FLD _1

Etiq_27:
FXCH 
FADD 


Etiq_28:
FSTP varInteger2


Etiq_29:
JMP Etiq

Etiq_30:
FLD varInteger2

Etiq_31:
FLD _3

Etiq_32:
FXCH 
FADD 


Etiq_33:
FLD _15

Etiq_34:
FXCH 
FCOM
FSTSW AX
SAHF


Etiq_35:
JL Etiq47

Etiq_36:
FLD varInteger2

Etiq_37:
FLD _5

Etiq_38:
FLD _2

Etiq_39:
FXCH 
FADD 


Etiq_40:
FLD _3

Etiq_41:
FXCH 
FMUL 


Etiq_42:
FXCH 
FCOM
FSTSW AX
SAHF


Etiq_43:
JLE Etiq45

Etiq_44:
mov dx,OFFSET _Paso por el IF ANIDADO
mov ah,9
int 21h

Etiq_45:
mov dx,OFFSET _Paso por el IF
mov ah,9
int 21h

Etiq_46:
JMP Etiq48

Etiq_47:
mov dx,OFFSET _Paso por el ELSE
mov ah,9
int 21h

Etiq_48:
FLD varInteger1

Etiq_49:
FLD _1

Etiq_50:
FXCH 
FADD 


Etiq_51:
FSTP varInteger1


Etiq_52:
JMP Etiq

mov ax,4c00h
int 21h
End