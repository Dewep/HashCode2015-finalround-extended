#!/usr/bin/env python3
__author__ = 'Dewep'


from hashcode.balloon import Balloon
from hashcode.target import Target
from hashcode.map import Map


class HashCode(object):

    def __init__(self, file):

        # Initialise variables
        self.max_y, self.max_x, self.max_altitude = (None, None, None)
        self.nb_targets, self.radius, self.nb_balloons, self.nb_tours = (None, None, None, None)
        self.start_y, self.start_x = (None, None)
        self.map = None
        self.balloons = list()
        self.targets = list()

        # Parse
        self._parse(file)

    def _parse(self, file):

        with open(file, "r") as f:
            # Parse configurations
            self.max_y, self.max_x, self.max_altitude = map(int, f.readline().split())
            self.nb_targets, self.radius, self.nb_balloons, self.nb_tours = map(int, f.readline().split())
            self.start_y, self.start_x = map(int, f.readline().split())

            # Generate Map
            self.map = Map(self)

            # Parse Balloons
            for b in range(0, self.nb_balloons):
                self.balloons.append(Balloon(self, b))

            # Parse Targets
            for i in range(0, self.nb_targets):
                tmp_y, tmp_x = map(int, f.readline().split())
                self.targets.append(Target(self, tmp_y, tmp_x))

            # Set vectors
            for altitude in range(0, self.max_altitude):
                for y in range(0, self.max_y):
                    vectors = list(map(int, f.readline().split()))
                    index = 0
                    for x in range(0, self.max_x):
                        self.map.init_case(altitude, y, x, vectors[index + 1], vectors[index])
                        index += 2

    def format(self, file):
        with open(file, "w") as f:
            for tour in range(0, self.nb_tours):
                res = []
                for balloon in self.balloons:
                    res.append(str(balloon.get_movement(tour)))
                print(" ".join(res), file=f)

