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
        self.setup_window(width, height, title)
        self.setup_program()

    def setup_window(self, width, height, title):
        # Set up the window
        self.width = width
        self.height = height
        self.title = title
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
        pygame.display.gl_set_attribute(GL_CONTEXT_MAJOR_VERSION, 3)
        pygame.display.gl_set_attribute(GL_CONTEXT_MINOR_VERSION, 3)
        self.screen = pygame.display.set_mode((width, height), flags=pygame.OPENGL | pygame.GL_DOUBLEBUFFER)
        pygame.display.set_caption(title)

    def setup_program(self):
        vertex_shader = load_shader('vertex_shader.glsl')
        fragment_shader = load_shader('fragment_shader.glsl')

        self.ctx = mgl.create_context()

        # Create a shader program
        self.shader_program = self.ctx.program(vertex_shader=vertex_shader,
                                               fragment_shader=fragment_shader)
        print(self.shader_program)

    def setup_vertex_buffer(self):
        vertices = np.array([
            -0.5, -0.5, 0.0,  # Bottom-left vertex
            0.5, -0.5, 0.0,  # Bottom-right vertex
            0.0, 0.5, 0.0,  # Top vertex
        ], dtype='float32')

        self.vertex_buffer = self.ctx.buffer(data=bytearray(vertices.tobytes()), dynamic=False)

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            pygame.display.flip()

        pygame.quit()
