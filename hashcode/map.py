#!/usr/bin/env python3
__author__ = 'Dewep'


class Case(object):

    def __init__(self, _map, altitude, pos_y, pos_x, vector_y, vector_x):
        self.map = _map
        self.altitude = altitude
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.vector_y = vector_y
        self.vector_x = vector_x


class Map(object):

    def __init__(self, hashcode):
        self.hashcode = hashcode
        self.altitudes = [[[None] * self.hashcode.max_x] * self.hashcode.max_y] * self.hashcode.max_altitude

    def init_case(self, altitude, pos_y, pos_x, vector_y, vector_x):
        self.altitudes[altitude][pos_y][pos_x] = Case(self, altitude, pos_y, pos_x, vector_y, vector_x)
