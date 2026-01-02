import random
mixed_right_coordinates = []
right_coordinates = []
def adding_coordinates(var_b_s_coordinates, var_m_s_coordinates, var_l_s_coordinates):
    global mixed_right_coordinates
    global right_coordinates
    for i in var_b_s_coordinates:
        mixed_right_coordinates.append(i)
    for j in var_m_s_coordinates:
        mixed_right_coordinates.append(j)
    for k in var_l_s_coordinates:
        mixed_right_coordinates.append(k)
    right_coordinates = [
        var_b_s_coordinates,
        var_m_s_coordinates[:2],
        var_m_s_coordinates[2:],
        [var_l_s_coordinates[0]],
        [var_l_s_coordinates[1]],
        [var_l_s_coordinates[2]],
    ]
    return mixed_right_coordinates, right_coordinates

class MiddleShip:
    def __init__(self):
        self.middle_ship_coordinates = []
    def generation(self, var_oc_cells):
        while len(self.middle_ship_coordinates) != 4:
            while True:
                a = random.randint(1, 5)
                b = random.randint(1, 5)
                if (a, b) not in var_oc_cells:
                    direction = random.choice(['vertical', 'horizontal'])
                    if direction == 'vertical':
                        next_direction = random.choice(['up', 'down'])
                        if next_direction == 'up':
                            if (a + 1, b) not in var_oc_cells:
                                self.middle_ship_coordinates.append((a, b))
                                a, b = a + 1, b
                                self.middle_ship_coordinates.append((a, b))
                                for i in self.middle_ship_coordinates:
                                    var_oc_cells .append(i)
                                    a, b = i
                                    var_oc_cells.append((a - 1, b))
                                    var_oc_cells.append((a, b - 1))
                                    var_oc_cells.append((a + 1, b))
                                    var_oc_cells.append((a, b + 1))
                                    var_oc_cells.append((a + 1, b + 1))
                                    var_oc_cells.append((a - 1, b - 1))
                                    var_oc_cells.append((a - 1, b + 1))
                                    var_oc_cells .append((a + 1, b - 1))
                                break
                            else:
                                continue
                        elif next_direction == 'down':
                            if (a - 1, b) not in var_oc_cells:
                                self.middle_ship_coordinates.append((a, b))
                                a, b = a - 1, b
                                self.middle_ship_coordinates.append((a, b))
                                for i in self.middle_ship_coordinates:
                                    var_oc_cells .append(i)
                                    a, b = i
                                    var_oc_cells.append((a - 1, b))
                                    var_oc_cells.append((a, b - 1))
                                    var_oc_cells.append((a + 1, b))
                                    var_oc_cells.append((a, b + 1))
                                    var_oc_cells.append((a + 1, b + 1))
                                    var_oc_cells.append((a - 1, b - 1))
                                    var_oc_cells.append((a - 1, b + 1))
                                    var_oc_cells .append((a + 1, b - 1))
                                break
                            else:
                                continue
                    elif direction == 'horizontal':
                        next_direction = random.choice(['left', 'right'])
                        if next_direction == 'left':
                            if (a, b - 1) not in var_oc_cells:
                                self.middle_ship_coordinates.append((a, b))
                                a, b = a, b - 1
                                self.middle_ship_coordinates.append((a, b))
                                for i in self.middle_ship_coordinates:
                                    var_oc_cells .append(i)
                                    a, b = i
                                    var_oc_cells.append((a - 1, b))
                                    var_oc_cells.append((a, b - 1))
                                    var_oc_cells.append((a + 1, b))
                                    var_oc_cells.append((a, b + 1))
                                    var_oc_cells.append((a + 1, b + 1))
                                    var_oc_cells.append((a - 1, b - 1))
                                    var_oc_cells.append((a - 1, b + 1))
                                    var_oc_cells .append((a + 1, b - 1))
                                break
                            else:
                                continue
                        elif next_direction == 'right':
                            if (a, b + 1) not in var_oc_cells:
                                self.middle_ship_coordinates.append((a, b))
                                a, b = a, b + 1
                                self.middle_ship_coordinates.append((a, b))
                                for i in self.middle_ship_coordinates:
                                    var_oc_cells .append(i)
                                    a, b = i
                                    var_oc_cells.append((a - 1, b))
                                    var_oc_cells.append((a, b - 1))
                                    var_oc_cells.append((a + 1, b))
                                    var_oc_cells.append((a, b + 1))
                                    var_oc_cells.append((a + 1, b + 1))
                                    var_oc_cells.append((a - 1, b - 1))
                                    var_oc_cells.append((a - 1, b + 1))
                                    var_oc_cells.append((a + 1, b - 1))
                                break
                            else:
                                continue
                else:
                    continue
        return var_oc_cells, self.middle_ship_coordinates
