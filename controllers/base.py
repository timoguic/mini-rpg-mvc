import pygame


class PygameController:
    def _run_loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    return False
                elif event.type == pygame.locals.KEYDOWN:
                    if event.key == pygame.locals.K_ESCAPE:
                        return False
                elif event.type == pygame.locals.MOUSEBUTTONDOWN:
                    return event.pos
