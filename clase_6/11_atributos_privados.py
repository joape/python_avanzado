class User:
    def __init__(self, username: str, password: str) -> None:
        self.__username = username  # atributo privado
        self.password = password

    def set_username(self, new_value: str):
        if len(new_value) > 3:
            self.__username = new_value
        else:
            raise ValueError("La longitud debe ser mayor a 3 caracteres")

    def get_username(self):
        return self.__username


user = User("admin", "1234")
print(user.get_username())
user.set_username("superadmin")
print(user.get_username())
