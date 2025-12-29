field = [['*'] * 7 for i in range(7)]
for i in field:
    print(*i)
print()
mixed_right_coordinates = [(1, 1), (1, 2), (1, 3), (4, 0), (5, 0), (3, 4), (3, 5), (0, 6), (5, 3), (6, 6), (0, 0)]
right_coordinates = [[(1, 1), (1, 2), (1, 3)], [(4, 0), (5, 0)], [(3, 4), (3, 5)], [(0, 6)], [(5, 3)], [(6, 6)], [(0, 0)]]
right_guessed_coordinates = []
class Checking:
    def intro(self):
        users_coordinate = input('Enter the coordinates:\n')
        users_coordinate = [int(n) for n in users_coordinate.split(',')]
        a, b = users_coordinate
        users_coordinate = (a, b)
        Checking().check_1(users_coordinate)
    def check_1(self, users_coordinate):
        while len(mixed_right_coordinates) != 0:
            if users_coordinate in mixed_right_coordinates:
                a, b = users_coordinate
                field[a][b] = 'H'
                mixed_right_coordinates.remove(users_coordinate)
                right_guessed_coordinates.append(users_coordinate)
            else:
                a, b = users_coordinate
                field[a][b] = 'M'
            for i in field:
                print(*i)
            Checking().check_2()
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
        for p in field:
            print(*p)
        Checking().intro()
y = Checking()
y.intro()



