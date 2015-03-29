#!/usr/bin/env python3
__author__ = 'Dewep'


class Balloon(object):

    def __init__(self, hashcode, _id):
        self.hashcode = hashcode
        self.id = _id
        self.altitude = 0
        self.x = self.hashcode.start_x
        self.y = self.hashcode.start_y
        self.movements = list()

    def get_movement(self, tour):
        if tour < len(self.movements):
            return self.movements[tour]
        return 0
