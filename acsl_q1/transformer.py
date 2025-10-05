def transform(input_str: str) -> str:
    """
    Transforms a string based on a specific logic.

    The input string is expected to contain three space-separated parts:
    1. A string of digits (e.g., "124987").
    2. An integer `p` representing a 1-based position from the left.
    3. An integer `q` representing a 1-based position from the right.

    Args:
        input_str: A space-separated string with a number and two positions.

    Returns:
        The transformed string.
    """
    
    qwerty = input()
yay = qwerty.strip().split('\n')
for l in yay:
  yay_part=l.split()
  N = int(yay_part[0])
  P = int(yay_part[1])
  D = int(yay_part[2])

  n = str(N)
  p = len(n) - P

  def findp(n,p):
    nst = []
    for i in n:
      nst.append(i)
    return(nst[p])

  x = findp(n,p)

  def findu(num):
    l = len(str(num))
    emt = []
    for i in str(num):
      emt.append(i)
    return emt[l-1]

  def findl(num):
    emt = []
    for i in str(num):
      emt.append(i)
    return emt[0]

  def main(x,D):
    x = int(x)
    if x < 5:
      x = x + D
      x = findu(x)
      return(x)
    elif x > 4:
      x = x - D
      x = abs(x)
      x = findl(x)
      return(x)

  x = main(x,D)

  def replace(n,p,x):
    nst = []
    for i in n:
      nst.append(i)
    nst[p] = x
    for i in (p+1,len(n)-1):
      nst[i] = str(0)
    y = "".join(nst)
    y = int(y)
    print(y)

  replace(n,p,x)

    return ""
