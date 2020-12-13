#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2020]:


import random
from IPython.display import clear_output


# In[2021]:


def verificar_letra(letra):
    global letras_introducidas
    global puntaje
    global errores
    global num_letras_desifradas
    global new_hide_word
    global letras_descubiertas
    global letras_mostrar
    global letra_ya_introducida
    
    letras_introducidas.append(letra)
    if letra in word:
        if letra in letras_mostrar:
            letra_ya_introducida = True
        else:
            puntaje += 20
            num_letras_desifradas += 1
            letras_descubiertas.append(letra)
            letras_mostrar.append(letra)
    else:
        errores += 1
        # Nuevo commit
        if puntaje > 0:
            puntaje -= 10


# In[2022]:


def actualizar_palabra():
    global completar_palabra
    
    completar_palabra = False
    hide_word = ""
    
    for letter in word:
        if letter in letras_mostrar:
            hide_word += letter
        else:
            hide_word += "-"
            completar_palabra = True
            
            
    return (hide_word)
            
    


# In[2023]:



def mostrar_tablero(palabra, letras_introducidas, errores, puntaje):
    
    global letra_ya_introducida
    
    if True:
        clear_output()
        
    
    print("Palabra a adivinar: " + new_hide_word)
    print("Letras ingresadas: " + str(letras_introducidas))
    print("errores: " + str(errores))
    print("puntaje: " + str(puntaje))
    
    if letra_ya_introducida:
            print("\nEsta letra ya había sido descubierta")
    
    
    print(index_name)
    letra_ya_introducida = False
    


# In[2024]:



def core_juego():
    global ind_word
    global letras_introducidas
    global puntaje
    global errores
    global num_letras_desifradas
    global lenght_word
    global new_hide_word
    global completar_palabra
    global letras_mostrar
    
    #print("Que comience el juego !")
    
    #if new_player:
        #print("Nuevo jugador")
        
    #if registered_player:
        #print("Ya había jugado")
    
    new_hide_word = actualizar_palabra()
    
    while errores < 3 and completar_palabra:
        mostrar_tablero(new_hide_word, letras_introducidas, errores, puntaje)
        letra_elegida = input("Eljia una letra: ")[0]
        verificar_letra(letra_elegida)
        new_hide_word = actualizar_palabra()
        
    if completar_palabra == False:
        print("Has ganado :D  La palabra es: " + word )
    elif errores >= 3:
        print("Has perdido :(  La palabra era: " + word )
        
    completar_palabra = True
    errores = 0
    
    
    marcador[index_name][ind_word] += puntaje
    


# In[2025]:


def remplazar_nombre(name):
    global xUser
    global nombres
    global index_name
    
    if xUser <= 3:
        nombres[xUser] = name
        index_name = xUser
        xUser += 1
    else:
        xUser = 0
        nombres[xUser] = name
        index_name = xUser
        xUser += 1
        


# In[2026]:


def borrar_registo_nombre(index_name):
    global marcador
    
    x = 0
    for word in palabras:
        marcador[index_name][x] = 0
        x += 1


# In[2027]:


def jugar():
    global index_name
    global new_player
    global registered_player
    y = 0
    nuevo = True
    
    name = input("Ingrese su nombre: ")
    for nam in nombres:
        if nam == name:
            index_name = y
            nuevo = False
            
        y+=1
    y = 0
    
    if nuevo:
        new_player = True
        remplazar_nombre(name)
        borrar_registo_nombre(index_name)
    else:
        registered_player = True

    core_juego()


# In[2028]:


# agregar nuevas palabras


# In[2029]:


def borrar_registo_palabra(index_word):
    global marcador
    
    x = 0
    for name in nombres:
        marcador[x][index_word] = 0
        x += 1


# In[2030]:


def cambiar_palabras():
    clear_output()
    x = 0
    global palabras
    show_error = True
    
    print(palabras)
    cuanto_modificar = input("Si quieres cambiar una palabra escribe: U \nSi quieres cambiar todas escribe: T ")
    if cuanto_modificar == "U":
        palabra_cambiar = input("Escriba la palabra que desea cambiar: ")
        for palabra in palabras:
            if palabra_cambiar == palabra:
                palabras[x] = input("Escriba la nueva palabra: ")
                borrar_registo_palabra(x)
                show_error = False
                
                # Nuevo commit
                nuevo_cambio = input("Si deaseas cambiar otra palabra escribe: N \nSi deseas volver al menú solo da Enter")
                if nuevo_cambio == "N":
                    cambiar_palabras()
                    
            x+=1
        if show_error:
            print("ERROR: No está esa palabra en la lista")
    elif cuanto_modificar == "T":
        palabras[0] = input("Escriba la nueva palabra 1: ")
        palabras[1] = input("Escriba la nueva palabra 2: ")
        palabras[2] = input("Escriba la nueva palabra 3: ")
        palabras[3] = input("Escriba la nueva palabra 4: ")
        
        borrar_registo_palabra(0)
        borrar_registo_palabra(1)
        borrar_registo_palabra(2)
        borrar_registo_palabra(3)
        
    print(palabras)
    
    


