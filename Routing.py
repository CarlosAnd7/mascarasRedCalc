import ipaddress
import math

def calcularDirecciones(direcciones):
    bits_necesarios = math.ceil(math.log2(direcciones + 2))
    direcciones_requeridas = int(math.pow(2, bits_necesarios)) - 2
    return bits_necesarios, direcciones_requeridas
    return i - 1, d

def calcularMascara(x):
    return 32 - x

def ruteoLAN(red, direcciones,b):
    # Convertir la dirección de red a un objeto de red
    red_obj = ipaddress.ip_network(red)

    # Imprimir información de la red
    print("Máscara de red:", red_obj.netmask)
    print("Dirección de red:", red_obj.network_address)

    if(b):
        print("Primera asignable:", red_obj.network_address + 1)
        print("Ultima asignable:", red_obj.broadcast_address - 2)
        print("Gateway:", red_obj.broadcast_address - 1)
    else:
        print("Primera asignable:", red_obj.broadcast_address -2)
        print("Ultima asignable:", red_obj.broadcast_address -1)
    print("Broadcast de red:", red_obj.broadcast_address)

# Solicitar la red base al usuario
red_base_str = input("Ingrese la dirección de red base: ")
red_base = ipaddress.ip_address(red_base_str)

# Solicitar las cantidades al usuario
cantidades = []
while True:
    cantidad_str = input("Ingrese una cantidad de direcciones (o 'fin' para terminar): ")
    if cantidad_str.lower() == "fin":
        break
    cantidades.append(int(cantidad_str))

cantidades.sort(reverse=True)
mascaras = []

contador_redes = 1

for cantidad in cantidades:
    dir, _ = calcularDirecciones(cantidad)
    masc = calcularMascara(dir)
    mascaras.append(masc)
    red = ipaddress.ip_network(str(red_base) + "/" + str(masc), strict=False)
    print(f"Red {contador_redes}: {red}")
    if cantidad == 2:
        ruteoLAN(red, cantidad, False)
    else:
        ruteoLAN(red, cantidad, True)
    print()
    red_base = red.broadcast_address + 1
    contador_redes += 1