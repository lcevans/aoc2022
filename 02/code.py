with open('data.txt') as f:
    rounds = [line.strip().split(' ') for line in f]

# PART 1

TO_RPS = {
    'A': 0, # Rock
    'B': 1, # Paper
    'C': 2, # Scissors
    'X': 0,
    'Y': 1,
    'Z': 2,
}
def score(round):
    opponent = TO_RPS[round[0]]
    me = TO_RPS[round[1]]

    loss_tie_win = ((me - opponent + 1) % 3) - 1 # According as -1, 0, 1
    battle_points = 3 * loss_tie_win + 3
    choice_points = me + 1
    return battle_points + choice_points

print(sum(score(round) for round in rounds))


# PART 2
def score(round):
    opponent = TO_RPS[round[0]]
    loss_tie_win = TO_RPS[round[1]] - 1 # According as -1, 0, 1

    me = (loss_tie_win + opponent) % 3
    battle_points = 3 * loss_tie_win + 3
    choice_points = me + 1
    return battle_points + choice_points

print(sum(score(round) for round in rounds))
