def to_bin(number: int):
    result = []

    while number:
        result.append(number % 2)
        number //= 2
    result.reverse()
    print(*result, sep="")


to_bin(int(input("Enter number: ")))
