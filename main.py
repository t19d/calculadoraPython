# encoding: utf-8
import funciones as f

menu = f.imprimirMenu()
repetir = True
while repetir:
    if (menu > 5):
        print "ERROR: SELECCIONE UN NÚMERO ENTRE 1 Y 5"
        menu = f.imprimirMenu()
    elif (menu < 5):
        f.operar(menu)
        if (f.preguntar()):
            menu = f.imprimirMenu()
        else:
            repetir = False
    else:
        repetir = False
