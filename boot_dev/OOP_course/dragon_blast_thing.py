class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        if self.pos_x >= x_1 and self.pos_x <= x_2:
            if self.pos_y >= y_1 and self.pos_y <= y_2:
                return True
        return False


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        fire_range = self.__fire_range
        units_reached = []

        for unit in units:
            unit_x = unit.pos_x
            unit_y = unit.pos_y
            for i in range((x - fire_range), (x + fire_range) + 1):
                for j in range((y - fire_range), (y + fire_range) + 1):
                    if super().in_area(i, j, unit_x, unit_y):
                        units_reached.append(unit)

        print(units_reached)
        # super().in_area(x, y, unit_x, unit_y)


units = [Unit("Cian", 3, 3), Unit("Andrew", -1, 4), Unit("Baran", -6, 5)]

drake = Dragon("Draco", 2, 2, 3)

print(drake.breathe_fire(2, 3, units))
