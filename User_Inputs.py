import pygame


class User_Inputs:
    def __init__(self, app):
        self.pressed = False
        self.app = app

    def event_handling(self):
        # Handle wasd controls to translate the fulcrum and camera on the xz axis
        self.translate_control()

        running = True
        for event in pygame.event.get():
            # check if the app has been quit
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            # check if the mouse has moved for orbit control
            elif event.type == pygame.MOUSEMOTION:
                self.orbit_control(event)

            # check if the mousewheel has turned for zoom control
            elif event.type == pygame.MOUSEWHEEL:
                self.app.camera.zoom_control(event)
        return running

    def orbit_control(self, event):
        # Process mouse motion events for rotation
        x_rel, y_rel = event.rel
        if pygame.mouse.get_pressed()[0]:  # Left mouse button is pressed
            if self.pressed:
                self.app.camera.orbit_around_fulcrum(x_rel, y_rel)
            self.pressed = True
        else:
            self.pressed = False

    def translate_control(self):
        keys = pygame.key.get_pressed()

        # Translate
        if keys[pygame.K_w]:
            self.app.camera.translate([0, 0, 0.1])
        if keys[pygame.K_s]:
            self.app.camera.translate([0, 0, -0.1])
        if keys[pygame.K_a]:
            self.app.camera.translate([0.1, 0, 0])
        if keys[pygame.K_d]:
            self.app.camera.translate([-0.1, 0, 0])
