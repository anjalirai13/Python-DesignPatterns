class Home(object):
    def __init__(self):
        pass

    def work_on_hvac(self, hvac):
        print("Work done in home by {}".format(hvac))

    def work_on_electricity(self, electrician):
        print("Work done in home by {}".format(electrician))

    def accept(self, worker):
        worker.visit(self)

    def __str__(self):
        return self.__class__.__name__


class Visitor(object):
    def __str__(self):
        return self.__class__.__name__


class  HvacSpecialist(Visitor):
    def visit(self, house):
        house.work_on_hvac(self)


class Electrician(Visitor):
    def visit(self, house):
        house.work_on_electricity(self)


hv = HvacSpecialist()
e = Electrician()

h = Home()
h.accept(hv)
h.accept(e)