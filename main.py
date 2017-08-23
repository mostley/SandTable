"""
Main class
"""
from pygame_executor import PygameExecutor
import random, math

class Movement:
    """ represents a movement """

    def __init__(self, angle_delta, distance_delta):
        self.angle_delta = self.clamp(angle_delta)
        self.distance_delta = self.clamp(distance_delta)

    def clamp(self, value):
        """ clamps a value in between -1 and 1 """
        return max(-1, min(value, 1))

    def __str__(self):
        return "[" + str(self.angle_delta) + ":" + str(self.distance_delta) + "]"


class TestModule:
    """ a test module """

    def __init__(self):
        self.length = 600
        self.name = "Test Module"

    def tick(self, i, pos):
        """ execute a single tick, returns a Movement """
        print("tick " + str(i))
        if i < self.length/2:
            return Movement(0.001, 0.001)
        else:
            return Movement(-360.0/self.length, math.sin(i)/40)


class Main:
    """
    Handles sand modules
    """

    def __init__(self):
        self.running = False
        self.modules = []
        self.current_module = None
        self.current_pos = None
        self.executor = PygameExecutor()

    def add_module(self, module):
        """ add a module to execution """
        self.modules.append(module)

    def get_next_module(self):
        """ returns a random next module """
        return self.modules[random.choice(range(len(self.modules)))]

    def execute_module(self):
        """ execute a module """

        print("Execute Module '" + self.current_module.name + "'")

        for i in range(self.current_module.length):
            movement = self.current_module.tick(i, self.current_pos)
            self.current_pos = self.executor.execute(movement)

            if self.executor.error:
                print("[ERROR] Encountered error, stopping execution of module '" + self.executor.fatal + "'")
                break

            if self.executor.fatal:
                print("[FATAL] Encountered fatal error, stopping execution of sandtable '" + self.executor.fatal + "'")
                self.running = False
                break
        
        self.current_module = None

    def run(self):
        """ starts the execution """
        if len(self.modules) <= 0:
            print("No modules loaded!")
            return

        self.running = True

        self.executor.setup()

        while self.running:
            if not self.current_module:
                self.current_module = self.get_next_module()
                self.executor.reset()

            self.execute_module()



if __name__ == '__main__':
    print("Starting Sandtable")
    MAIN = Main()
    for i in range(10):
        MAIN.add_module(TestModule())
    MAIN.run()
