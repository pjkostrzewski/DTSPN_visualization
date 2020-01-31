from helpers import *
from AppView import AppView


class AnimationView(AppView):

    def __init__(self):
        super().__init__()

        self.route = []
        self.data = self.file_manager.get_dubins_data()
        self.delay = 60

    def draw_route(self):
        for r in self.route:
            pygame.draw.circle(self.screen, COLOR_ACTIVE, r, 2, 1)

    def run(self):
        running = True
        gen = (x for x in self.data)
        draw = True
        while running:
            ev = pygame.event.get()
            for event in ev:
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    self._navigate(event)
                    if event.key == pygame.K_ESCAPE:
                        running = False
            self.screen.fill(BACK_COLOR)
            speed_text = self.font.render("predkosc: {}".format(self.delay), True, COLOR_ACTIVE)
            self.screen.blit(speed_text, (20, 20))
            try:
                step = next(gen)
            except StopIteration:
                draw = False
            if draw:
                self.car.x += step[0]
                self.car.y += step[1]
                temp_x = copy.deepcopy(self.car.x)
                temp_y = copy.deepcopy(self.car.y)
                self.route.append((int(temp_x), int(temp_y)))
                rotation_degrees = convert_from_radians(step[2])
                self.car.rotate(rotation_degrees)
            self.draw_points()
            self.draw_route()
            self.car.display()
            pygame.display.update()
            self.clock.tick(self.delay)

    def _navigate(self, event):
        if event.key == pygame.K_UP:
            self.delay += 5
        if event.key == pygame.K_DOWN:
            self.delay -= 5
