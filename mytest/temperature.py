def analyze_temperature(temperatures):

    if not temperatures or len(temperatures) != 7:
        return None
    

    if not all(isinstance(temp, int) for temp in temperatures):
        return None
    

    average_temp = round(sum(temperatures) / len(temperatures), 1)
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    hot_days = sum(1 for temp in temperatures if temp > 25)
    cold_days = sum(1 for temp in temperatures if temp < 10)
    

    return {
        "average": average_temp,
        "max": max_temp,
        "min": min_temp,
        "hot_days": hot_days,
        "cold_days": cold_days
    }


# Примеры использования
if __name__ == "__main__":
    # Пример 1: нормальные данные
    temps1 = [22, 24, 26, 28, 30, 19, 21]
    result1 = analyze_temperature(temps1)
    print("Пример 1:")
    print(f"Температуры: {temps1}")
    print(f"Результат: {result1}")
    print()
    
    # Пример 2: с жаркими и холодными днями
    temps2 = [8, 12, 26, 30, 32, 9, 27]
    result2 = analyze_temperature(temps2)
    print("Пример 2:")
    print(f"Температуры: {temps2}")
    print(f"Результат: {result2}")
    print()

      # Пример 3: пустой список
    temps3 = []
    result3 = analyze_temperature(temps3)
    print("Пример 3 (пустой список):")
    print(f"Результат: {result3}")
    print()
