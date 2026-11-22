tyagain=True
while tyagain:
    x=input('give me a sentence ')
    r=x.split()
    if len(r)<3:
        print("try again")
    else:
        print(r[2])
        tyagain=False
