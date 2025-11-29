"""
Crear una clase User
  - atributos: username, password
  - metodo: login
Crear las siguientes clases que hereden de User:
    - Staff (Profesional de la salud)
    - Pacient (Paciente)
"""

class User:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
    
    def login(self):
        pass  # Método que será sobrescrito en las clases derivadas


class Staff(User):
    def __init__(self, username: str, password: str, especialidad: str) -> None:
     
        self.username = username
        self.password = password
        self.especialidad = especialidad
    
    def login(self):
        print(f"¡Bienvenido Staff {self.username}! - Especialidad: {self.especialidad}")

class Pacient(User):   
    def __init__(self, username: str, password: str, historial_medico: str) -> None:
       
        self.username = username
        self.password = password
        self.historial_medico = historial_medico
    
    def login(self):
        print(f"¡Bienvenido Paciente {self.username}! - Tu historial está disponible")

def main():
    # Creo instancias
    staff_1 = Staff("Dr_Garcia", "seg123", "Cardiología")
    staff_2 = Staff("Dra_Lopez", "seg456", "Pediatría")
    
    paciente_1 = Pacient("juan_perez", "pass123", "Sin alergias conocidas")
    paciente_2 = Pacient("maria_sanchez", "pass456", "Diabetes tipo 2")
    
    # Pruebo método login() - Polimorfismo
    print("=== Login de Staff ===")
    staff_1.login()
    staff_2.login()
    
    print("\n=== Login de Pacientes ===")
    paciente_1.login()
    paciente_2.login()


main()