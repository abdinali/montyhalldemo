import random


def switch_strategy_simulation(trials):
    wins = 0
    for _ in range(trials):
        prizePos = random.randint(0, 2)
        guessPos = random.randint(0, 2)

        revealedPos = getRevealPosition(guessPos, prizePos)
        switchPos = getSwitchPosition(guessPos, revealedPos)

        if switchPos == prizePos:
            wins += 1

    winPct = float(wins / trials)
    return winPct

def stay_strategy_simulation(trials):
    wins = 0
    for _ in range(trials):
        prizePos = random.randint(0, 2)
        guessPos = random.randint(0, 2)

        if guessPos == prizePos:
            wins += 1

    winPct = float(wins / trials)
    return winPct

def getRevealPosition(guessPos, prizePos):
    if prizePos == 0:
        if guessPos == 0: return random.choice([1, 2])
        if guessPos == 1: return 2
        if guessPos == 2: return 1
    elif prizePos == 1:
        if guessPos == 0: return 2
        if guessPos == 1: return random.choice([0, 2])
        if guessPos == 2: return 0
    else:
        if guessPos == 0: return 1
        if guessPos == 1: return 0
        if guessPos == 2: return random.choice([0, 1])


def getSwitchPosition(guessPos, revealedPos):
    if guessPos == 0:
        if revealedPos == 1: return 2
        if revealedPos == 2: return 1
    elif guessPos == 1:
        if revealedPos == 2: return 0
        if revealedPos == 0: return 2
    else:
        if revealedPos == 0: return 1
        if revealedPos == 1: return 0


win_percentage_switch = switch_strategy_simulation(1_000_000)
win_percentage_stay = stay_strategy_simulation(1_000_000)

# Switching improves odds of winning the prize from ~1/3 to ~2/3.
print(win_percentage_switch, win_percentage_stay)
