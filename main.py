import generation as gen

gen.Calling().big_ship_call()

mixed_right_coordinates = []
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

field = [['*'] * 7 for i in range(7)]
all_guessed_coordinates = []
right_guessed_coordinates = []
field_2 = [['*'] * 7 for i in range(7)]
for i in mixed_right_coordinates:
    a, b = i
    field_2[a][b] = 'R'
for row in field_2:
    print(*row)


class Game:
    def intro(self):
        print('  1 2 3 4 5 6 7')
        rows = 'ABCDEFG'
        for i in range(7):
            print(rows[i], *field[i])
        while len(mixed_right_coordinates) != 0:
            try:
                users_coordinate = input('Enter the coordinates(from 1 to 7): like A, 1\n')
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
            self.intro()

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

game = Game()
game.intro()




