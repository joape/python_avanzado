"""
Crear una clase User
  - atributos: username, password
  - metodo: login
Crear las siguientes clases que hereden de User:
    - Staff (Profesional de la salud)
    - Patient (Paciente)
"""


class User:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def login(self) -> None:
        print(f"Bienvenido al sistema {self.username}")


class Staff(User):
    def login(self) -> None:
        print("[staff] ", end="")
        super().login()


class Patient(User):
    def login(self) -> None:
        print("[patient] ", end="")
        super().login()


def main():
    staff = Staff("Dr. House", "1234")
    staff.login()

    patient = Patient("Tere", "4567")
    patient.login()


if __name__ == "__main__":
    main()
