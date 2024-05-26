import os, random

grids = [None, 100, 100, -100, 100, -300, -100, 300, 500]
tallyOfPossibleWinnings = {}

def traverseTrack(): # returns the winnings collected through traversing the track by rolling a standard four-sided die twice
    winnings = 0
    position = 0
    for i in range(2):
        roll = random.randint(1, 4)
        position += roll
        winnings += grids[position]
    return winnings

def spinSpinner(): # returns the winnings collected through spinning the spinner twice
    winnings = 0
    for i in range(2):
        spin = random.randint(1, 2)
        if spin == 1:
            winnings += 100
        else:
            winnings -= 100
    return winnings

def playGame(): # plays the game once and returns the winnings of that game
    winning = 0
    winning += traverseTrack()
    winning += spinSpinner()
    return winning

def main(): # runs the simulation 200000 times, writes the results to results.txt, calculates the experimental probability of each winning, and calculates the average winnings
    global tallyOfPossibleWinnings
    n = 200000
    if os.path.exists("results.txt"):
        os.remove("results.txt")
    with open("results.txt", "a+") as f:
        totalWinnings = 0
        f.write("Results of " + str(n) + " Simulated Games of Rolling Egg: \n\n")
        for i in range(n):
            winning = playGame()
            totalWinnings += winning
            if winning >= 0:
                f.write("$" + str(winning) + "\n")
            else:
                f.write("-$" + str(abs(winning)) + "\n")
            if winning in tallyOfPossibleWinnings.keys():
                tallyOfPossibleWinnings[winning] += 1
            else:
                tallyOfPossibleWinnings[winning] = 1
        f.write("\n\nExperimental Probability Distribution: \n\n")
        tallyOfPossibleWinnings = {key: tallyOfPossibleWinnings[key] for key in sorted(tallyOfPossibleWinnings.keys())}
        for key in tallyOfPossibleWinnings.keys():
            if key >= 0:
                winningInDollars = "$" + str(key)
            else:
                winningInDollars = "-$" + str(abs(key))
            f.write(winningInDollars + ": " + str(tallyOfPossibleWinnings[key]) + "/" + str(n) + " --> " + str(tallyOfPossibleWinnings[key] / n) + "\n")
        f.write("\n\nExperimental Average: \n\n")
        experimentalAverage = totalWinnings / n
        if experimentalAverage >= 0:
            f.write("A(W) = $" + str(experimentalAverage))
        else:
            f.write("A(W) = -$" + str(abs(experimentalAverage)))

if __name__ == "__main__":
    main()