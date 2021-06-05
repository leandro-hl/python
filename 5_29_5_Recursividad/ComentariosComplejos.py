# Este es un archivo que solo tiene comentarios simples para el ejercicio 6-1
import datetime # Importo un modulo
# Dejo una linea en blanco
for _ in range(10): # Tiene un ciclo random
    texto = input("Ingrese un texto: ") # Solicito que se ingrese un texto
    print(str(datetime.datetime.now())) # Muestro la fecha y hora actual
    print(f'Se (ingreso)# el texto:\n# {texto}') # Muestro el (texto) ingresado con un '#' antes
    # Fin del archivo