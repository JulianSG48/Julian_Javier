#El programa da la bienvenida al usuario
print("""Bienvenido(a) a nuestra tienda, a continuación le mostraremos nuestros productos 
con sus respectivos precios:""")

#Definimos los productos y sus precios, y los imprimimos
producto1 = "pizza"
precio1 = 35000

producto2 = "lasagna"
precio2 = 20000

producto3 = "gaseosa"
precio3 = 7000

print("Tenemos una", producto1, "con un costo de $", precio1, "pesos")

print("tenemos una", producto2, "con un costo de $", precio2, "pesos")

print("o tenemos una", producto3, "con un costo de $", precio3, "pesos")


#Entrada de datos 
nombre_producto = (input ("Ingrese el producto que desea comprar:"))

num_productos = int(input("Ingrese el número de productos que va a comprar: ")) 

precio_producto = float(input("Ingrese el valor de cada producto: "))

if num_productos > 20: descuento = 0.20 
elif num_productos > 10: descuento = 0.10 
elif num_productos > 5: descuento = 0.05 
else: descuento = 0.0 

# Cálculo del valor total 
subtotal = num_productos * precio_producto 

descuento_total = subtotal * descuento 

total_a_pagar = subtotal - descuento_total 

# Salida de resultados 
print(f"\nSubtotal: ${subtotal:.2f}") 
print(f"Descuento aplicado: ${descuento_total:.2f}") 
print(f"Total a pagar: ${total_a_pagar:.2f}") 



