car = 'subaru'
print("\nIs car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
car = 'suzuki'
print("\nIs car == 'subaru'? I predict True.")
print(car == 'suzuki')
print("\nIs car == 'audi'? I predict False.")
print(car == 'suzuki')
# using lower()
car = 'BMW' 
print("\nIs car == 'bmw'? I predict True.")
print(car == 'bmw')
print("\nIs car == 'bmw'? I predict False.")
print(car.lower() == 'bmw')
car = 'Tayota'
print("\nIs car == 'subaru'? I predict True.")
print(car == 'Tayota')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
# using equality, unEquality, lessthen, greaterthen, lessthen equal, greaterthen equal
number:int = 47
print("\nIs number == 47? I predict True.")
print(number == 47)
print("\nIs number < 50? I predict True.")
print(number < 50)
number1:int = 47
print("\nIs number >= 47? I predict True.")
print(number1 >= 47)
print("\nIs number <= 50? I predict True.")
print(number1 <= 50)

# List findings

cars: list[str] = ["BMW", "Homda", "Tayota", "Audi", "Jaguar"]

find:str = "TayOtA"
for i in cars:
   print( True if i.lower() == find.lower() else False )
print("\n")
for i in cars:
   print( True if i.lower() != find.lower() else False )

print("\n")
print(True if find.lower() not in cars else False)
print("\n")
print(True if find.lower() in cars else False)