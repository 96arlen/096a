class Transport:
    def __init__(self, spd, cap):
        self.spd = spd
        self.cap = cap

    def travel_time(self, dist):
        return dist / self.spd


class Bus(Transport): pass
class Train(Transport): pass
class Airplane(Transport):
    def travel_time(self, dist):
        return super().travel_time(dist) * 0.8


d = 600
print(Bus(50, 40).travel_time(d))
print(Train(150, 180).travel_time(d))
print(Airplane(900, 160).travel_time(d))
