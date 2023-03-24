import pygame


class UserInputs:
    def __init__(self, app, event_manager):
        self.pressed = False
        self.event_manager = event_manager
        self.app = app

    def event_handling(self):
        # Handle wasd controls to translate the fulcrum and camera on the xz axis
        self.translate_control()

        for event in pygame.event.get():
            self.event_manager.propagate_event(event)

    def translate_control(self):
        keys = pygame.key.get_pressed()

        # Translate
        if keys[pygame.K_w]:
            self.app.cameras[self.app.active_camera].translate([0, 0, 0.1])
        if keys[pygame.K_s]:
            self.app.cameras[self.app.active_camera].translate([0, 0, -0.1])
        if keys[pygame.K_a]:
            self.app.cameras[self.app.active_camera].translate([0.1, 0, 0])
        if keys[pygame.K_d]:
            self.app.cameras[self.app.active_camera].translate([-0.1, 0, 0])
