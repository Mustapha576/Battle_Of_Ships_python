from sys import argv
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
outputs = []
player1_board = {"B1": [], "B2": [], "P1": [], "P2": [], "P3": [], "P4": [], "C": [], "D": [], "S": []}
player2_board = {"B1": [], "B2": [], "P1": [], "P2": [], "P3": [], "P4": [], "C": [], "D": [], "S": []}

player1_list = [["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]]
player2_list = [["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]]


c1 = ["-"]
b1 = ["-", "-"]
d1 = ["-"]
s1 = ["-"]
pb1 = ["-", "-", "-", "-"]

c2 = ["-"]
b2 = ["-", "-"]
d2 = ["-"]
s2 = ["-"]
pb2 = ["-", "-", "-", "-"]


def reading_inputs():  # Opening files and checking them whether there is a mistake or not
    try:
        player1 = open(argv[1], "r")
        player2 = open(argv[2], "r")
        player1_commands = open(argv[3], "r")
        player2_commands = open(argv[4], "r")
        return player1, player2, player1_commands, player2_commands

    except IOError:
        print("IOError: input file(s) Player1.txt, Player2.txt, Player1.in, Player2.in is/are not reachable.")
        outputs.append("IOError: input file(s) Player1.txt, Player2.txt, Player1.in, Player2.in is/are not reachable.")
        quit()


def ship_places(x, y):  # Placing all the ships by using ship_places function, these places added into places1_board and places2_board
    with open(x, "r") as file1:
        lineup = 1
        for line in file1:
            line1 = line.strip()
            a = line1.split(";")
            b = 0
            d = 0
            for i in a:
                if "C" == i:
                    y["C"].append(str(lineup) + "," + letters[b - d])
                    b += 1
                    d += 1
                if "D" == i:
                    y["D"].append(str(lineup) + "," + letters[b - d])
                    b += 1
                    d += 1
                if "S" == i:
                    y["S"].append(str(lineup) + "," + letters[b - d])
                    b += 1
                    d += 1
                b += 1
            if line.startswith("B1"):
                start, rotation, blank = line.split(";")
                if rotation == "right":
                    c = start.split(",")
                    d = letters.index(c[1])
                    e = c[0].split(":")
                    for i in letters[d:d + 4]:
                        y["B1"].append(e[1] + "," + i)
                elif rotation == "down":
                    c = start.split(",")
                    e = c[0].split(":")
                    for i in range(int(e[1]), int(e[1]) + 4):
                        y["B1"].append(str(i) + "," + c[1])
            if line.startswith("B2"):
                start, rotation, blank = line.split(";")
                if rotation == "right":
                    c = start.split(",")
                    d = letters.index(c[1])
                    e = c[0].split(":")
                    for i in letters[d:d + 4]:
                        y["B2"].append(e[1] + "," + i)
                elif rotation == "down":
                    c = start.split(",")
                    e = c[0].split(":")
                    for i in range(int(e[1]), int(e[1]) + 4):
                        y["B2"].append(str(i) + "," + c[1])
            if line.startswith("P1"):
                start, rotation, blank = line.split(";")
                if rotation == "right":
                    c = start.split(",")
                    d = letters.index(c[1])
                    e = c[0].split(":")
                    for i in letters[d:d + 2]:
                        y["P1"].append(e[1] + "," + i)
                elif rotation == "down":
                    c = start.split(",")
                    e = c[0].split(":")
                    for i in range(int(e[1]), int(e[1]) + 2):
                        y["P1"].append(str(i) + "," + c[1])
            if line.startswith("P2"):
                start, rotation, blank = line.split(";")
                if rotation == "right":
                    c = start.split(",")
                    d = letters.index(c[1])
                    e = c[0].split(":")
                    for i in letters[d:d + 2]:
                        y["P2"].append(e[1] + "," + i)
                elif rotation == "down":
                    c = start.split(",")
                    e = c[0].split(":")
                    for i in range(int(e[1]), int(e[1]) + 2):
                        y["P2"].append(str(i) + "," + c[1])
            if line.startswith("P3"):
                start, rotation, blank = line.split(";")
                if rotation == "right":
                    c = start.split(",")
                    d = letters.index(c[1])
                    e = c[0].split(":")
                    for i in letters[d:d + 2]:
                        y["P3"].append(e[1] + "," + i)
                elif rotation == "down":
                    c = start.split(",")
                    e = c[0].split(":")
                    for i in range(int(e[1]), int(e[1]) + 2):
                        y["P3"].append(str(i) + "," + c[1])
            if line.startswith("P4"):
                start, rotation, blank = line.split(";")
                if rotation == "right":
                    c = start.split(",")
                    d = letters.index(c[1])
                    e = c[0].split(":")
                    for i in letters[d:d + 2]:
                        y["P4"].append(e[1] + "," + i)
                elif rotation == "down":
                    c = start.split(",")
                    e = c[0].split(":")
                    for i in range(int(e[1]), int(e[1]) + 2):
                        y["P4"].append(str(i) + "," + c[1])
            lineup += 1


def gaming():  # All ships placed in the beginning of the function and all turns played in this function.
    outputs.append("Battle of Ships Game")
    outputs.append("")
    print("Battle of Ships Game\n")
    ship_places("Player1.txt", player1_board)
    ship_places("OptionalPlayer1.txt", player1_board)
    ship_places("Player2.txt", player2_board)
    ship_places("OptionalPlayer2.txt", player2_board)

    with open("Player1.in", "r") as file:
        for line in file:
            turns = line.split(";")
    a = 0
    num1 = 2
    num2 = 1
    error_times_p1 = 3
    error_times_p2 = 3
    played_places1 = []
    played_places2 = []
    for h in range(0, 200):
        if int(h) == len(turns):
            break
        if a % 2 == 0:
            if a == 0:  # No play in this round, just showing the empty board
                outputs.append("Player1's Move")
                outputs.append("")
                outputs.append("Round : {}\t\t\t\t\tGrid Size: 10x10".format(a + 1))
                outputs.append("")
                outputs.append("Player1's Hidden Board  \tPlayer2's Hidden Board")
                print("Player1's Move\n")
                print("Round : {}\t\t    Grid Size: 10x10\n".format(a + 1))
                print("Player1's Hidden Board      Player2's Hidden Board")
                b = " ".join(map(str, letters))
                outputs.append("  {}\t\t  {}".format(b, b))
                print("  {}\t      {}".format(b, b))
                for j in range(0, 10):
                    if j == 9:
                        c = " ".join(map(str, player1_list[j]))
                        outputs.append(str(j + 1) + c + "\t\t" + str(j + 1) + c)
                        print(str(j + 1) + c + "       " + str(j + 1) + c)
                    else:
                        c = " ".join(map(str, player1_list[j]))
                        outputs.append(str(j + 1) + " " + c + "\t\t" + str(j + 1) + " " + c)
                        print(str(j + 1) + " " + c + "       " + str(j + 1) + " " + c)
                outputs.append("")
                outputs.append("Carrier \t-\t\t\t\tCarrier \t-")
                outputs.append("Battleship  - - \t\t\tBattleship  - -")
                outputs.append("Destroyer \t-\t\t\t\tDestroyer \t-")
                outputs.append("Submarine \t-\t\t\t\tSubmarine \t-")
                outputs.append("Patrol Boat - - - - \t\tPatrol Boat - - - -")
                print()
                print("Carrier     -\t\t    Carrier     -")
                print("Battleship  - - \t    Battleship  - -")
                print("Destroyer   -\t\t    Destroyer   -")
                print("Submarine   -\t\t    Submarine   -")
                print("Patrol Boat - - - - \t    Patrol Boat - - - -")
                a += 1

            else:
                with open("Player2.in", "r") as file:
                    for line1 in file:
                        try:
                            turns2 = line1.split(";")
                            number, letter = turns2[a - num1].split(",")

                            # Catching Errors
                            if int(number) > 10:
                                raise AssertionError
                            if turns2[a - num1] in played_places2:
                                raise AssertionError

                            # If the move hits any ship, it removes from player1_board and changes "-" to "X"  in player1_list and appends to played_places2
                            for j in player1_board:
                                if turns2[a - num1] in player1_board[j]:
                                    player1_list[int(number) - 1][letters.index(letter)] = "X"
                                    player1_board[j].remove(turns2[a - num1])
                                    played_places2.append(turns2[a - num1])

                            # If the move doesn't hit any ship, it changes "-" to "X" in player1_list and appends to played_places2
                            if player1_list[int(number) - 1][letters.index(letter)] != "X":
                                player1_list[int(number) - 1][letters.index(letter)] = "O"
                                played_places2.append(turns2[a - num1])

                            # In player1_board dictionary, if any key is empty it turns "-" to "X" up those specific list for player1(e.g. if carrier sink, "-" in c1 list changed to "X")
                            b1_hits = 0
                            pb1_hits = 0
                            for i in player1_board:
                                if len(player1_board[i]) == 0:
                                    if i == "B1":
                                        b1[int(b1_hits)] = "X"
                                        b1_hits += 1
                                    if i == "B2":
                                        b1[int(b1_hits)] = "X"
                                        b1_hits += 1
                                    if i == "P1":
                                        pb1[int(pb1_hits)] = "X"
                                        pb1_hits += 1
                                    if i == "P2":
                                        pb1[int(pb1_hits)] = "X"
                                        pb1_hits += 1
                                    if i == "P3":
                                        pb1[int(pb1_hits)] = "X"
                                        pb1_hits += 1
                                    if i == "P4":
                                        pb1[int(pb1_hits)] = "X"
                                        pb1_hits += 1
                                    if i == "C":
                                        c1[0] = "X"
                                    if i == "D":
                                        d1[0] = "X"
                                    if i == "S":
                                        s1[0] = "X"
                            b1_join = " ".join(map(str, b1))
                            pb1_join = " ".join(map(str, pb1))
                            b2_join = " ".join(map(str, b2))
                            pb2_join = " ".join(map(str, pb2))

                            # If game doesn't over, this condition continues the game and showing some output for this round
                            if c1.count("-") != 0 or b1.count("-") != 0 or d1.count("-") != 0 or s1.count("-") != 0 or pb1.count("-") != 0:
                                outputs.append("")
                                outputs.append("Enter your move: {}".format(turns2[a - num1]))
                                outputs.append("")
                                outputs.append("Player1's Move")
                                outputs.append("")
                                outputs.append("Round : {}\t\t\t\t\tGrid Size: 10x10".format(a - num1 + 2))
                                outputs.append("")
                                outputs.append("Player1's Hidden Board  \tPlayer2's Hidden Board")
                                print()
                                print("Enter your move: {}\n".format(turns2[a - num1]))
                                print("Player1's Move\n")
                                print("Round : {}\t\t    Grid Size: 10x10\n".format(a - num1 + 2))
                                print("Player1's Hidden Board      Player2's Hidden Board")
                                b = " ".join(map(str, letters))
                                outputs.append("  {}\t\t  {}".format(b, b))
                                print("  {}\t      {}".format(b, b))
                                a += 1
                                num1 += 1

                            # If the game overs, this condition ends the game and showing some output for this round
                            if c1.count("-") == 0 and b1.count("-") == 0 and d1.count("-") == 0 and s1.count("-") == 0 and pb1.count("-") == 0:
                                outputs.append("")
                                outputs.append("Enter your move: {}".format(turns2[a - num1]))
                                outputs.append("")
                                outputs.append("Player2 Wins!")
                                outputs.append("")
                                outputs.append("Final Information")
                                outputs.append("")
                                outputs.append("Player1's Board  \t\t\tPlayer2's Board")
                                print()
                                print("Enter your move: {}\n".format(turns2[a - num1]))
                                print("Player2 Wins!\n")
                                print("Final Information\n")
                                print("Player1's Board  \t    Player2's Board")
                                b = " ".join(map(str, letters))
                                outputs.append("  {}\t\t  {}".format(b, b))
                                print("  {}\t      {}".format(b, b))

                            # It shows the board for p1 and p2
                            for k in range(1, 11):
                                if k == 10:
                                    join1 = " ".join(map(str, player1_list[k - 1]))
                                    join2 = " ".join(map(str, player2_list[k - 1]))
                                    outputs.append(str(k) + join1 + "\t\t" + str(k) + join2)
                                    print(str(k) + join1 + "       " + str(k) + join2)
                                else:
                                    join1 = " ".join(map(str, player1_list[k - 1]))
                                    join2 = " ".join(map(str, player2_list[k - 1]))
                                    outputs.append(str(k) + " " + join1 + "\t\t" + str(k) + " " + join2)
                                    print(str(k) + " " + join1 + "       " + str(k) + " " + join2)

                            # It shows how many ships sink by two players
                            outputs.append("")
                            outputs.append("Carrier \t{}\t\t\t\tCarrier \t{}".format(c1[0], c2[0]))
                            outputs.append("Battleship  {}\t\t\t\tBattleship  {}".format(b1_join, b2_join))
                            outputs.append("Destroyer \t{}\t\t\t\tDestroyer \t{}".format(d1[0], d2[0]))
                            outputs.append("Submarine \t{}\t\t\t\tSubmarine \t{}".format(s1[0], s2[0]))
                            outputs.append("Patrol Boat {} \t\tPatrol Boat {}".format(pb1_join, pb2_join))
                            print()
                            print("Carrier     {}\t\t    Carrier     {}".format(c1[0], c2[0]))
                            print("Battleship  {} \t    Battleship  {}".format(b1_join, b2_join))
                            print("Destroyer   {}\t\t    Destroyer   {}".format(d1[0], d2[0]))
                            print("Submarine   {}\t\t    Submarine   {}".format(s1[0], s2[0]))
                            print("Patrol Boat {} \t    Patrol Boat {}".format(pb1_join, pb2_join))

                        # If any error happens, it solves here
                        except IndexError:
                            outputs.append("")
                            outputs.append("IndexError: {}".format(turns2[a - num1]))
                            print()
                            print("IndexError: {}".format(turns2[a - num1]))
                            a += 2
                            num1 += 1
                            num2 += int(error_times_p1)
                            if int(error_times_p1) == 3:
                                error_times_p1 -= 1
                        except ValueError:
                            outputs.append("")
                            outputs.append("ValueError: {}".format(turns2[a - num1]))
                            print()
                            print("ValueError: {}".format(turns2[a - num1]))
                            a += 2
                            num1 += 1
                            num2 += int(error_times_p1)
                            if int(error_times_p1) == 3:
                                error_times_p1 -= 1
                        except AssertionError:
                            outputs.append("")
                            outputs.append("Enter your move: {}".format(turns2[a - num1]))
                            outputs.append("AssertionError: Invalid Operation.")
                            print()
                            print("AssertionError: Invalid Operation.")
                            a += 2
                            num1 += 1
                            num2 += int(error_times_p1)
                            if int(error_times_p1) == 3:
                                error_times_p1 -= 1

        if a % 2 == 1:
            try:
                number, letter = turns[a - num2].split(",")
                if int(number) > 10:
                    raise AssertionError
                if turns[a - num2] in played_places1:
                    raise AssertionError

                # If the move hits any ship, it removes from player2_board and changes "-" to "X"  in player2_list and appends to played_places1
                for j in player2_board:
                    if turns[a - num2] in player2_board[j]:
                        player2_list[int(number) - 1][letters.index(letter)] = "X"
                        player2_board[j].remove(turns[a - num2])
                        played_places1.append(turns[a - num2])

                # If the move doesn't hit any ship, it changes "-" to "X" in player2_list and appends to played_places1
                if player2_list[int(number) - 1][letters.index(letter)] != "X":
                    player2_list[int(number) - 1][letters.index(letter)] = "O"
                    played_places1.append(turns[a - num2])

                # In player2_board dictionary, if any key is empty it turns "-" to "X" up those specific list for player2(e.g. if carrier sink, "-" in c2 list changed to "X")
                b2_hits = 0
                pb2_hits = 0
                for i in player2_board:
                    if len(player2_board[i]) == 0:
                        if i == "B1":
                            b2[int(b2_hits)] = "X"
                            b2_hits += 1
                        if i == "B2":
                            b2[int(b2_hits)] = "X"
                            b2_hits += 1
                        if i == "P1":
                            pb2[int(pb2_hits)] = "X"
                            pb2_hits += 1
                        if i == "P2":
                            pb2[int(pb2_hits)] = "X"
                            pb2_hits += 1
                        if i == "P3":
                            pb2[int(pb2_hits)] = "X"
                            pb2_hits += 1
                        if i == "P4":
                            pb2[int(pb2_hits)] = "X"
                            pb2_hits += 1
                        if i == "C":
                            c2[0] = "X"
                        if i == "D":
                            d2[0] = "X"
                        if i == "S":
                            s2[0] = "X"
                b1_join = " ".join(map(str, b1))
                pb1_join = " ".join(map(str, pb1))
                b2_join = " ".join(map(str, b2))
                pb2_join = " ".join(map(str, pb2))

                # If game doesn't over, this condition continues the game and showing some output for this round
                if c2.count("-") != 0 or b2.count("-") != 0 or d2.count("-") != 0 or s2.count("-") != 0 or pb2.count("-") != 0:
                    outputs.append("")
                    outputs.append("Enter your move: {}".format(turns[a - num2]))
                    outputs.append("")
                    outputs.append("Player2's Move")
                    outputs.append("")
                    outputs.append("Round : {}\t\t\t\t\tGrid Size: 10x10".format(a - num2 + 1))
                    outputs.append("")
                    outputs.append("Player1's Hidden Board \t\tPlayer2's Hidden Board")
                    print()
                    print("Enter your move: {}\n".format(turns[a - num2]))
                    print("Player2's Move\n")
                    print("Round : {}\t\t    Grid Size: 10x10\n".format(a - num2 + 1))
                    print("Player1's Hidden Board      Player2's Hidden Board")
                    b = " ".join(map(str, letters))
                    outputs.append("  {}\t\t  {}".format(b, b))
                    print("  {}\t      {}".format(b, b))
                    a += 1
                    num2 += 1

                # If the game overs, this condition ends the game and showing some output for this round
                if c2.count("-") == 0 and b2.count("-") == 0 and d2.count("-") == 0 and s2.count("-") == 0 and pb2.count("-") == 0:
                    outputs.append("")
                    outputs.append("Enter your move: {}".format(turns2[a - num1]))
                    outputs.append("")
                    outputs.append("Player1 Wins!")
                    outputs.append("")
                    outputs.append("Final Information")
                    outputs.append("")
                    outputs.append("Player1's Board  \t\t\tPlayer2's Board")
                    print()
                    print("Enter your move: {}\n".format(turns2[a - num1]))
                    print("Player1 Wins!\n")
                    print("Final Information\n")
                    print("Player1's Board  \t    Player2's Board")
                    b = " ".join(map(str, letters))
                    outputs.append("  {}\t\t  {}".format(b, b))
                    print("  {}\t      {}".format(b, b))

                # It shows the board for p1 and p2
                for k in range(1, 11):
                    if k == 10:
                        c = " ".join(map(str, player1_list[k - 1]))
                        d = " ".join(map(str, player2_list[k - 1]))
                        outputs.append(str(k) + c + "\t\t" + str(k) + d)
                        print(str(k) + c + "       " + str(k) + d)
                    else:
                        c = " ".join(map(str, player1_list[k - 1]))
                        d = " ".join(map(str, player2_list[k - 1]))
                        outputs.append(str(k) + " " + c + "\t\t" + str(k) + " " + d)
                        print(str(k) + " " + c + "       " + str(k) + " " + d)

                # It shows how many ships sink by two players
                outputs.append("")
                outputs.append("Carrier \t{}\t\t\t\tCarrier \t{}".format(c1[0], c2[0]))
                outputs.append("Battleship  {}\t\t\t\tBattleship  {}".format(b1_join, b2_join))
                outputs.append("Destroyer \t{}\t\t\t\tDestroyer \t{}".format(d1[0], d2[0]))
                outputs.append("Submarine \t{}\t\t\t\tSubmarine \t{}".format(s1[0], s2[0]))
                outputs.append("Patrol Boat {} \t\tPatrol Boat {}".format(pb1_join, pb2_join))
                print()
                print("Carrier     {}\t\t    Carrier     {}".format(c1[0], c2[0]))
                print("Battleship  {} \t    Battleship  {}".format(b1_join, b2_join))
                print("Destroyer   {}\t\t    Destroyer   {}".format(d1[0], d2[0]))
                print("Submarine   {}\t\t    Submarine   {}".format(s1[0], s2[0]))
                print("Patrol Boat {} \t    Patrol Boat {}".format(pb1_join, pb2_join))

            # If any error happens, it solves here
            except IndexError:
                outputs.append("")
                outputs.append("IndexError: {}".format(turns[a - num2]))
                print()
                print("IndexError: {}\n".format(turns[a - num2]))
                a += 2
                num2 += 1
                num1 += int(error_times_p2)
                if int(error_times_p2) == 3:
                    error_times_p2 -= 1
            except ValueError:
                outputs.append("")
                outputs.append("ValueError: {}".format(turns[a - num2]))
                print()
                print("ValueError: {}\n".format(turns[a - num2]))
                a += 2
                num2 += 1
                num1 += int(error_times_p2)
                if int(error_times_p2) == 3:
                    error_times_p2 -= 1
            except AssertionError:
                outputs.append("")
                outputs.append("Enter your move: {}".format(turns[a - num2]))
                outputs.append("AssertionError: Invalid Operation.")
                print()
                print("AssertionError: Invalid Operation.\n")
                a += 2
                num2 += 1
                num1 += int(error_times_p2)
                if int(error_times_p2) == 3:
                    error_times_p2 -= 1


def output():  # Output function for Battleships.out
    outfile = open("Battleships.out", "w")
    for line in outputs:
        outfile.write(line + "\n")


def main():  # main function gathers all the functions and executes the programme
    reading_inputs()
    gaming()
    output()


main()
