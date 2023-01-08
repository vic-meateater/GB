def simple_factors(number: int):
    result = []
    p = 2

    while p != number:
        if number % p == 0:
            number /= p
            result.append(p)
        else:
            p += 1
    else:
        result.append(p)
    return result


print(simple_factors(int(input("Enter number: "))))
