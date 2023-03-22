import pygame
import numpy as np
import pyrr
import math


class Camera:
    def __init__(self, position=[0, 0, -3], rotation=[0, 0, math.pi], zoom=1):
        self.position = np.array(position)
        self.rotation = np.array(rotation)
        self.rotation_speed = 1/180
        self.orbit_fulcrum = np.array([0, 0, 0])
        self.facing = np.array([0, 0, -1])
        self.up = np.array([0, 1, 0])
        self.right = np.array([1, 0, 0])
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
                    self.orbit_around_fulcrum(x_rel, y_rel)
                self.pressed = True
            else:
                self.pressed = False

    def zoom_control(self, event):
        if event.type == pygame.MOUSEWHEEL:
            self.zoom = self.zoom * (1 - event.y / 20)

    def orbit_around_fulcrum(self, delta_x, delta_y, sensitivity=0.005):
        # Calculate the vector from the fulcrum to the camera position
        vector_to_camera = self.position - self.orbit_fulcrum

        # Rotate around the vertical axis (Y-axis)
        rotation_y = pyrr.Matrix44.from_eulers((0, 0, delta_x * sensitivity), dtype='float32')
        vector_to_camera = pyrr.matrix44.apply_to_vector(rotation_y, vector_to_camera)

        # Rotate around the horizontal axis (camera's right vector)
        right_vector = np.cross(self.facing, [0, 1, 0])
        right_vector = pyrr.vector3.normalize(right_vector)
        rotation_matrix_right = pyrr.matrix44.create_from_axis_rotation(right_vector, delta_y * sensitivity,
                                                                        dtype='float32')
        vector_to_camera = pyrr.matrix44.apply_to_vector(rotation_matrix_right, vector_to_camera)

        # Add the rotated vector to the fulcrum position to get the new camera position
        self.position = self.orbit_fulcrum + vector_to_camera

        # Update the facing vector
        self.facing = -pyrr.vector3.normalize(self.orbit_fulcrum - self.position)
        self.right = -pyrr.vector3.normalize(np.cross(self.facing, np.array([0, 1, 0])))
        self.up = -pyrr.vector3.normalize(np.cross(self.right, self.facing))
        print(f'facing: {self.facing}')
        print(f'right: {self.right}')
        print(f'up: {self.up}')

    def translate(self, translation_vector):
        self.position = self.position + np.array(translation_vector)


    def create_view_matrix(self):
        # Calculate the camera's rotation matrix
        rotation_matrix = self.create_rotation_matrix()

        # Calculate the camera's translation matrix
        translation_matrix = pyrr.matrix44.create_from_translation(self.position, dtype='float32')

        # Calculate the view matrix (inverse of the camera's model matrix)
        view_matrix = pyrr.matrix44.multiply(rotation_matrix, translation_matrix)
        view_matrix = pyrr.matrix44.inverse(view_matrix)

        return view_matrix

    def create_rotation_matrix(self):
        rotation_matrix = np.column_stack((self.right, self.up, self.facing, [0, 0, 0]))
        rotation_matrix = np.append(rotation_matrix, [[0, 0, 0, 1]], 0)
        print(rotation_matrix)

        # Transpose the matrix to obtain the final rotation matrix
        rotation_matrix = np.transpose(rotation_matrix)
        return rotation_matrix
