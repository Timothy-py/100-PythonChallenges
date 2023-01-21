# games = [[1, 2, 3, 4], [1, 3, 2, 4]]
games = [[1, 2, 3, 4], [4, 3, 1, 2]]
n = 4
for round in games:
    team1 = set(round[:n//2])
    team2 = set(round[n//2:])
    print(team1)
    print(team2)
