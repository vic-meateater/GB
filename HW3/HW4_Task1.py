num = float(input("Enter a real number: "))
accuracy = input("Enter the required accuracy '0.0001': ")
accuracy_d = len(accuracy) - 2
print(f"num = {num:.{accuracy_d}f}")
