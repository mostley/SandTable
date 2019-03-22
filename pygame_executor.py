""" visualizes movements with pygame """
import pygame, math, random


class PygameExecutor:
    """ Executor that visualizes the movements with pygame """

    def __init__(self):
        self.screen = None
        self.current_line = None
        self.diameter = 800
        self.center_point = (self.diameter/2, self.diameter/2)
        self.current_angle = 0
        self.current_slider_pos = 0
        self.current_pos = (0, 0)
        self.rotation_speed = 0.1
        self.error = None
        self.fatal = None
        self.color = self.random_color()

        print("color: " + str(self.color[0]) + ":" + str(self.color[1]) + ":" + str(self.color[2]))

    def random_color(self):
        """ generates a random color """
        return (
            int(math.floor(random.random() * 255)),
            int(math.floor(random.random() * 255)),
            int(math.floor(random.random() * 255))
        )

    def reset(self):
        """ sets a new color """
        self.color = self.random_color()

    def setup(self):
        """ sets up the executor """
        pygame.init()
        self.screen = pygame.display.set_mode((self.diameter, self.diameter))
        self.screen.fill((0, 0, 0))

    def calculate_cartesian(self):
        """ calculates the cartesian coordinates from polar coordinates """
        return (
            self.center_point[0] + self.current_slider_pos * math.cos(self.current_angle),
            self.center_point[1] + self.current_slider_pos * math.sin(self.current_angle)
        )

    def add_movement(self, movement):
        """ adds the movement to the current position """
        self.current_slider_pos += movement.distance_delta * self.diameter/2.0
        self.current_angle += movement.angle_delta * 360

    def execute(self, movement):
        """ executes the movement and updates the visualization """
        print("Execute " + str(movement))
        current_pos = self.calculate_cartesian()
        self.add_movement(movement)
        new_pos = self.calculate_cartesian()

        self.current_line = (current_pos, new_pos)
        
        self.update()

        return (self.current_angle, self.current_slider_pos)

    def drawLine(self, line):
        """ draws a line """
        pygame.draw.line(self.screen, self.color, line[0], line[1], 1)

    def update(self):
        """ updates the screen """
        
        self.drawLine(self.current_line)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.fatal = 'USER_QUIT'
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.fatal = 'USER_QUIT'
