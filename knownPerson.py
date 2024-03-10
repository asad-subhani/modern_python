from typing import Dict


personData: Dict[str, str | int] = { 
  "first_name": "Asad Subhani",
  "father_name": "Zafar Iqbal",
  "age": 25,
  "city": "Lahore"

}
print(f"Name: {personData.get("first_name")}")
print(f"Father name: {personData.get("father_name")}")
print(f"Age: {personData.get("age")}")
print(f"City: {personData.get("city")}")