in_list = [1, 2, 3, 6, 7]

def get_sum(x):
  s = 0
  for num in x:
    s=s + num
  return s

y = get_sum(in_list)
print(f"the sum is {y}")

