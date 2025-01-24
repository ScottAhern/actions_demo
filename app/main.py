def equal(x: int, y: int) -> bool:
    if (x is y):
        return True
    return False

value1 = 5
value2 = 5

res = equal(value1, value2)

print(f"Values are equal: {res}")
