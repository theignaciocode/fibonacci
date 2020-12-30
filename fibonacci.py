def fibonacci(position: int) -> int:
    numbers = [0, 1]
    if position == 0 or position == 1:
        return numbers[position]
    else:
        for i in range(2, position + 1, 1):
            new_number = numbers[-1] + numbers[-2]
            numbers.append(new_number)
        return numbers[position]


print(fibonacci(2))     # 1
print(fibonacci(5))     # 5
print(fibonacci(9))     # 34

# developer: theIGNACIOcode
