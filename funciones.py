# encoding: utf-8

def imprimirMenu():
    return input ("**********************\n1.SUMAR\n2.RESTAR\n3.MULTIPLICAR\n4.DIVIDIR\n5.SALIR\n**********************\nSELECCIONE UNA OPCIÓN: ")


def operar(n):
    if (n == 1):
        s1 = input ("(primer valor) ")
        s2 = input ("(segundo valor) ")
        print s1, "+", s2, "=", s1+s2
    if (n == 2):
        s1 = input ("(primer valor) ")
        s2 = input ("(segundo valor) ")
        print s1, "-", s2, "=", s1-s2
    if (n == 3):
        s1 = input ("(primer valor) ")
        s2 = input ("(segundo valor) ")
        print s1, "*", s2, "=", s1*s2
    if (n == 4):
        s1 = input ("(primer valor) ")
        s2 = input ("(segundo valor) ")
        if (s2 == 0):
            print "ERROR: NO SE PUEDE DIVIDIR ENTRE 0"
        else:
            print s1, "/", s2, "=", s1/s2


def preguntar():
    r = raw_input ("¿DESEA CONTINUAR OPERANDO? (S/N): ")
    continuar = False
    if (r.upper() == "S"):
        continuar = True
    return continuar
