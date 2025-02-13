import requests
import time


def obtener_datos_clima (ciudad):

    url = f"http://api.weatherapi.com/v1/current.json?key=eee223ab500d419ba48235019241006&q={ciudad}"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    json = response.json()
    print (json["current"]["temp_c"], "°C")
    print (json["current"]["condition"]["text"])

    #return response.text
def obtener_ubicacion (ciudad):

    url = f"http://api.weatherapi.com/v1/current.json?key=eee223ab500d419ba48235019241006&q={ciudad}"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    json = response.json()
    print ("del pais:" + json["location"]["country"])
    print ("del departamento/region:" + json["location"]["region"])
    print (json["location"]["tz_id"])



def obtener_datos_hora (ciudad):
    url = f"http://api.weatherapi.com/v1/current.json?key=eee223ab500d419ba48235019241006&q={ciudad}"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    json = response.json()
    print ( "El día y hora actuales son:" + json["location"]["localtime"])


def obtener_datos_polucion(ciudad):
    url = f"http://api.weatherapi.com/v1/current.json?key=eee223ab500d419ba48235019241006&q={ciudad}"
    response = requests.get(url)
    data = response.json()
    wind_degree = data['current']['wind_degree']
    print(f"La tasa de polución es: {wind_degree}" + "SO2")

    if wind_degree < 20:
        print("El aire es de una excelente calidad")
    elif 21 <= wind_degree < 80:
        print("El aire es de buena calidad y se encuentra mayormente descontaminado")
    elif 81 <= wind_degree < 250:
        print("El aire es de mala calidad, es urgente su limpieza")
    else:
        print("El aire es de muy mala calidad, puede llegar a ser dañino y es muy urgente su descontaminación")


def opcion_no_valida():
    print("Opción no válida. Intenta de nuevo.")

def menu():

    print("1. Consultar Clima")
    print("2. Consultar hora y día")
    print("3. Consultar polucion")
    print("4. Consultar la ubicacion de la ciudad")
    print("5. cambiar ciudad")
    print("6. Salir")

#def seleccion_ciudad():
    #ciudad = input("digite la ciudad:")

def main():
    ciudad = input("digite la ciudad: ")
    
    while True:
        print(f'''ciudad actual:{ciudad}

''')
        
        menu()





        opcion = input("Selecciona una opción: ")


        if opcion == '1':
              obtener_datos_clima(ciudad)
              time.sleep(2)
              print('''

                ''')

        elif opcion == '2':
              obtener_datos_hora(ciudad)
              time.sleep(2)
              print('''

                ''')


        elif opcion == '3':

                obtener_datos_polucion(ciudad)
                time.sleep(2)
                print('''

                ''')


        elif opcion == '4':
                obtener_ubicacion(ciudad)
                time.sleep(2)
                print('''

                ''')



        elif opcion == '5':

                main()
                

        elif opcion == '6':
            print("Saliendo del programa...")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
            time.sleep(1)
            print('''

                ''')
if __name__ == "__main__":
    main()