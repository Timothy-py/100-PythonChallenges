# QUESTION
# There are n(n is even) players, conveniently labelled 1, 2, ...n. These players will play m rounds of games. In each round of games, the players are split into two teams of n/2 players each. Two players x < y are said to have played against each other if they were on different teams for one of the m games.

# You are given three arguments: n, m, games. Your task is to check that for all pairs of players 1<=x, y<=n, player x has played against y. games is a 2-dimensional list that represents the m rounds of games among n players.

# Write a function check(n, m games) that takes in 3 arguments.

# Inputs
# It is guaranteed that n, m are integers and 1<=n<=20,000, 1<=m<=30. It is also guaranteed that n is even. games is a 2 dimensional list with m rows and n columns, where games[i]is a permutation of 1,2,3,...,n representing round number i. In particular for round i, games[i][0], games[i][1], games[i][n/2-1] is on one team, games[i][n/2], games[i][n/2+1], games[i][n-1] is on the other team.

# Outputs
# check(n,m,games) should return a boolean, True if and only if all pairs of players have played against each other in the m rounds of games.


# SOLUTION
def check(n, m, games):
    # Create a dictionary to store a set of players for each player
    # players = {i: set() for i in range(1, n+1)}
    players = dict()
    for i in range(1, n+1):
        players[i] = set()

    # Iterate through the rounds of games
    for round in games:
        # Get the sets of players in each team for the current round
        # team1 = set(round[:n//2])
        # team2 = set(round[n//2:])
        split = n//2
        team1 = set(round[:split])
        team2 = set(round[split:])
        # For each player in team1, add all players in team2 to their set
        for player in team1:
            players[player].update(team2)
        # For each player in team2, add all players in team1 to their set
        for player in team2:
            players[player].update(team1)

    # Iterate through the players and check that the size of their set is n-1
    for player in players:
        if len(players[player]) == n-1:
            return True
        else:
            return False


n = 4
m = 2
games = [[1, 2, 3, 4], [1, 3, 2, 4]]
print(check(n, m, games))


# EXPLANATIONS
# This function keeps track of all the players that each player played against. It then checks if the size of the set is equal to n-1 which means that the player has played against all other players. If any of the players set size is less than n-1, it means that that player has not played against all other players and thus the function returns False. If all players set size is equal to n-1, the function returns True.

# To solve this problem, you will need to iterate through all pairs of players and check if they have played against each other in at least one of the m rounds of games. One way to do this is to create a set for each player, which will store the players they have played against. Then, iterate through the rounds of games and add the players on the opposing team to each player's set. Finally, check that the size of each player's set is n-1, indicating that they have played against all other players. Here's an example implementation of the check() function:
