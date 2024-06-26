from datetime import datetime, timedelta
import random
import os
# creamos la clase nodo 
class Nodo:
    def __init__(self, alumno=None):
        self.alumno = alumno
        self.siguiente = None
        self.anterior = None
#creamos la lista doblemente enlazada
class ListaDoblementeEnlazada:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def esta_vacia(self):
        return self.head is None
    #alumno agregado a un nodo
    def agregar_alumno(self, alumno):
        nuevo_nodo = Nodo(alumno)
        if self.head is None:
            self.head = self.tail = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.tail
            self.tail.siguiente = nuevo_nodo
            self.tail = nuevo_nodo
    #utilizamos una lista como ejemplo
    def lista_ejemplo(self, cantidad):
        for _ in range(cantidad):
            nombre = Alumno.generar_nombre()
            dni = Alumno.generar_dni()
            fecha_ingreso = Alumno.generar_fecha_ingreso()
            carrera = Alumno.generar_carrera()
            nuevo_alumno = Alumno(nombre, dni, fecha_ingreso, carrera)
            self.agregar_alumno(nuevo_alumno)
    #sobrecargamos el metodo iter
    def __iter__(self):
        return ListaIterador(self.head)
    # metodo de ordenacion
    def ordenar_por_fecha_ingreso(self):
        if self.head is None:
            return
        
        actual = self.head.siguiente
        
        while actual is not None:
            alumno_actual = actual.alumno
            fecha_actual = alumno_actual.datos['FechaIngreso']
            nodo_anterior = actual.anterior
            
            while nodo_anterior is not None and nodo_anterior.alumno.datos['FechaIngreso'] > fecha_actual:
                nodo_anterior.siguiente.alumno, nodo_anterior.alumno = nodo_anterior.alumno, nodo_anterior.siguiente.alumno
                nodo_anterior = nodo_anterior.anterior
            
            actual = actual.siguiente
    #creamos directorio y archivo para guardar datos
    def crear_directorio_y_archivo():
        directorio = 'directorio_alumnos'
        archivo_alumnos = 'alumnos.txt'
        
        try:
            # Crear directorio si no existe
            if not os.path.exists(directorio):
                os.makedirs(directorio)
                print(f'Se ha creado el directorio "{directorio}"')

            # Crear y escribir lista de alumnos en el archivo
            with open(os.path.join(directorio, archivo_alumnos), 'w') as file:
                alumnos = ['Juan', 'María', 'Carlos', 'Ana']
                for alumno in alumnos:
                    file.write(f'{alumno}\n')
                print(f'Se ha creado el archivo "{archivo_alumnos}" en "{directorio}"')

        except OSError as e:
            print(f'Error al crear el directorio o archivo: {e}')

    # metodo para mover el directorio y borrar datos
    def mover_directorio_y_borrar():
        directorio_origen = 'directorio_alumnos'
        directorio_destino = 'nueva_ruta'

        try:
            # Mover directorio a nueva ruta
            os.rename(directorio_origen, directorio_destino)
            print(f'Se ha movido el directorio "{directorio_origen}" a "{directorio_destino}"')

            # Borrar archivo y directorio
            archivo_alumnos = os.path.join(directorio_destino, 'alumnos.txt')
            os.remove(archivo_alumnos)
            os.rmdir(directorio_destino)
            print(f'Se ha borrado el archivo "{archivo_alumnos}" y el directorio "{directorio_destino}"')

        except OSError as e:
            print(f'Error al mover o borrar el directorio/archivo: {e}')

#lista encargada de recorrer la lista
class ListaIterador:
    def __init__(self, nodo):
        self.nodo_actual = nodo
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.nodo_actual is None:
            raise StopIteration
        alumno = self.nodo_actual.alumno
        self.nodo_actual = self.nodo_actual.siguiente
        return alumno
#creamos la clase Fecha inicializada con la fecha de hoy 1.1   
class Fecha:
    def __init__(self, dia=None, mes=None, anio=None):
        if dia is None or mes is None or anio is None:
            # Si no se proporcionan los parámetros, inicializamos con la fecha de hoy
            hoy = datetime.now()
            self.dia = hoy.day
            self.mes = hoy.month
            self.anio = hoy.year
        else:
            self.dia = dia
            self.mes = mes
            self.anio = anio
    #sobrecarga de metodo str    
    def __str__(self):
        return f"{self.dia:02}/{self.mes:02}/{self.anio}"
    #sobrecarga de metodo eq
    def __eq__(self, otra_fecha):
        return (self.dia == otra_fecha.dia and
                self.mes == otra_fecha.mes and
                self.anio == otra_fecha.anio)
    #sobrecarga de metodo add 
    def __add__(self, dias):
        nueva_fecha = datetime(self.anio, self.mes, self.dia) + timedelta(days=dias)
        return Fecha(nueva_fecha.day, nueva_fecha.month, nueva_fecha.year)
    # metodo para calcular cuanto tiempo hay entre dos fechas
    def calcular_dif_fecha(self, otra_fecha):
        fecha1 = datetime(self.anio, self.mes, self.dia)
        fecha2 = datetime(otra_fecha.anio, otra_fecha.mes, otra_fecha.dia)
        diferencia = fecha1 - fecha2
        return abs(diferencia.days)
#creamos la clase Alumno que contiene sus datos en diccionario    
class Alumno:
    def __init__(self, nombre, dni, fecha_ingreso, carrera):
        self.datos = {
            "Nombre": nombre,
            "DNI": dni,
            "FechaIngreso": fecha_ingreso,
            "Carrera": carrera
        }
    #sobrecarga de metodo str
    def __str__(self):
        return f"Nombre: {self.datos['Nombre']}, DNI: {self.datos['DNI']}, " \
               f"Fecha de Ingreso: {self.datos['FechaIngreso']}, Carrera: {self.datos['Carrera']}"
    #sobrecarga de metodo eq
    def __eq__(self, otro_alumno):
        return self.datos == otro_alumno.datos
    #utilizamos una funcion para cambiar datos del alumno
    def cambiar_datos(self, nombre=None, dni=None, fecha_ingreso=None, carrera=None):
        if nombre:
            self.datos['Nombre'] = nombre
        if dni:
            self.datos['DNI'] = dni
        if fecha_ingreso:
            self.datos['FechaIngreso'] = fecha_ingreso
        if carrera:
            self.datos['Carrera'] = carrera
    #calculamos la antiguedad del alumno en la carrera
    def antiguedad(self):
        fecha_actual = datetime.now()
        fecha_ingreso = self.datos['FechaIngreso']
        tiempoCarrera = fecha_actual - fecha_ingreso
        return tiempoCarrera.days // 365  # Calculamos la antigüedad en años
    #utilizamos el metodo staticmethod para que no dependan de una clase
    @staticmethod
    def generar_nombre():
        nombres = ["Pedro", "Jose", "Matias", "Julieta", "Mariano"]
        return random.choice(nombres)

    @staticmethod
    def generar_dni():
        return random.randint(10000000, 99999999)
    #devuelve fecha aleatoria de ingreso
    @staticmethod
    def generar_fecha_ingreso():
        start_date = datetime.now() - timedelta(days=365*4)  # Fecha hace máximo 4 años
        end_date = datetime.now()
        return start_date + (end_date - start_date) * random.random()
    #esta funcion devolvera aleatoriamente una carrera
    @staticmethod
    def generar_carrera():
        carreras = ["Programacion", "Medicina", "Derecho", "Administración", "Psicología"]
        return random.choice(carreras)
