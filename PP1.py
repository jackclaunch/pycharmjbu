print("Employee's name:")
name = input()

print("Basic pay:")
pay = int(input())

print("Deductions:")
deductions = int(input())

salary = pay - deductions
print(f"{name}'s total pay is {salary}")