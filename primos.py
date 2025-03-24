from tkinter import * # Importar librería de ventanas
from tkinter.ttk import Label, Entry, Button # Importar objetos de ventanas
import tkinter.messagebox # Importar message boxes

window = Tk() # Inicializar librería
window.geometry("500x300") # Dimensionar a 500x300 pixeles
window.resizable(False, False) # Definir como ventana no redimensionable
window.title("Comprobar números primos") # Definir título
window.iconbitmap('icono.ico') # Designar ícono
bg = PhotoImage(file = "imagen.png") # Designar imagen de fondo
divisores = [] # Designar lista de divisores

imagen = Label(window, image = bg) # Designar imagen de fondo como label
imagen.place(x = 0, y = 0) # Poner imagen de fondo

label1 = Label(window, font=("Segoe UI", 25), text="Insertar Número") # Texto de insertar número
label1.pack() # Añadir texto de insertar número a la ventana

label2 = Label(window, font=("Segoe UI", 25), text="", wraplength=300, justify="center") # Texto de resultado de calculación

entry1 = Entry(window, font=("Segoe UI", 25)) # Entrada de texto
entry1.pack() # Añadir entrada de texto a la ventana

def esPrimo(): #Comprobar si es primo, iteraciones iniciales 2
    divisores = [] # Vaciar lista de divisores
    try: # Probar código
        if(int(entry1.get()) >= 10000): # Si el número es mayor o igual a 10,000
            aviso = tkinter.messagebox.askokcancel(title="Advertencia", message="Operar con números grandes puede tardar bastante considerando la velocidad del equipo, ¿Continuar de todas formas?") # Avisar sobre operaciones en números grandes
            if(not aviso): # Si se dice que no
                return # Salir de la función
        label2.config(text="Calculando...")
        for i in range(2, int(entry1.get())): # Por cada iteración empezando desde 2 hasta el número ingresado
            if(int(entry1.get()) % i == 0): # Comprobar si el número al dividirse por la iteración da resto 0
                divisores.append(i) #Si da resto 0 añadir número de iteración a la lista de divisores
                
        if(len(divisores) >= 1): # Si hay 1 o más divisores 
            label2.config(text="El número no es primo, tiene " + str(len(divisores)) + " divisores") # Mostrar que el número no es primo y su cantidad de divisores
        else: # Si no
            label2.config(text="El número es primo") # Mostrar que el número es primo
    except:
        label2.config(text="Por favor insertar números válidos de menos de 64 caracteres") # Avisar de insertar números válidos
        divisores = [] # Vaciar lista de divisores

button1 = Button(window, text="Calcular", command=esPrimo) # Botón de calcular que utiliza la función esPrimo
button1.pack() # Añadir botón a la ventana
label2.pack() # Añadir texto de resultado a la ventana

window.mainloop() # Mostrar ventana