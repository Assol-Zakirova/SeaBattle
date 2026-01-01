import generation as gen

def asking_for_name():
    name = input('Please, enter your name\n')
    return name

mixed_right_coordinates = []
right_coordinates = []
def adding_coordinates():
    global mixed_right_coordinates
    global right_coordinates
    for i in gen.big_ship_coordinates:
        mixed_right_coordinates.append(i)
    for j in gen.middle_ship_coordinates:
        mixed_right_coordinates.append(j)
    for k in gen.little_ship_coordinates:
        mixed_right_coordinates.append(k)

    right_coordinates = [
        gen.big_ship_coordinates,
        gen.middle_ship_coordinates[:2],
        gen.middle_ship_coordinates[2:],
        [gen.little_ship_coordinates[0]],
        [gen.little_ship_coordinates[1]],
        [gen.little_ship_coordinates[2]],
    ]

gen.Calling().big_ship_call()
adding_coordinates()

field = [['*'] * 7 for i in range(7)]
all_guessed_coordinates = []
right_guessed_coordinates = []
amount_of_shots = 0

class Game:
    def intro(self):
        global amount_of_shots
        while len(mixed_right_coordinates) != 0:
            try:
                print('  1 2 3 4 5 6 7')
                rows = 'ABCDEFG'
                for i in range(7):
                    print(rows[i], *field[i])
                users_coordinate = input('Enter the coordinates(from 1 to 7): like A, 1\n')
                amount_of_shots += 1
                users_coordinate = users_coordinate.split(',')
                a, b = users_coordinate
                b = int(b)
                d = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6}
                d2 = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
                users_coordinate = (d2[a], d[b])
                self.check_1(users_coordinate)
            except:
                print("Invalid input. Example: A,1")
                continue
        self.ending()

    def check_1(self, users_coordinate):
        if users_coordinate not in all_guessed_coordinates:
            if users_coordinate in mixed_right_coordinates:
                a, b = users_coordinate
                field[a][b] = 'H'
                mixed_right_coordinates.remove(users_coordinate)
                right_guessed_coordinates.append(users_coordinate)
                all_guessed_coordinates.append(users_coordinate)
            else:
                a, b = users_coordinate
                field[a][b] = 'M'
                all_guessed_coordinates.append(users_coordinate)
            self.check_2()
        else:
            print('You have already entered these coordinates, please try again')

    def check_2(self):
        for i in right_coordinates:
            l = len(i)
            counter = 0
            ship_for_sunk = []
            for j in i:
                ship_for_sunk.append(j)
                if j in right_guessed_coordinates:
                    counter += 1
                    if counter == l:
                        for k, h in ship_for_sunk:
                            field[k][h] = 'S'
    def ending(self):
        global max_counter
        global c
        global max_counter_2
        global field
        global all_guessed_coordinates
        global right_guessed_coordinates
        global amount_of_shots
        global mixed_right_coordinates
        global right_coordinates
        continue_game = input('Do you wanna play the game again? Yes/No\n')
        if continue_game == 'Yes':
            max_counter = 0
            c = 0
            max_counter_2 = 0
            mixed_right_coordinates = []
            right_coordinates = []
            gen.Calling().big_ship_call()
            adding_coordinates()
            field = [['*'] * 7 for i in range(7)]
            all_guessed_coordinates = []
            right_guessed_coordinates = []
            amount_of_shots = 0
            game.intro()
        else:
            
            with open("participants.txt", "a") as f:
                f.write(f'{users_name} - {amount_of_shots}\n')
            with open("participants.txt") as f:
                print(f.read())

users_name = asking_for_name()
game = Game()
game.intro()
game.ending()

