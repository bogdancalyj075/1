def calcX ():
    input_a = int(input("Введіть значення для a: "))
    input_b = int(input("Введіть значення для b: "))
    if (input_a < 0 or input_b < 0):
        print("Число повинно бути не від'ємним")
        return
  
    input_mathematical_action = input ("Введіть математичну дію (+, -, *, /): ")
    if input_mathematical_action not in ['+', '-', '*', '/']:
        print("Помилка: введіть коректну математичну дію.")
    if input_mathematical_action == '+':
        summary = input_a + input_b
    if input_mathematical_action == '-':
        summary = input_a - input_b
    if input_mathematical_action == '*':
        summary = input_a * input_b
    if input_mathematical_action == '/':
        summary = input_a / input_b
     
     
    print(f"Сума: {summary}")
    return 