import time
import os

def pomodoro_timer(minutos):
    segundos_totales = minutos * 60

    while segundos_totales > 0:
        mins, segs = divmod(segundos_totales, 60)
        
        formato_tiempo = f'{mins:02d}:{segs:02d}'
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("=== MODO ENFOQUE ===")
        print(f"Tiempo restante: {formato_tiempo}")
        print("====================")
        
        time.sleep(1)
        segundos_totales -= 1

    print("\n¡Tiempo cumplido! Es hora de un descanso.")

if __name__ == "__main__":
    try:
        pomodoro_timer(25)
    except KeyboardInterrupt:
        print("\nTemporizador detenido.")