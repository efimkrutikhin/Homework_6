def generate_arithmetic_progression():
    a1 = float(input("Введите первый элемент прогрессии: "))
    d = float(input("Введите разность прогрессии: "))
    n = int(input("Введите количество элементов: "))
    
    progression = [a1 + (i * d) for i in range(n)]
    return progression

def main():
    progression = generate_arithmetic_progression()
    
    print("Арифметическая прогрессия:")
    for num in progression:
        print(num)

if __name__ == "__main__":
    main()