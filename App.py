import pygame
import moderngl as mgl
import numpy as np
import pyrr
from pygame.locals import GL_CONTEXT_PROFILE_CORE, GL_CONTEXT_MAJOR_VERSION, GL_CONTEXT_MINOR_VERSION
from helper_functions import *


class App:
    def __init__(self, width, height, title):
        # Initialize Pygame
        pygame.init()

        # Set up the window
        self.width = width
        self.height = height
        self.title = title
        self.screen = pygame.display.set_mode((width, height), flags=pygame.OPENGL|pygame.GL_DOUBLEBUFFER)
        pygame.display.set_caption(title)
        pygame.display.gl_set_attribute(GL_CONTEXT_PROFILE_CORE, 1)
        pygame.display.gl_set_attribute(GL_CONTEXT_MAJOR_VERSION, 3)
        pygame.display.gl_set_attribute(GL_CONTEXT_MINOR_VERSION, 3)

        # Set up ModernGL context
        self.ctx = mgl.create_context(pygame.display.get_wm_info()['window'])


        # Initialize camera attributes
        self.camera_position = [0, 0, -5]
        self.camera_rotation = [0, 0, 0]
        self.camera_zoom = 1

        # Setup the opengl render pipeline
        self.setup_render_pipeline()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            # Update the camera and any other objects here

            # Clear the screen
            self.ctx.clear()

            # Render the triangle
            self.vao.render(mgl.TRIANGLES)

            pygame.display.flip()

        pygame.quit()

    def setup_render_pipeline(self):
        # Load shaders
        vertex_shader_source = load_shader("vertex_shader.glsl")
        fragment_shader_source = load_shader("fragment_shader.glsl")

        # Create a shader program
        self.shader_program = self.ctx.program(vertex_shader=vertex_shader_source,
                                               fragment_shader=fragment_shader_source)
        # Vertex data (x, y, z, r, g, b)
        vertices = np.array([
            -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,  # Bottom-left vertex (red)
            0.5, -0.5, 0.0, 0.0, 1.0, 0.0,  # Bottom-right vertex (green)
            0.0, 0.5, 0.0, 0.0, 0.0, 1.0,  # Top vertex (blue)
        ], dtype='float32')

        # Index data (defines the triangles)
        indices = np.array([
            0, 1, 2,  # Triangle connecting the three vertices
        ], dtype='uint32')

        # Create vertex buffer
        vertex_buffer = self.ctx.buffer(data=bytearray(vertices.tobytes()), dynamic=False)

        # Create index buffer
        index_buffer = self.ctx.buffer(data=bytearray(indices.tobytes()), dynamic=False)

        # Create a vertex array object (VAO)
        self.vao = self.ctx.vertex_array(self.shader_program, [(vertex_buffer, '3f 3f', 'in_vert', 'in_color')],
                                         index_buffer)

        # Create a perspective projection matrix
        fov = np.radians(60)
        aspect_ratio = self.width / self.height
        near_plane = 0.1
        far_plane = 100
        projection_matrix = pyrr.matrix44.create_perspective_projection_matrix(fov, aspect_ratio, near_plane, far_plane)

        # Pass the projection matrix to the shader
        self.shader_program['projection_matrix'].write(projection_matrix.astype('float32').tobytes())

        # Create a view matrix (identity matrix for now)
        view_matrix = pyrr.matrix44.create_look_at(self.camera_position, [0, 0, 0], [0, 1, 0])

        # Pass the view matrix to the shader
        self.shader_program['view_matrix'].write(view_matrix.astype('float32').tobytes())

