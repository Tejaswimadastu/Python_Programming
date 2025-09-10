def add_element(a, x):
    a.add(x)
    return a
def remove_element(a, x):
    a.discard(x)
    return a
x = set(map(int, input("Enter elements of set A: ").split()))
y = int(input("Enter a number to add to set A: "))
print("A after adding:", add_element(x, y))
