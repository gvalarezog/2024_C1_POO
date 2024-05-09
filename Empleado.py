class Empleado:

    contador_empleado = 0

    def __init__(self, nombre, sueldo, eliminado=False):
        self.__nombre = nombre
        self.__sueldo = sueldo
        self.__eliminado = eliminado
        # Empleado.contador_empleado = Empleado.contador_empleado + 1
        Empleado.contador_empleado += 1
        self.__id = Empleado.contador_empleado

    # Getters
    @property
    def nombre(self):
        return self.__nombre

    @property
    def sueldo(self):
        return self.__sueldo

    @property
    def eliminado(self):
        return self.__eliminado

    @property
    def id(self):
        return self.__id

    # Setters
    # @id.setter
    # def id(self, id):
    #     self.__id = id

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @sueldo.setter
    def sueldo(self, sueldo):
        self.__sueldo = sueldo

    @eliminado.setter
    def eliminado(self, eliminado):
        self.__eliminado = eliminado

    def __str__(self):
        return f'Empleado: {str(self.__dict__)}'

if __name__ == '__main__':
    e1 = Empleado(nombre='Juan', sueldo=1000, eliminado=False)
    print(e1)
    print(e1.nombre)
    e1.nombre = "Carlos"
    print(e1.nombre)
    # e1.__nombre = 'Maria'
    # print(e1.__nombre)

    e2 = Empleado('Maria', 2000, eliminado=False)
    print(e2)
    e3 = Empleado('Maria', 2000, eliminado=False)
    print(e3)
    e4 = Empleado('Maria', 2000)
    print(e4)
    # e4.id = 4000
    # print(e4)
