import random
import sys
sys.setrecursionlimit(5000)
big_ship_coordinates = []
middle_ship_coordinates = []
little_ship_coordinates = []
occupied_cells = []
max_counter = 0
c = 0
max_counter_2 = 0
class Calling:
    def big_ship_call(self):
        global occupied_cells
        global big_ship_coordinates
        global middle_ship_coordinates
        global little_ship_coordinates
        little_ship_coordinates = []
        middle_ship_coordinates = []
        occupied_cells = []
        big_ship_coordinates = []
        BigShip().generation()

    def middle_ship_call(self):
        MiddleShip().generation()
    def little_ship_call(self):
        LittleShip().generation()
class MiddleShip:
    def generation(self):
        global occupied_cells
        global middle_ship_coordinates
        global max_counter
        while max_counter != 400:
            if len(middle_ship_coordinates) != 4:
                max_counter += 1
                a = random.randint(1, 5)
                b = random.randint(1, 5)
                if (a, b) not in occupied_cells:
                    direction = random.choice(['vertical', 'horizontal'])
                    if direction == 'vertical':
                        next_direction = random.choice(['up', 'down'])
                        if next_direction == 'up':
                            if (a + 1, b) not in occupied_cells:
                                middle_ship_coordinates.append((a, b))
                                a, b = a + 1, b
                                middle_ship_coordinates.append((a, b))
                                for i in middle_ship_coordinates:
                                    occupied_cells.append(i)
                                    a, b = i
                                    occupied_cells.append((a - 1, b))
                                    occupied_cells.append((a, b - 1))
                                    occupied_cells.append((a + 1, b))
                                    occupied_cells.append((a, b + 1))
                                    occupied_cells.append((a + 1, b + 1))
                                    occupied_cells.append((a - 1, b - 1))
                                    occupied_cells.append((a - 1, b + 1))
                                    occupied_cells.append((a + 1, b - 1))

                            else:
                                Calling().middle_ship_call()
                        elif next_direction == 'down':
                            if (a - 1, b) not in occupied_cells:
                                middle_ship_coordinates.append((a, b))
                                a, b = a - 1, b
                                middle_ship_coordinates.append((a, b))
                                for i in middle_ship_coordinates:
                                    occupied_cells.append(i)
                                    a, b = i
                                    occupied_cells.append((a - 1, b))
                                    occupied_cells.append((a, b - 1))
                                    occupied_cells.append((a + 1, b))
                                    occupied_cells.append((a, b + 1))
                                    occupied_cells.append((a + 1, b + 1))
                                    occupied_cells.append((a - 1, b - 1))
                                    occupied_cells.append((a - 1, b + 1))
                                    occupied_cells.append((a + 1, b - 1))

                            else:
                                Calling().middle_ship_call()
                    elif direction == 'horizontal':
                        next_direction = random.choice(['left', 'right'])
                        if next_direction == 'left':
                            if (a, b - 1) not in occupied_cells:
                                middle_ship_coordinates.append((a, b))
                                a, b = a, b - 1
                                middle_ship_coordinates.append((a, b))
                                for i in middle_ship_coordinates:
                                    occupied_cells.append(i)
                                    a, b = i
                                    occupied_cells.append((a - 1, b))
                                    occupied_cells.append((a, b - 1))
                                    occupied_cells.append((a + 1, b))
                                    occupied_cells.append((a, b + 1))
                                    occupied_cells.append((a + 1, b + 1))
                                    occupied_cells.append((a - 1, b - 1))
                                    occupied_cells.append((a - 1, b + 1))
                                    occupied_cells.append((a + 1, b - 1))

                            else:
                                Calling().middle_ship_call()
                        elif next_direction == 'right':
                            if (a, b + 1) not in occupied_cells:
                                middle_ship_coordinates.append((a, b))
                                a, b = a, b + 1
                                middle_ship_coordinates.append((a, b))
                                for i in middle_ship_coordinates:
                                    occupied_cells.append(i)
                                    a, b = i
                                    occupied_cells.append((a - 1, b))
                                    occupied_cells.append((a, b - 1))
                                    occupied_cells.append((a + 1, b))
                                    occupied_cells.append((a, b + 1))
                                    occupied_cells.append((a + 1, b + 1))
                                    occupied_cells.append((a - 1, b - 1))
                                    occupied_cells.append((a - 1, b + 1))
                                    occupied_cells.append((a + 1, b - 1))

                            else:
                                Calling().middle_ship_call()
                else:
                    Calling().middle_ship_call()
            else:
                Calling().little_ship_call()
                break
        else:
            occupied_cells = []
            max_counter = 0
            BigShip().generation()
