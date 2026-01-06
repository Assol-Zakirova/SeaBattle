import generation as gen
import os

launch_generation = gen.BigShip()
launch_generation.generation()

def asking_for_name():
    name = input('Please, enter your name\n')
    os.system('clear')
    return name
class Game:
    def __init__(self):
        self.field = [['*'] * 7 for i in range(7)]
        self.all_guessed_coordinates = []
        self.right_guessed_coordinates = []
        self.amount_of_shots = 0
    def intro(self):
        while len(gen.mixed_right_coordinates) != 0:
            try:
                print('  1 2 3 4 5 6 7')
                rows = 'ABCDEFG'
                for i in range(7):
                    print(rows[i], *self.field[i])
                users_coordinate = input('Enter the coordinates(from 1 to 7): like A, 1\n')
                self.amount_of_shots += 1
                users_coordinate = users_coordinate.split(',')
                a, b = users_coordinate
                b = int(b)
                d = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6}
                d2 = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
                users_coordinate = (d2[a], d[b])
                self.check_1(users_coordinate)
                os.system('clear')
            except:
                os.system('clear')
                print("Invalid input. Example: A,1")
                continue
        self.ending()
    def check_1(self, users_coordinate):
        if users_coordinate not in self.all_guessed_coordinates:
            if users_coordinate in gen.mixed_right_coordinates:
                a, b = users_coordinate
                self.field[a][b] = 'H'
                gen.mixed_right_coordinates.remove(users_coordinate)
                self.right_guessed_coordinates.append(users_coordinate)
                self.all_guessed_coordinates.append(users_coordinate)
            else:
                a, b = users_coordinate
                self.field[a][b] = 'M'
                self.all_guessed_coordinates.append(users_coordinate)
            self.check_2()
        else:
            print('You have already entered these coordinates, please try again')
    def check_2(self):
        for i in gen.right_coordinates:
            l = len(i)
            counter = 0
            ship_for_sunk = []
            for j in i:
                ship_for_sunk.append(j)
                if j in self.right_guessed_coordinates:
                    counter += 1
                    if counter == l:
                        for k, h in ship_for_sunk:
                            self.field[k][h] = 'S'
    def ending(self):
        os.system('clear')
        continue_game = input('Do you wanna play the game again? Yes/No\n')
        if continue_game == 'Yes':
            os.system('clear')
            launch_generation = gen.BigShip()
            launch_generation.generation()
            game = Game()
            game.intro()
        else:
            os.system('clear')
            with open("participants.txt", "a") as f:
                f.write(f"{users_name} - {self.amount_of_shots}\n")
            players = []
            with open("participants.txt") as f:
                for line in f:
                    line = line.strip()

                    if not line:
                        continue  

                    if ' - ' not in line:
                        continue  

                    name, shots = line.split(' - ')
                    players.append((name, int(shots)))
                    players.sort(key=lambda x: x[1])

            print('The list of participants from the highest to the lowest score:')
            for name, shots in players:
                print(f'{name} - {shots}')
users_name = asking_for_name()
game = Game()
game.intro()





