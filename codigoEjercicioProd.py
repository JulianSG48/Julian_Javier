#
#
# Primero: Definimos las variables en un ámbito global, es decir, un alcance de la varibale en cualquier
#          parte del programa, por lo que se puede "citar" la variable en donde queramos. #

P1 = "Lasagna"
S1 = 20000

P2 = "Pizza"
S2 = 30000

P3 = "Gaseosa"
S3 = 7000

# Segundo: El programa da la bienvenida al usuario, y definimos una función, pues así se podrá invocar la
#          función al final, y luego se ejecutará todo el código cuando deseemos. #

def bien():
    print("Bienvenido(a) a nuestra tienda, a continuación le mostraremos nuestros productos con sus respectivos precios:")

# Segundo: El programa muestra sus productos con sus precios. #

    print("Tenemos una", P1, "con un costo de", S1, "pesos")

    print("Tenemos una", P2, "con un costo de", S2, "pesos")

    print("o tenemos una", P3, "con un costo de", S3, "pesos")

# Tercero: El programa le dice al usuario que elija un o unos productos y la cantidad de dichos productos.

bien()