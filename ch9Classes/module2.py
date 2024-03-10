from module import User

class Privileges:
  def __init__(self, privileges:list[str] = ["add user", "add post", "delete user"]) -> None:
    self.privileges = privileges

  def show_privileges(self)->None:
    print("Admin have following privileges:")
    for prev in self.privileges:
      print(f"\t{prev}")

class Admin(User):
  def __init__(self, first_name: str, last_name: str, age: int, role: str) -> None:
    
    super().__init__(first_name, last_name, age, role)

  # instance of privileges class
    self.my_privileges:Privileges = Privileges()