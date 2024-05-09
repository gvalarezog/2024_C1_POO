

class Persona:
    def __init__(self, nombre, cedula, apellido=None, email=''):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._email = email

    def mostrar_persona(self):
        return f'Nombre: {self._nombre}, Apellido: {self._apellido}'

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    def __str__(self):

        return f'Persona: {self.__dict__.__str__()}'


if __name__ == '__main__':
    p1 = Persona(nombre='Luis', apellido='Perez', cedula='0123456789')
    print(p1)
    p2 = Persona(email='mp@mail.com', cedula='1236549870', nombre='Maria', apellido='Paz')
    print(p2)