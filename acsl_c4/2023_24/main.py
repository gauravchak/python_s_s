def spot(w,rows):
    q = []
    for i in w:
        q.append(i)
    q[0] = int(q[0])
    q[1] = int(q[1])    
    q[0] = q[0] - 1
    q[1] = q[1] - 1
    ans = rows[q[0]]
    answer = ans[q[1]]
    ans[q[1]] = "E"
    return(answer)

def process(board:str, path: str) -> str:
    tiles = board.split(" ")
    r1 = [tiles[0],tiles[1],tiles[2],tiles[3],tiles[4]]
    r2 = [tiles[5],tiles[6],tiles[7],tiles[8],tiles[9]]
    r3 = [tiles[10],tiles[11],tiles[12],tiles[13],tiles[14]]
    r4 = [tiles[15],tiles[16],tiles[17],tiles[18],tiles[19]]
    r5 = [tiles[20],tiles[21],tiles[22],tiles[23],tiles[24]]
    r6 = [tiles[25],tiles[26],tiles[27],tiles[28],tiles[29]]
    r7 = [tiles[30],tiles[31],tiles[32],tiles[33],tiles[34]]
    r8 = [tiles[35],tiles[36],tiles[37],tiles[38],tiles[39]]
    rows = [r1,r2,r3,r4,r5,r6,r7,r8]
    okay = path.split()
    last = okay[len(okay) - 1]
    numbers = []
    q = []
    for w in okay:
        go = spot(w,rows)
        numbers.append(go)
    n = 0
    for i in numbers:
            n = n + int(i)
    r = 2
    while n > r:
         r = r * 2
    t = []
    for i in last:
        t.append(i)
    t[0] = int(t[0])
    t[1] = int(t[1])    
    t[0] = t[0] - 1
    t[1] = t[1] - 1
    ans = rows[t[0]]
    ans[t[1]] = r
    y = True
    while  y == True:
        y = False
        for i in range(0,len(rows)-1):
            for j in range(len(rows[i])):
                 qwe = rows[i]
                 if qwe[j] != "E":
                      b = i + 1 
                      qwer = rows[b]
                      if qwer[j] == "E":
                           qwer[j] = qwe[j]
                           qwe[j] = "E"
        for i in range(1,len(rows)):
            for j in range(len(rows[i])):
                 qwe = rows[i]
                 if qwe[j] == "E":
                      b = i - 1 
                      qwer = rows[b]
                      if qwer[j] != "E":
                           y = True
    toadd = ['256','128','64','32','16','8','4','2']
    p = 0
    for i in range(len(rows)):
         for j in range(len(rows[i])):
              asd = rows[i]
              if asd[j] == "E":
                asd[j] = toadd[p]
                p = p + 1
                if p == len(toadd):
                     p = 0
    x = []
    for i in rows:
         for j in i:
              x.append(str(j))
    return " ".join(x)

test_cases = [
    {
        "board": "4 128 4 128 32 16 16 4 256 16 32 4 16 64 4 8 64 64 256 8 16 2 2 256 4 32 128 2 64 8 256 32 128 16 2 8 32 32 4 32",
        "path": "13 23 32 41 51 61 72 82 83",
        "expected": "256 128 64 128 32 32 16 8 256 16 4 2 16 64 4 4 128 64 256 8 16 16 2 256 4 32 64 2 64 8 256 2 128 16 2 8 128 256 4 32",
    },
    {
        "board": "256 16 256 2 32 2 16 2 16 8 32 2 256 64 16 4 2 128 2 32 8 8 32 256 2 2 4 8 32 128 16 16 32 64 256 4 16 128 4 8",
        "path": "14 23 32 42 41 51 52 63 72 73 74 83",
        "expected": "256 128 64 32 32 16 8 4 2 8 256 256 128 16 16 2 64 256 64 32 32 16 256 2 2 2 16 128 256 128 16 4 32 32 256 4 16 512 4 8",
    },
    {
        "board": "256 16 256 2 32 2 16 2 16 8 32 2 256 64 16 4 2 128 2 32 8 8 32 256 2 2 4 8 32 128 16 16 32 64 256 4 16 128 4 8",
        "path": "14 23 32 42 41 51 52 63 72 73 74 83",
        "expected": "256 128 64 32 32 16 8 4 2 8 256 256 128 16 16 2 64 256 64 32 32 16 256 2 2 2 16 128 256 128 16 4 32 32 256 4 16 512 4 8",
    },
    {
        "board": "256 16 256 2 32 2 16 2 16 8 32 2 256 64 16 4 2 128 2 32 8 8 32 256 2 8 4 8 32 128 16 16 32 64 256 4 16 128 4 8",
        "path": "14 23 32 41 51 52 61 71 72 82",
        "expected": "256 128 64 32 32 16 8 256 16 8 4 2 256 64 16 256 16 128 2 32 256 16 32 256 2 2 2 8 32 128 32 4 32 64 256 4 128 128 4 8",
    },
]


for test_case in test_cases:
    result = process(test_case["board"], test_case["path"])
    assert result == test_case["expected"], f"Expected {test_case['expected']} but got {result}"

print("All tests passed!")