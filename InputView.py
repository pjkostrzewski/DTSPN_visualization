from helpers import *
from AppView import AppView


class InputView(AppView):

    def __init__(self):
        super().__init__()
        self.radius = RADIUS_START
        self.turn = TURN_START

    def run(self):
        running = True
        while running:
            ev = pygame.event.get()
            for event in ev:
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    self.points.append((pos, self.radius))
                if event.type == pygame.KEYDOWN:
                    self._navigate(event)
                    if event.key == pygame.K_RETURN and self.points:
                        running = False
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill(BACK_COLOR)
            radius_text = self.font.render("promien punktu: {}, promień skrętu: {}".format(self.radius, self.turn),
                                           True, COLOR_ACTIVE)
            self.screen.blit(radius_text, (20, 20))
            self.car.display()
            self.draw_points()
            pygame.display.update()
        pygame.event.clear()
        self.file_manager.write_dtspn_input(self.turn, self.car, self.points)

    def _navigate(self, event):
        if event.key == pygame.K_UP:
            self.radius += 5
        elif event.key == pygame.K_DOWN:
            self.radius -= 5
        elif event.key == pygame.K_LEFT:
            self.turn -= 1
        elif event.key == pygame.K_RIGHT:
            self.turn += 1
        elif event.key == pygame.K_w:
            self.car.y -= 10
        elif event.key == pygame.K_s:
            self.car.y += 10
        elif event.key == pygame.K_a:
            self.car.x -= 10
        elif event.key == pygame.K_d:
            self.car.x += 10
        elif event.key == pygame.K_q:
            self.car.rotate(-10)
        elif event.key == pygame.K_e:
            self.car.rotate(10)