class LittleShip:
    def __init__(self):
        self.little_ship_coordinates = []
    def generation(self, var_oc_cells):
        while len(self.little_ship_coordinates) != 3:
            while True:
                a = random.randint(0, 6)
                b = random.randint(0, 6)
                if (a, b) not in var_oc_cells:
                    self.little_ship_coordinates.append((a, b))
                    var_oc_cells.append((a, b))
                    var_oc_cells.append((a - 1, b))
                    var_oc_cells.append((a, b - 1))
                    var_oc_cells.append((a + 1, b))
                    var_oc_cells.append((a, b + 1))
                    var_oc_cells.append((a + 1, b + 1))
                    var_oc_cells.append((a - 1, b - 1))
                    var_oc_cells.append((a - 1, b + 1))
                    var_oc_cells.append((a + 1, b - 1))
                    break
                else:
                    continue
        return var_oc_cells, self.little_ship_coordinates

class BigShip:
    def __init__(self):
        self.big_ship_coordinates = []
        self.occupied_cells = []
    def generation(self):
        a = random.randint(2, 4)
        b = random.randint(2, 4)
        self.big_ship_coordinates.append((a, b))
        direction = random.choice(['vertical', 'horizontal'])
        if direction == 'vertical':
            next_direction = random.choice(['up', 'down'])
            if next_direction == 'up':
                a, b = a + 1, b
                self.big_ship_coordinates.append((a, b))
                a, b = a + 1, b
                self.big_ship_coordinates.append((a, b))
            elif next_direction == 'down':
                a, b = a - 1, b
                self.big_ship_coordinates.append((a, b))
                a, b = a - 1, b
                self.big_ship_coordinates.append((a, b))
        elif direction == 'horizontal':
            next_direction = random.choice(['left', 'right'])
            if next_direction == 'left':
                a, b = a, b - 1
                self.big_ship_coordinates.append((a, b))
                a, b = a, b - 1
                self.big_ship_coordinates.append((a, b))
            elif next_direction == 'right':
                a, b = a, b + 1
                self.big_ship_coordinates.append((a, b))
                a, b = a, b + 1
                self.big_ship_coordinates.append((a, b))
        for i in self.big_ship_coordinates:
            self.occupied_cells.append(i)
            a, b = i
            self.occupied_cells.append((a - 1, b))
            self.occupied_cells.append((a, b - 1))
            self.occupied_cells.append((a + 1, b))
            self.occupied_cells.append((a, b + 1))
            self.occupied_cells.append((a + 1, b + 1))
            self.occupied_cells.append((a - 1, b - 1))
            self.occupied_cells.append((a - 1, b + 1))
            self.occupied_cells.append((a + 1, b - 1))
        var_oc_cells = self.occupied_cells
        var_b_s_coordinates = self.big_ship_coordinates
        var_oc_cells, var_m_s_coordinates = MiddleShip().generation(var_oc_cells)
        var_oc_cells, var_l_s_coordinates = LittleShip().generation(var_oc_cells)
        adding_coordinates(var_b_s_coordinates, var_m_s_coordinates, var_l_s_coordinates)

        


