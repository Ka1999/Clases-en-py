class Estudiante:
    def __init__(self,
                 nombre: str,
                 edad: int,
                 grado: int,
                 riesgo_desercion: str = "Alto",
                 asistencias: int = 0,
                 porcentaje_asistencia : float = 0):
        self.nombre: str = nombre
        self.edad: int = edad
        self.grado: int  = grado
        self.riesgo_desercion: str = riesgo_desercion
        self.asistencias: int = asistencias
        self.porcentaje_asistencia = porcentaje_asistencia
    
    def registrar_asistencia(self, total_asistencias):
        self.asistencias = total_asistencias
    
    def cambiar_riesgo(self, nuevo_riesgo):
        self.riesgo_desercion = nuevo_riesgo

    def mostrar_informacion(self):
        print("Nombre", self.nombre)
        print("Edad", self.edad)
        print("Grado", self.grado)
        print("Riesgo de deserción", self.riesgo_desercion)
        print("Asistencias", self.asistencias)
        print("Porcentaje de asistencia:", self.porcentaje_asistencia)

    def actualizar_indicador(self, total_clases):
        self.porcentaje_asistencia = (self.asistencias/total_clases) * 100

variable_estudiante = Estudiante(nombre="Andres<3",
                                 edad=27,
                                 grado=10,
                                 riesgo_desercion="Bajo",
                                 asistencias = 15)
variable_estudiante.actualizar_indicador(58)

variable_estudiante2 = Estudiante(nombre="Fly<3",
                                 edad=1,
                                 grado=5,
                                 asistencias=15)

variable_estudiante.mostrar_informacion()

    