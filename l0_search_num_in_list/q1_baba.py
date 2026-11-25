# Find the sum of numbers from 1 to x
z = int(input("find the additiong of one to the number you enter:"))
def find_sum(x: int) -> int:
    q = 0
    y = 0
    for i in range(0, x):
        #print("i", i)
        y = y + 1
        #print("y", y)
        q = q + y
        #print("q", q)
    return q


res = find_sum(z)
print(res)
