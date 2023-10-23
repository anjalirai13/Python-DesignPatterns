import time

class Producer:
    def produce(self):
        print("Producer is working hard")

    def meet(self):
        print("Producer has time to meet you")

class Proxy:
    def __init__(self):
        self.occupied = "No"
        self.producer = None

    def produce(self):
        if self.check_status():
            self.producer.produce()
        else:
            print("Producer is busy")

    def meet(self):
        if self.check_status():
            self.producer.meet()
        else:
            print("Producer is busy")

    def check_status(self):
        print ("Checking if producer is available...")
        if self.producer is None:
            self.producer = Producer()
        time.sleep(2)
        if self.occupied == "No":
            return True
        return False

p = Proxy()
p.produce()
p.occupied = "Yes"
p.produce()

p.meet()
p.occupied = "No"
p.meet()
