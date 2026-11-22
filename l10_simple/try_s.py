# take input frm user

#
i = input("enter numbers")
p = i.split()

print(f"1.{i}2.{p}")
p = [int(y) for y in p]
print(p)
