def decode(inputstr: str, code: str) -> str:
    print(inputstr)
    print(code)

inputstr = 'ACSL is an international computer science competition among more than 300 schools.  With countrywide and worldwide participants it became the American Computer Science League.  It has been in continuous existence since 1978.  Each yearly competition consists of 4 regular season contests.  All students at each school may compete but the team score is the sum of the best 3 or 5 top scores.  Each contest consists of a written section and a programming section.'
code = '1.5.4 4.2.6 1.10.1 3.2.1 6.11.6 2.9.8 4.10.3 5.18.1'

x = decode(inputstr,code)
print(x)
