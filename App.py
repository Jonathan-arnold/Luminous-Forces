import pygame
import moderngl as mgl
import numpy as np
import pyrr
from pygame.locals import GL_CONTEXT_PROFILE_CORE, GL_CONTEXT_MAJOR_VERSION, GL_CONTEXT_MINOR_VERSION
from helper_functions import *
from Camera import *
from UserInputs import *
from EventManager import *
from EventHandler import *


class App(EventHandler):
    def __init__(self, width, height, title):
        # Initialize Pygame
        pygame.init()

        # Set up a window with pygame and configure it for opengl. This
        # includes setting the version number of opengl using the core
        # profile, and using the OPENGL and DOUBLEBUF flags for the display
        # mode.
        self.setup_window(width, height, title)

        # Set up the moderngl rendering pipeline. See internal comments.
        self.create_program()

        # Create a vertex buffer - a structure that we load vertex data into in
        # preparation for passing it to the gpu.
        self.create_vertex_buffer(triangle())

        # Create an index buffer - this will tell the gpu how to assemble triangles
        # from the vertices
        self.create_index_buffer([[0, 1, 2], [3, 4, 5]])

        # Create a vertex array - this will create a relationship between the data
        # in the vertex buffer and the vertex attributes, which tell the gpu how to
        # interpret the data in the buffer. e.g. the first three values are
        # position, the next three are color, then that repeats.
        self.create_vertex_array()

        # Create a User_Inputs object to handle inputs from the user
        self.event_manager = EventManager()
        self.user_inputs = UserInputs(self, self.event_manager)
        self.event_manager.register_listener(pygame.QUIT, self)
        self.event_manager.register_listener(pygame.KEYDOWN, self)

        # Create a list of cameras. This allows us to change the position and
        # orientation of the user's perspective.
        self.cameras = {
            'main_camera': Camera(self),
            'secondary_camera': Camera(self, [-10, 0, 0], [-1, 0, 0], 2)
        }
        self.active_camera = 'main_camera'
        # Activate the main camera
        self.cameras[self.active_camera].toggle()

        # Initialize the pygame clock
        self.clock = pygame.time.Clock()

        # Initialize the running variable
        self.running = False

    def handle_event(self, event):
        # Check if the user has quit the app
        if event.type == pygame.QUIT:
            self.running = False

        if event.type == pygame.KEYDOWN:
            # Check if the user has quit the app
            if event.key == pygame.K_ESCAPE:
                self.running = False

            # Check if the camera has been changed
            if event.key == pygame.K_0:
                self.switch_camera('main_camera')
            if event.key == pygame.K_1:
                self.switch_camera('secondary_camera')

    def switch_camera(self, camera_name):
        # Deactivate the currently active camera and activate the given camera
        if camera_name in self.cameras:
            self.cameras[self.active_camera].toggle()
            self.active_camera = camera_name
            self.cameras[self.active_camera].toggle()


    def setup_window(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        pygame.display.gl_set_attribute(GL_CONTEXT_MAJOR_VERSION, 3)
        pygame.display.gl_set_attribute(GL_CONTEXT_MINOR_VERSION, 3)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
        self.screen = pygame.display.set_mode((width, height), flags=pygame.OPENGL | pygame.DOUBLEBUF)
        pygame.display.set_caption(title)

    def create_program(self):
        # import our shaders and save them as string variables
        vertex_shader = load_shader('vertex_shader.glsl')
        fragment_shader = load_shader('fragment_shader.glsl')

        # this creates an opengl context which is like initializing opengl, so we
        # can use it.
        self.ctx = mgl.create_context()

        # Create a shader program - this compiles and connects our shaders for use
        self.shader_program = self.ctx.program(vertex_shader=vertex_shader,
                                               fragment_shader=fragment_shader)

        # Create a projection matrix that will transform objects from world space to camera space
        projection_matrix = create_perspective_projection_matrix(60, self.width / self.height, 0.1, 100)
        self.shader_program['projection_matrix'].write(projection_matrix.astype('float32').tobytes())

    def create_vertex_buffer(self, vertices):
        # Convert the vertices to a NumPy array of the appropriate data type
        vertices = np.array(vertices, dtype='f4')

        # Create a vertex buffer object (VBO) and upload the data to the GPU
        self.vertex_buffer = self.ctx.buffer(vertices)

    def create_index_buffer(self, indices):
        # Convert the indices to a NumPy array of the appropriate data type
        index_data = np.array(indices, dtype='uint32')

        # Create an index buffer object (IBO) and upload the data to the GPU
        self.index_buffer = self.ctx.buffer(index_data)

    def create_vertex_array(self):
        self.vertex_array = self.ctx.vertex_array(self.shader_program, self.vertex_buffer,
                                                  'in_vert', index_buffer=self.index_buffer)

    def run(self):
        self.running = True

        while self.running:
            # Handle pygame events for quit and camera controls
            self.user_inputs.event_handling()

            # Clear the buffer, render the vertices, and set up the view matrix
            self.render()

            self.clock.tick(60)

        # terminate the app
        self.destroy()

    def render(self):
        self.ctx.clear(color=(0.3, 0.5, 0.7))
        self.vertex_array.render(mgl.TRIANGLES)

        pygame.display.flip()

        view_matrix = self.cameras[self.active_camera].create_view_matrix()
        self.shader_program['view_matrix'].write(view_matrix.astype('float32').tobytes())

    def destroy(self):
        # Safely exit the program
        pygame.quit()
        self.vertex_array.release()
        self.vertex_buffer.release()
        self.ctx.release()
