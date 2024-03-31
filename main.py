class User:
    def __init__(self, id, name, level='user'):
        self._id = id
        self._name = name
        self._level = level

    def get_info(self):
        return f"ID: {self._id}, Name: {self._name}, Level: {self._level}"

class Admin(User):
    def __init__(self, id, name, level='admin'):
        super().__init__(id, name, level)

    def add_user(self, user):
        all_users.append(user)
        print(f"Пользователь {user._name} добавлен.")

    def remove_user(self, user):
        all_users.remove(user)
        print(f"Пользователь {user._name} удален.")

all_users = []


admin = Admin('001', 'Паша')
user1 = User('002', 'Витя')
user2 = User('003', 'Миша')

admin.add_user(user1)
admin.add_user(user2)

print(user1.get_info())
print(user2.get_info())

admin.remove_user(user1)

# Показать всех пользователей
for user in all_users:
    print(user.get_info())


