import datetime  # Importado para la fecha del reporte final

print("=============================================")
print("   SISTEMA DE VENTAS - TECHZONE STORE        ")
print("=============================================\n")

# ------------------------------------------
# PARTE 1 - ACCESO AL SISTEMA
# ------------------------------------------
print("--- INICIO DE SESIÓN ---")
usuario_input = input("Usuario: ")
contrasena_input = input("Contraseña: ")

# Validación de credenciales requeridas
if usuario_input == "Admin" and contrasena_input == "Thriller1982":
    print("\nAcceso concedido. Bienvenido al sistema.\n")
    print("---------------------------------------------")
    
    # ------------------------------------------
    # PARTE 2 - REGISTRO DE PRODUCTOS
    # ------------------------------------------
    print("--- REGISTRO DE PRODUCTOS ---")
    nombre_producto = input("Nombre del producto: ")
    precio_producto = float(input("Precio del producto (S/): "))
    cantidad_comprada = int(input("Cantidad comprada: "))
    
    # Cálculos matemáticos base
    subtotal = precio_producto * cantidad_comprada
    igv = subtotal * 0.18
    
    # Aplicación de la fórmula: Total = (Precio x Cantidad) + (Precio x Cantidad x 0.18)
    total_a_pagar = subtotal + igv
    
    # ------------------------------------------
    # PARTE 3 - DESCUENTOS AUTOMÁTICOS
    # ------------------------------------------
    # Estructura condicional compuesta para evaluar el monto total
    if total_a_pagar > 500:
        porcentaje_desc = 0.20
        descuento_aplicado = total_a_pagar * porcentaje_desc
    elif total_a_pagar > 300:
        porcentaje_desc = 0.10
        descuento_aplicado = total_a_pagar * porcentaje_desc
    else:
        porcentaje_desc = 0.0
        descuento_aplicado = 0.0
        
    total_final = total_a_pagar - descuento_aplicado
    
    # Resultados de los descuentos de la Parte 3
    print("\n--- PROCESANDO DESCUENTOS ---")
    print(f"Descuento aplicado ({int(porcentaje_desc * 100)}%): S/ {descuento_aplicado:.2f}")
    print(f"Total final: S/ {total_final:.2f}\n")
    print("---------------------------------------------")

    # ------------------------------------------
    # PARTE 4 - REPORTE FINAL
    # ------------------------------------------
    print("--- REPORTE FINAL ---")
    print(f"• Nombre del producto: {nombre_producto}")
    print(f"• Cantidad: {cantidad_comprada}")
    print(f"• Total pagado: S/ {total_final:.2f}")
    print(f"• Descuento aplicado: S/ {descuento_aplicado:.2f}")
    
    # Fecha del registro
    fecha_actual = datetime.date.today().strftime("%d/%m/%Y")
    print(f"• Fecha del registro:  {fecha_actual}")
    print("*****************************************************************")

else:
    # Mensaje en caso las credenciales de la Parte 1 sean incorrectas
    print("\n[X] Error: Usuario o contraseña incorrectos. El sistema se cerrará.")