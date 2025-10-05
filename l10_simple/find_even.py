in_str = input("Enter the numbers: ")
print(f"in_str = {in_str}")

in_list_str = in_str.split()
print(f"in_list_str = {in_list_str}")

in_list_nums = [int(x) for x in in_list_str]
print(f"in_list_nums = {in_list_nums}")

def get_even(x):
  y = []
  for num in x:
    if num % 2 == 0:
      y.append(num)
  return y

z = get_even(in_list_nums)
print(f"final list = {z}")
