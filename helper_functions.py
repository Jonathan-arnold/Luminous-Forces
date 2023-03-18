import numpy as np
import pyrr


# takes the file path of a shader, reads its content, and returns it as a string
def load_shader(shader_file):
    with open(shader_file, "r") as file:
        return file.read()


def triangle():
    vertices = np.array([
        -0.5, -0.5, 0.0,  # Bottom-left vertex
        0.5, -0.5, 0.0,  # Bottom-right vertex
        0.0, 0.5, 0.0,  # Top vertex
    ], dtype='f4')

    return vertices


def create_perspective_projection_matrix(fov, aspect_ratio, near_plane, far_plane):
    projection_matrix = pyrr.matrix44.create_perspective_projection_matrix(fov, aspect_ratio,
                                                                           near_plane, far_plane)
    return projection_matrix

