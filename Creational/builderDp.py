# Abstract course
class Course:

    def __init__(self):
        self.Fee()
        self.available_batches()

    def Fee(self):
        raise NotImplementedError

    def available_batches(self):
        raise NotImplementedError


# concrete course
class DSA(Course):
    """Class for Data Structures and Algorithms"""

    def Fee(self):
        self.fee = 8000

    def available_batches(self):
        self.batches = 5

    def __str__(self):
        return "DSA"


# concrete course
class SDE(Course):
    """Class for Software Development Engineer"""

    def Fee(self):
        self.fee = 10000

    def available_batches(self):
        self.batches = 4

    def __str__(self):
        return "SDE"


# concrete course
class STL(Course):
    """Class for Standard Template Library"""

    def Fee(self):
        self.fee = 5000

    def available_batches(self):
        self.batches = 7

    def __str__(self):
        return "STL"


class Temp(Course):
    def __str__(self):
        return "Temp"

class CourseDetails:
    def get_course_details(self, sub):
        print('Course : {0} | Fee : {0.fee} | Batches Available : {0.batches}'.format(sub))


# main method
if __name__ == "__main__":
    dsa = DSA()  # object for DSA course
    sde = SDE()  # object for SDE course
    stl = STL()  # object for STL course

    cd = CourseDetails()
    cd.get_course_details(dsa)
    # complex_course = construct_course(Complexcourse)
    # print(complex_course)