#!/usr/bin/env python3
__author__ = 'Dewep'


from hashcode.balloon import Balloon
from hashcode.target import Target
from hashcode.map import Map


class HashCode(object):

    def __init__(self, file):

        # Initialise variables
        self.max_y, self.max_x, self.max_altitude = (0, 0, 0)
        self.nb_targets, self.radius, self.nb_balloons, self.nb_tours = (0, 0, 0, 0)
        self.start_y, self.start_x = (0, 0)
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
            for altitude in range(1, self.max_altitude):
                for y in range(0, self.max_y):
                    vectors = list(map(int, f.readline().split()))
                    index = 0
                    for x in range(0, self.max_x):
                        self.map.init_case(altitude, y, x, vectors[index], vectors[index + 1])
                        index += 2

    def format(self, file):
        with open(file, "w") as f:
            for tour in range(0, self.nb_tours):
                res = []
                for balloon in self.balloons:
                    res.append(str(balloon.get_movement(tour)))
                print(" ".join(res), file=f)

    def score(self, file):

        with open(file, "r") as f:
            score = 0

            for tour in range(0, self.nb_tours):
                moves = list(map(int, f.readline().split()))
                assert (len(moves) == self.nb_balloons), "#%d: Bad number of balloons" % tour
                targets = self.targets[:]

                for index in range(0, self.nb_balloons):
                    balloon = self.balloons[index]
                    move = moves[index]
                    assert (move in [-1, 0, 1]), "#%d: Bad value for a move" % tour

                    if not balloon.is_lost:
                        assert (move != -1 or balloon.altitude > 1), "#%d: Can't down" % tour
                        assert (move != 1 or balloon.altitude + 1 < self.max_altitude), "#%d: Can't up" % tour
                        balloon.move(move)
                        if balloon.is_lost:
                            print("#%d: Balloon %d lost" % (tour, index))
                        else:
                            score += balloon.score(targets)

                print("\tScore #%d: %d" % (tour, score))

            print("\nFinal score: %d" % score)
            return score
