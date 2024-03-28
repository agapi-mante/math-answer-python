price_per_kg = float(input("Введите цену за 1 кг конфет: "))

for kg in range(1, 11):
    total_price = price_per_kg * kg
    print(f"Стоимость {kg} кг конфет: {total_price}")


