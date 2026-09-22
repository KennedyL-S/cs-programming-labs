distance = float(input())
fuel_consumption = float(input())
fuel_price = float(input())

fuel_needed = (distance * fuel_consumption) / 100
total_cost = fuel_needed * fuel_price

print(f"Топливо: {fuel_needed:.2f} л")
print(f"Стоимость: {total_cost:.2f} руб")