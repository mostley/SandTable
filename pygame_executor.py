""" visualizes movements with pygame """
import pygame, math


class PygameExecutor:
    """ Executor that visualizes the movements with pygame """

    def __init__(self):
        self.screen = None
        self.lines = []
        self.diameter = 800
        self.center_point = (self.diameter/2, self.diameter/2)
        self.current_angle = 0
        self.current_slider_pos = 0
        self.current_pos = (0, 0)
        self.rotation_speed = 5
        self.slider_speed = 5
        self.error = None
        self.fatal = None

    def setup(self):
        """ sets up the executor """
        pygame.init()
        self.screen = pygame.display.set_mode((self.diameter, self.diameter))

    def calculate_cartesian(self):
        """ calculates the cartesian coordinates from polar coordinates """
        return (
            self.center_point[0] + self.current_slider_pos * math.cos(self.current_angle),
            self.center_point[1] + self.current_slider_pos * math.sin(self.current_angle)
        )

    def add_movement(self, movement):
        """ adds the movement to the current position """
        self.current_slider_pos += movement.distance_delta * self.rotation_speed
        self.current_angle += movement.angle_delta * self.slider_speed

    def execute(self, movement):
        """ executes the movement and updates the visualization """
        print("Execute " + str(movement))
        current_pos = self.calculate_cartesian()
        self.add_movement(movement)
        new_pos = self.calculate_cartesian()

        line = (current_pos, new_pos)
        self.lines.append(line)
        self.update()

    def drawLine(self, line):
        """ draws a line """
        pygame.draw.line(self.screen, (255,255,255), line[0], line[1], 1)

    def update(self):
        """ redraws the screen """
        self.screen.fill((0, 0, 0))
        for line in self.lines:
            self.drawLine(line)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.fatal = 'USER_QUIT'
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.fatal = 'USER_QUIT'
