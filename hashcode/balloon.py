#!/usr/bin/env python3
__author__ = 'Dewep'


from math import pow, fabs


class Balloon(object):

    def __init__(self, hashcode, _id):
        self.hashcode = hashcode
        self.id = _id
        self.altitude = 0
        self.x = self.hashcode.start_x
        self.y = self.hashcode.start_y
        self.movements = list()
        self.is_lost = False

    def _is_target_covered_by_balloon(self, target):
        if fabs(target.y - self.y) > self.hashcode.radius:
            return False
        if min(fabs(target.x - self.x), fabs(self.hashcode.max_x - fabs(target.x - self.x))) > self.hashcode.radius:
            return False
        dist = min(fabs(self.x - target.x), self.hashcode.max_x - fabs(self.x - target.x))
        tmp = pow(self.y - target.y, 2) + pow(dist, 2)
        return tmp <= pow(self.hashcode.radius, 2)

    def move(self, move):
        if self.is_lost:
            return
        self.movements.append(move)
        if move == -1 and self.altitude <= 1:
            raise Exception("Can't down")
        if move == 1 and self.altitude == self.hashcode.max_altitude - 1:
            raise Exception("Can't up")
        self.altitude += move
        if self.altitude > 0:
            self.y, self.x = self.hashcode.map.altitudes[self.altitude][self.y][self.x].get_next()
            if self.y < 0 or self.y >= self.hashcode.max_y:
                self.is_lost = True

    def get_movement(self, tour):
        if tour < len(self.movements):
            return self.movements[tour]
        return 0

    def score(self, targets):
        score = 0
        if self.altitude > 0:
            for target in targets[:]:
                if self._is_target_covered_by_balloon(target):
                    targets.remove(target)
                    score += 1
        return score
