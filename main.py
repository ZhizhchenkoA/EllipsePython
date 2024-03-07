import numpy as np


class Ellipse:

    def __init__(self, a=1.0, e=0.0, i=0.0, longitude=0.0, arg=0.0,
                 scale=1):
        self.a = a
        self.e = e
        self.i = i
        self.longitude = longitude
        self.arg = arg
        self.scale = scale
        self.r = []
        self.cords = []
        self.ellipse_r()
        self.ellipse_xy()
        self.v1 = np.array(
            [0, 0, 1])  # OZ
        self.v2 = np.array(
            [0, 0, 1])  # вектор нормали к плоскости эллипса
        self.v3 = np.array([0, 1, 0])  # ветор на восходящий узел


        self.set_arg(self.arg, True)
        self.set_long(self.longitude, True)
        self.set_i(self.i, True)
    def ellipse_r(self):
        phi = 0
        while phi <= np.pi * 2:
            self.r.append([self.a * (1 - self.e ** 2) / (
                        1 + self.e * np.cos(phi)), phi])
            phi += 0.01
        self.r.append([self.a * (1 - self.e ** 2) / (
                        1 + self.e * np.cos(0)), 0])

    def ellipse_xy(self):

        for i in self.r:

            self.cords.append(np.array(
                [i[0] * np.cos(i[1]), i[0] * np.sin(i[1]), 0]))

    def set_i(self, phi, first=False):
        phi0 = 0 if first else self.i
        for i in range(len(self.cords)):
            self.cords[i] = self.rotation(self.cords[i], self.v3,
                                          phi - phi0)
        self.v2 = self.rotation(self.v2, self.v3, phi - phi0)
        ...

    def set_arg(self, phi, first=False):
        phi0 = 0 if first else self.arg
        for i in range(len(self.cords)):
            self.cords[i] = self.rotation(self.cords[i], self.v2, phi - phi0)
        ...


    def set_long(self, phi, first=False):
        phi0 = 0 if first else self.longitude
        for i in range(len(self.cords)):
            self.cords[i] = self.rotation(self.cords[i], self.v1, phi - phi0)
        self.v3 = self.rotation(self.v3, self.v1, phi - phi0)
        self.v2 = self.rotation(self.v2, self.v1, phi - phi0)
        ...
    @staticmethod
    def rotation(xyz: np.array, v: np.array, phi):
        rot_mat = np.array(
            [[np.cos(phi) + (1 - np.cos(phi)) * v[0] ** 2,
              (1 - np.cos(phi)) * v[0] * v[1] - np.sin(phi) * v[2],
              (1 - np.cos(phi)) * v[0] * v[2] + np.sin(phi) * v[1]],

             [(1 - np.cos(phi)) * v[1] * v[0] + np.sin(phi) * v[2],
              np.cos(phi) + (1 - np.cos(phi)) * v[1] ** 2,
              (1 - np.cos(phi)) * v[1] * v[2] - np.sin(phi) * v[0]],

             [(1 - np.cos(phi)) * v[2] * v[0] - np.sin(phi) * v[1],
              (1 - np.cos(phi)) * v[2] * v[1] + np.sin(phi) * v[0],
              np.cos(phi) + (1 - np.cos(phi)) * v[2] ** 2]])
        return rot_mat @ xyz