class BigShip:
    def generation(self):
        global big_ship_coordinates
        global occupied_cells
        big_ship_coordinates = []
        occupied_cells = []
        a = random.randint(2, 4)
        b = random.randint(2, 4)
        big_ship_coordinates.append((a, b))
        direction = random.choice(['vertical', 'horizontal'])
        if direction == 'vertical':
            next_direction = random.choice(['up', 'down'])
            if next_direction == 'up':
                a, b = a + 1, b
                big_ship_coordinates.append((a, b))
                a, b = a + 1, b
                big_ship_coordinates.append((a, b))
            elif next_direction == 'down':
                a, b = a - 1, b
                big_ship_coordinates.append((a, b))
                a, b = a - 1, b
                big_ship_coordinates.append((a, b))
        elif direction == 'horizontal':
            next_direction = random.choice(['left', 'right'])
            if next_direction == 'left':
                a, b = a, b - 1
                big_ship_coordinates.append((a, b))
                a, b = a, b - 1
                big_ship_coordinates.append((a, b))
            elif next_direction == 'right':
                a, b = a, b + 1
                big_ship_coordinates.append((a, b))
                a, b = a, b + 1
                big_ship_coordinates.append((a, b))
        for i in big_ship_coordinates:
            occupied_cells.append(i)
            a, b = i
            occupied_cells.append((a - 1, b))
            occupied_cells.append((a, b - 1))
            occupied_cells.append((a + 1, b))
            occupied_cells.append((a, b + 1))
            occupied_cells.append((a + 1, b + 1))
            occupied_cells.append((a - 1, b - 1))
            occupied_cells.append((a - 1, b + 1))
            occupied_cells.append((a + 1, b - 1))
        Calling().middle_ship_call()
class LittleShip:
    def generation(self):
        global occupied_cells
        global little_ship_coordinates
        global max_counter_2
        global max_counter
        global big_ship_coordinates
        global middle_ship_coordinates
        global c
        while max_counter_2 != 500:
            if len(little_ship_coordinates) != 3:
                max_counter_2 += 1
                a = random.randint(0, 6)
                b = random.randint(0, 6)
                if (a, b) not in occupied_cells:
                    little_ship_coordinates.append([(a, b)])
                    occupied_cells.append((a, b))
                    occupied_cells.append((a - 1, b))
                    occupied_cells.append((a, b - 1))
                    occupied_cells.append((a + 1, b))
                    occupied_cells.append((a, b + 1))
                    occupied_cells.append((a + 1, b + 1))
                    occupied_cells.append((a - 1, b - 1))
                    occupied_cells.append((a - 1, b + 1))
                    occupied_cells.append((a + 1, b - 1))
                    c += 1
                else:
                    Calling().little_ship_call()
                    break
            else:
                break
        else:
            max_counter = 0
            max_counter_2 = 0
            occupied_cells = []
            c = 0
            little_ship_coordinates = []
            big_ship_coordinates = []
            middle_ship_coordinates = []
            Calling().big_ship_call()





Calling().big_ship_call()


# print("Big ship coordinates:", big_ship_coordinates)
# print("Middle ship coordinates:", middle_ship_coordinates)
# print(little_ship_coordinates)
mixed_right_coordinates = []
for i in big_ship_coordinates:
    mixed_right_coordinates.append(i)
for j in middle_ship_coordinates:
    mixed_right_coordinates.append(j)
for k in little_ship_coordinates:
    mixed_right_coordinates.append(k)

right_coordinates = [big_ship_coordinates, middle_ship_coordinates[:2], middle_ship_coordinates[2:], little_ship_coordinates[0], little_ship_coordinates[1], little_ship_coordinates[2]]
print(right_coordinates)

# field = [['*'] * 7 for i in range(7)]
# mixed_right_coordinates = [(1, 1), (1, 2), (1, 3), (4, 0), (5, 0), (3, 4), (3, 5), (0, 6), (5, 3), (6, 6), (0, 0)]
# right_coordinates = [[(1, 1), (1, 2), (1, 3)], [(4, 0), (5, 0)], [(3, 4), (3, 5)], [(0, 6)], [(5, 3)], [(6, 6)], [(0, 0)]]
# all_guessed_coordinates = []
# right_guessed_coordinates = []
# class Game:
#     def intro(self):
#         print('  1 2 3 4 5 6 7')
#         rows = 'ABCDEFG'
#         for i in range(7):
#             print(rows[i], *field[i])
#         while len(mixed_right_coordinates) != 0:
#             try:
#                 users_coordinate = input('Enter the coordinates(from 1 to 7): like A, 1\n')
#                 users_coordinate = users_coordinate.split(',')
#                 a, b = users_coordinate
#                 b = int(b)
#                 d = {1 : 0, 2 : 1, 3 : 2, 4 : 3, 5 : 4, 6 : 5, 7 : 6}
#                 d2 = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6}
#                 users_coordinate = (d2[a], d[b])
#                 Game().check_1(users_coordinate)
#             except:
#                 Game().intro()
#     def check_1(self, users_coordinate):
#         if users_coordinate not in all_guessed_coordinates:
#             if users_coordinate in mixed_right_coordinates:
#                 a, b = users_coordinate
#                 field[a][b] = 'H'
#                 mixed_right_coordinates.remove(users_coordinate)
#                 right_guessed_coordinates.append(users_coordinate)
#                 all_guessed_coordinates.append(users_coordinate)
#             else:
#                 a, b = users_coordinate
#                 field[a][b] = 'M'
#                 all_guessed_coordinates.append(users_coordinate)
#             Game().check_2()
#         else:
#             print('You have already entered these coordinates, please try again')
#             Game().intro()
#     def check_2(self):
#         for i in right_coordinates:
#             l = len(i)
#             counter = 0
#             ship_for_sunk = []
#             for j in i:
#                 ship_for_sunk.append(j)
#                 if j in right_guessed_coordinates:
#                     counter += 1
#                     if counter == l:
#                         for k, h in ship_for_sunk:
#                             field[k][h] = 'S'
#         Game().intro()
# Game().intro()



