import pygame
import numpy as np
import pyrr
import math


class Camera:
    def __init__(self, position=[0, 0, -5], rotation=[0, 0, math.pi], zoom=1):
        self.position = position
        self.rotation = rotation
        self.zoom = zoom
        self.pressed = False

    def camera_control(self):
        keys = pygame.key.get_pressed()

        # Translate
        if keys[pygame.K_w]:
            self.translate([0, 0, 0.1])
        if keys[pygame.K_s]:
            self.translate([0, 0, -0.1])
        if keys[pygame.K_a]:
            self.translate([0.1, 0, 0])
        if keys[pygame.K_d]:
            self.translate([-0.1, 0, 0])


    def orbit_control(self, event):
        # Process mouse motion events for rotation
        if event.type == pygame.MOUSEMOTION:
            x_rel, y_rel = event.rel
            if pygame.mouse.get_pressed()[0]:  # Left mouse button is pressed
                if self.pressed:
                    self.rotate(x_rel, y_rel)
                self.pressed = True
            else:
                self.pressed = False

    def translate(self, translation_vector):
        self.position = self.position + np.array(translation_vector)

    def rotate(self, yaw, pitch):
        self.rotation = self.rotation + np.array([-pitch/180, 0.0, yaw/180])

    def create_view_matrix(self):
        # Calculate the camera's rotation matrix
        rotation_matrix = pyrr.matrix44.create_from_eulers(self.rotation, dtype='float32')

        # Calculate the camera's translation matrix
        translation_matrix = pyrr.matrix44.create_from_translation(self.position, dtype='float32')

        # Calculate the view matrix (inverse of the camera's model matrix)
        view_matrix = pyrr.matrix44.multiply(rotation_matrix, translation_matrix)
        view_matrix = pyrr.matrix44.inverse(view_matrix)

        return view_matrix
