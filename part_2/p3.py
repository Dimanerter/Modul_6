from enum import Enum

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

today = Day.MONDAY
print(today)  # Виведе: Day.MONDAY

if today == Day.MONDAY:
    print("Сьогодні понеділок.")
else:
    print("Сьогодні не понеділок.")

print(today.name)  
print(today.value)  


day_from_value = Day(1)
print(day_from_value)  # Виведе: Day.MONDAY
