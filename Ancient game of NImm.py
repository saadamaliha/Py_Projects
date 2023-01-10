"""
The ancient game of Nimm starts with a pile of 20 stones between the players.

The two players alternate turns.

On a given turn, a player may take either 1 or 2 stone from the center pile.

The two players continue until the center pile has run out of stones.
"""


def main():
    stones = 20
    player = 2
    if player == 2:
        player = 1
    else:
        player = 2
    while stones >= 0:
        if stones > 0:
            print('There are ' + str(stones) + ' stones left.')
            play = int(input("Player " + str(player) + " would you like to remove 1 or 2 stones? "))
            if 0 < play < 3:
                stones -= play
            else:
                play = int(input("Invalid choice. Please enter 1 or 2: "))
                stones -= play
        elif stones <= 0:
            print('Game over.')
            print("")
            if player == 1:
                print("Player 2 wins! ")
            else:
                print("Player 1 wins! ")
            break

    pass


if __name__ == '__main__':
    main()
