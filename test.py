def check(n, m, games):
    # Create a dictionary to store a set of players for each player
    players = {i: set() for i in range(1, n+1)}

    # Iterate through the rounds of games
    for round in games:
        # Get the sets of players in each team for the current round
        team1 = set(round[:n//2])
        team2 = set(round[n//2:])
        # For each player in team1, add all players in team2 to their set
        for player in team1:
            players[player].update(team2)
        # For each player in team2, add all players in team1 to their set
        for player in team2:
            players[player].update(team1)

    # Iterate through the players and check that the size of their set is n-1
    for player in players:
        if len(players[player]) != n-1:
            return False
    return True


def check(n, m, games):
    players = {i: set() for i in range(1, n+1)}

    for round in games:
        team1 = set(round[:n//2])
        team2 = set(round[n//2:])
        for player in team1:
            players[player].update(team2)
        for player in team2:
            players[player].update(team1)

    for player in players:
        if len(players[player]) != n-1:
            return False
    return True


n = 4
m = 2
games = [[1, 2, 3, 4], [4, 3, 1, 2]]
print(check(n, m, games))


# To solve this problem, you will need to iterate through all pairs of players and check if they have played against each other in at least one of the m rounds of games. One way to do this is to create a set for each player, which will store the players they have played against. Then, iterate through the rounds of games and add the players on the opposing team to each player's set. Finally, check that the size of each player's set is n-1, indicating that they have played against all other players. Here's an example implementation of the check() function:
