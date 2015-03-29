#!/usr/bin/env python3
__author__ = 'Dewep'


class Case(object):

    def __init__(self, _map, altitude, y, x, vector_y, vector_x):
        self.map = _map
        self.altitude = altitude
        self.y = y
        self.x = x
        self.vector_y = vector_y
        self.vector_x = vector_x

    def get_next(self):
        return self.y + self.vector_y, (self.x + self.vector_x) % self.map.hashcode.max_x


class Map(object):

    def __init__(self, hashcode):
        self.hashcode = hashcode
        self.altitudes = list()
        self.altitudes = [[[None for _ in range(0, self.hashcode.max_x)] for _ in range(0, self.hashcode.max_y)]
                          for _ in range(0, self.hashcode.max_altitude)]

    def init_case(self, altitude, y, x, vector_y, vector_x):
        self.altitudes[altitude][y + 0][x] = Case(self, altitude, y + 0, x, vector_y, vector_x)
