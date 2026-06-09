import random

def jugar():
    opciones = ["piedra", "papel", "tijera"]
    print("---¿No sabes?じゃんけんをしよう! (づ｡◕‿‿◕｡)づ ---")

    while True:
        print("\nElige una opción: piedra, papel, tijera (o escribe 'salir' (༎ຶ⌑༎ຶ) )")
        usuario = input("Tu elección: ").lower().strip()

        if usuario == "salir":
            print("¡ありがとう, vuelve a jugar conmigo, 先輩 ＼(*T▽T*)／")
            break

        if usuario not in opciones:
            print("¡Esa opción no es válida!, ばか (ノಠ益ಠ)ノ彡┻━┻")
            continue

        computadora = random.choice(opciones)
        print(f"Acabo de elegir: {computadora}")

        if usuario == computadora:
            print("¡Es un empate!")
        elif (usuario == "piedra" and computadora == "tijera") or \
             (usuario == "papel" and computadora == "piedra") or \
             (usuario == "tijera" and computadora == "papel"):
            print("¡Ganaste!, 愛する人 (ʃƪ＾3＾)♥")
        else:
            print("負けた... ( ; _ ; )")

jugar()
print("---Gracias por jugar、先輩 (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧---")