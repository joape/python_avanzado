"""
Crear una clase User
  - atributos: username, password
  - metodo: login
Crear las siguientes clases que hereden de User:
    - Staff (Profesional de la salud)
    - Patient (Paciente)
"""

from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    @abstractmethod
    def login(self) -> None:
        """Cada subclase debe implementar su propio login"""
        pass


class Staff(User):
    def login(self) -> None:
        print(f"Bienvenido profesional de la salud {self.username}")


class Patient(User):
    def login(self) -> None:
        print(f"Bienvenido paciente {self.username}")


def main():
    staff = Staff("Dr. House", "1234")
    staff.login()

    patient = Patient("Tere", "4567")
    patient.login()


if __name__ == "__main__":
    main()
