from Car import Car
from math import pi


class FilesOperations(object):

    DUBINS_FILE = "DubinsPath.txt"
    DTSPN_FILE = "DTSPN_input.txt"
    path = "../../build"

    def get_dubins_data(self):
        with open(self.path + f"/{self.DUBINS_FILE}", "r") as f:
            return [[float(x) for x in line.split()] for line in f.readlines()]

    def write_dtspn_input(self, turn, car: Car, points):
        print("CAR ROTATION", car.rotation, (180-car.rotation)+180)
        with open(self.path + f"/{self.DTSPN_FILE}", "w") as f:
            f.writelines(
                [
                    str(turn)+"\n",
                    "{} {} {}\n".format(car.x, car.y, ((180-car.rotation)+180) * pi / 180)  # mirroring, quick fix
                    ]
                )
            for xy, rotation in points:
                x, y = xy
                f.writelines("{} {} {}\n".format(x, y, rotation))

