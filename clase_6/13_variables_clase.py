class Usuario:
    sistema = "Django"  # variable de clase

    def __init__(self, username: str, password: str):
        self.username = username
        self.__password = password


admin = Usuario("admin", "admin123")
user = Usuario("user", "user123")

print(admin.sistema)
print(user.sistema)

# admin.sistema = "FastAPI"
Usuario.sistema = "FastAPI"
print()
print(admin.sistema)
print(user.sistema)
print(vars(admin))
print(vars(user))
