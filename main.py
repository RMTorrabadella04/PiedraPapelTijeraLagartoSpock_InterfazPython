from tkinter import *
import random

inicio=Tk()
inicio.geometry("700x700")
inicio.resizable(0,0)
inicio.title("Inicio")

imagen_fondo = PhotoImage(file="Resources/piedra-papel-tijeras-lagarto-spock.png")

# Crear un Label para la imagen de fondo
label_fondo = Label(inicio, image=imagen_fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Abre la segunda pestaña
def abrirJuego():
    # Withdraw la oculta la pestaña
    inicio.withdraw()

    # Creo nueva ventana para el juego
    juego = Toplevel(inicio)
    juego.geometry("900x700")
    juego.title("PIEDRA - PAPEL - TIJERA - LARGATO - SPOCK")
    juego.resizable(0,0)
    juego.config(bg="lightblue")

    titulo_juego = Label(juego, text="Elige tu opción y ten suerte vas a jugar con la maquina", font=("Calibri", 20, "bold"), fg="#FFFFFF", bg="#1e5db2", relief="solid", padx=20, pady=20,)
    titulo_juego.pack(pady=20)

    # Botones de las opciones
    boton_piedra = Button(juego, text="PIEDRA", width=20, height=8, font=("Calibri", 12, "bold"), fg="#FFFFFF", bg="#1e5db2", relief="solid", command=lambda: comprobador("Piedra"))
    boton_piedra.place(x=175, y=250)

    boton_papel = Button(juego, text="PAPEL", width=20, height=8, font=("Calibri", 12, "bold"), fg="#FFFFFF", bg="#1e5db2", relief="solid", command=lambda: comprobador("Papel"))
    boton_papel.place(x=375, y=250)

    boton_tijera = Button(juego, text="TIJERA", width=20, height=8, font=("Calibri", 12, "bold"), fg="#FFFFFF", bg="#1e5db2", relief="solid", command=lambda: comprobador("Tijera"))
    boton_tijera.place(x=575, y=250)

    boton_lagarto = Button(juego, text="LAGARTO", width=20, height=8, font=("Calibri", 12, "bold"), fg="#FFFFFF", bg="#1e5db2", relief="solid", command=lambda: comprobador("Lagarto"))
    boton_lagarto.place(x=275, y=480)

    boton_spock = Button(juego, text="SPOCK", width=20, height=8, font=("Calibri", 12, "bold"), fg="#FFFFFF", bg="#1e5db2", relief="solid", command=lambda: comprobador("Spock"))
    boton_spock.place(x=475, y=480)

    # En caso de que le des a la X para cerrar la ventana te redirigira a la pantalla de inicio
    juego.protocol("WM_DELETE_WINDOW", lambda: volver_menu(juego))


# Funcion comprobante

def comprobador(opcion):

    # Elige de manera random la opcion de la maquina

    opciones = ['Piedra', 'Papel', 'Tijera', 'Lagarto', 'Spock']
    eleccionRandom = random.choice(opciones)

    reglas = {
        'Piedra': ['Tijera', 'Lagarto'],  # Piedra aplasta Tijeras y Piedra aplasta Lagarto
        'Papel': ['Piedra', 'Spock'],     # Papel envuelve Piedra y Papel desaprueba Spock
        'Tijera': ['Papel', 'Lagarto'],   # Tijeras cortan Papel y Tijeras decapitan Lagarto
        'Lagarto': ['Papel', 'Spock'],    # Lagarto devora Papel y Lagarto envenena Spock
        'Spock': ['Tijera', 'Piedra']     # Spock aplasta Tijeras y Spock desintegra Piedra
    }

    # Comprobar si el usuario ganó, perdió o hubo empate
    if opcion == eleccionRandom:
        resultado = f"¡Empate! Ambos eligieron {opcion}"
        ganador = opcion
    elif eleccionRandom in reglas[opcion]:
        resultado = f"¡Ganaste! {opcion} gana a {eleccionRandom}"
        ganador = opcion
    else:
        resultado = f"Perdiste. {eleccionRandom} gana a {opcion}"
        ganador = eleccionRandom

    ventanaGanador = Toplevel(inicio)
    ventanaGanador.geometry("400x400")
    ventanaGanador.title("Resultado del Juego")
    ventanaGanador.resizable(0,0)

    # Etiqueta que muestra el mensaje
    textoGanador = Label(ventanaGanador, text=resultado, font=("Arial", 12), pady=20)
    textoGanador.pack()

    # Imagen del ganador al ponerlo como variable tenemos que "confirmarlo" para que se muestre correctamente

    imagen = PhotoImage(file=f"Resources/{ganador}.png")

    imagenGanadora = Label(ventanaGanador, image=imagen)
    imagenGanadora.pack(pady=40)

    # La variable imagen se asigna al Label, pero al hacer imagenGanadora.image = imagen
    # garantizamos que la imagen se mantenga en memoria y se pueda mostrar correctamente.

    imagenGanadora.image = imagen



# Vuelve al menu de inicio
def volver_menu(ventana):
    # Destroy cierra la ventana
    ventana.destroy()
    # Deiconify la muestra la ventana la cual antes hemos ocultado
    inicio.deiconify()

# Pantalla de Inicio

# Titulo
titulo = Label(inicio, text="PIEDRA - PAPEL - TIJERA - LARGATO - SPOCK", font=("Calibri", 20, "bold"), fg="#FFFFFF", bg="lightblue", relief="solid", padx=20, pady=20,)
titulo.pack(pady=20)

# Boton que te lleva a la segunda pantalla
boton_abrir = Button(inicio, text="EMPEZAR A JUGAR", command=abrirJuego, font=("Calibri", 20, "bold"), fg="#FFFFFF", bg="lightblue", relief="solid", padx=20, pady=20)
boton_abrir.place(x=210, y=550)

inicio.mainloop()