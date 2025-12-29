import random
big_ship_coordinates = []
class BigShip:
    def generation(self):
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
                print(big_ship_coordinates)
            elif next_direction == 'down':
                a, b = a - 1, b
                big_ship_coordinates.append((a, b))
                a, b = a - 1, b
                big_ship_coordinates.append((a, b))
                print(big_ship_coordinates)
        elif direction == 'horizontal':
            next_direction = random.choice(['left', 'right'])
            if next_direction == 'left':
                a, b = a, b - 1
                big_ship_coordinates.append((a, b))
                a, b = a, b - 1
                big_ship_coordinates.append((a, b))
                print(big_ship_coordinates)
            elif next_direction == 'right':
                a, b = a, b + 1
                big_ship_coordinates.append((a, b))
                a, b = a, b + 1
                big_ship_coordinates.append((a, b))
                print(big_ship_coordinates)
BigShip().generation()




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



