class Restaurant:
  def  __init__(self, restaurant_name:str, cuisine_type:str):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
  number_served: int = 0
  login_attempts: int = 0

  # Login attempts
  def increment_login_attempts(self)->None:
     self.login_attempts += 1

  # reset login attempts
  def reset_login_attempts(self)->None:
    self.login_attempts = 0

  def set_number_served(self, number:int)->None:
    self.number_served = number

  def increment_number_served(self, number:int)->None:
    self.number_served += number

  def describe_restaurant(self)->None:
    print(f"Welcome to {self.restaurant_name}, this is a famous {self.cuisine_type} restaurant.")

  def open_restaurant(self)->None:
    print(F"The {self.restaurant_name} is open now!")


class User:
  def __init__(self, first_name:str, last_name:str, age:int, role:str) -> None:
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.role = role
  
  def describe_user(self) -> None:
    print(f"This is {self.first_name} {self.last_name} and I am {self.age} years old {self.role}.")
  
  def greet_User(self) -> None:
    print(f"Good morning {self.first_name}!")