# In[2031]:


def nuevas_palabras():
        intento_contraseña = input("Ingresa la contraseña: ")
        if intento_contraseña == contraseña:
            cambiar_palabras()
        else:
            while True:
                segundo_intento = input("La contraseña es incorrecta, intenta de nuevo, o si deseas volver al Menú solo preciona Enter")
                if segundo_intento == contraseña:
                    cambiar_palabras()
                    break
                elif segundo_intento == "":
                    break      
                    


# In[2032]:


# Marcador


# In[2033]:


def ver_puntajes(maker):
    clear_output()
    
    print("MARCADOR\n")
    print("NOMBRE        PALABRA 1     PALABRA 2      PALABRA 3      PALABRA 4       TOTAL")
    print("________________________________________________________________________________________")
    print(nombres[0] + "\t|" + str(maker[0][0]) + "\t\t|" + str(maker[0][1]) + "\t\t|" + str(maker[0][2]) + "\t\t|" + str(maker[0][3]) + "\t\t|" + str(sum(maker[0])))
    print(nombres[1] + "\t|" + str(maker[1][0]) + "\t\t|" + str(maker[1][1]) + "\t\t|" + str(maker[1][2]) + "\t\t|" + str(maker[1][3]) + "\t\t|" + str(sum(maker[1])))
    print(nombres[2] + "\t|" + str(maker[2][0]) + "\t\t|" + str(maker[2][1]) + "\t\t|" + str(maker[2][2]) + "\t\t|" + str(maker[2][3]) + "\t\t|" + str(sum(maker[2])))
    print(nombres[3] + "\t|" + str(maker[3][0]) + "\t\t|" + str(maker[3][1]) + "\t\t|" + str(maker[3][2]) + "\t\t|" + str(maker[3][3]) + "\t\t|" + str(sum(maker[3])))
    
    


# In[2034]:


# Finalizar


# In[2035]:


def salir():
    
    global play
    play = False


# In[ ]:





# In[2036]:


def generar_letras_iniciales(num):
    global abc
    letras_init = []
    random.shuffle(abc)
    
    for x in range(0, num):
        letras_init.append(abc[x])
    return letras_init
        


# In[ ]:





# In[ ]:


# Main
nombres = ["", "", "", ""]

palabras = ["botella", "solidaridad", "matriz", "mochila"]

contraseña = "1234"
marcador = [
 [0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0]]

play = True
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

new_hide_word = ""

ind_word = 0
word = ""
letras_iniciales = []
letras_descubiertas = []
letras_mostrar = []
letras_introducidas = []
errores = 0
puntaje = 0
num_letras_desifradas = 0
completar_palabra = True
new_hide_word = ""


xUser = 0
letra_ya_introducida = False


def main():
    clear_output()
    global new_hide_word
    global word
    global lenght_word
    global letras_iniciales
    global letras_descubiertas
    global letras_mostrar
    global letras_introducidas
    global letra_ya_introducida
    global errores
    global puntaje
    global num_letras_desifradas
    global completar_palabra
    global index_name
    global ind_word
    global new_player
    global registered_player
    
    
    while True:
        while play:
            
            ind_word = random.randint(0, 3)
            word = palabras[ind_word]
            letras_introducidas = []
            letra_ya_introducida = False
            letras_iniciales = generar_letras_iniciales(10)
            
            letras_descubiertas = []
            letras_mostrar = letras_iniciales + letras_descubiertas
            errores = 0
            puntaje = 0
            num_letras_desifradas = 0
            completar_palabra = True
            index_name = 0
            #new_player = False
            #registered_player = False
            
            
            menu_choise = int(input("MENU\nIngrese el número: \n1) Para jugar \n2) Para agregar o cambiar palabras \n3) Para ver puntajes  \n4) Para Salir\n "))

            if(menu_choise == 1):
                jugar()
            if(menu_choise == 2):
                nuevas_palabras()
            if(menu_choise == 3):
                ver_puntajes(marcador)
            if(menu_choise == 4):
                salir()
                
        print("Gracias por jugar")
        break
main()


# In[ ]:





# In[ ]:




