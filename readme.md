# Luminous Forces

## Overview

This README file serves as a comprehensive guide to understanding the project.
The goal of the project is to [describe the main goal or purpose of the project].
The following sections will provide detailed information on how the project is
structured and how it can be understood by anyone not familiar with the project.

The documentation is organized in a hierarchical manner, starting with a high-level
explanation of the project's goals, followed by a conceptual explanation of how to
achieve those goals. It then gets into the details of how the goal can be accomplished
in pseudocode. Finally, references are provided for functions and classes from the code
that implement the pseudocode.

This format is recursive. For any complex functions or classes the above format will
be applied to them individually below the high-level concepts in a tree hierarchy.


## Table of Contents

1. [Goals](#goals)
   1. [Overall Project Goal](#overall-project-goal)
   2. [v0.1 Goal](#v01-goal)
2. [Function and Class Descriptions](#function-and-class-descriptions)
   1. [App.setup_program](#appsetupprogram)
   2. [Camera](#camera)
   3. [User_Inputs](#userinputs)
3. [Usage Instructions](#usage-instructions)
4. [Contributing Guidelines](#contributing-guidelines)
5. [Version History](#version-history)
   1. [v0.1](#v01---basic-3d-environment-and-camera-system--release-date--2023-03-21-)


## Goals

This section will describe the main goals of the project and provide a conceptual
understanding of the approach used to achieve those goals.


### Overall Project Goal

Luminous Forces is a 3D particle simulator that aims to provide an immersive and visually stunning experience while accurately simulating electric forces between charged particles. Drawing inspiration from Coulomb's Law, the project focuses on the interaction of protons, electrons, and neutrons within a confined space. By incorporating high-quality aesthetics, such as smooth, glowing spheres with distinct warm and cool color palettes for protons and electrons, Luminous Forces aims to create a captivating visual representation of the underlying physics.

The project is designed to offer a balance between real-time simulation and precision, with adjustable simulation speeds and a scalable number of particles. As the project evolves, Luminous Forces will incorporate additional features such as a user-friendly GUI, customizable simulation parameters, and an intuitive camera control system to enhance the overall user experience.

Luminous Forces strives to combine the beauty of the visual arts with the accuracy of scientific simulation, creating an engaging and educational tool for exploring the fascinating world of particle physics.

#### Natural Language Explanation

Luminous Forces will be developed using Python, taking advantage of several libraries and frameworks to create a visually stunning 3D particle simulator that accurately simulates electric forces between charged particles.

1. Pygame will be used to manage the main window, user input, and event handling. This library provides a simple interface to build interactive applications and games, making it an ideal choice for managing the display and user interactions.

2. ModernGL, a Python wrapper for OpenGL, will be employed to handle the 3D rendering pipeline. This library simplifies shader and buffer management, allowing for efficient rendering of the particles, including the smooth, glowing spheres with distinct warm and cool color palettes for protons and electrons.

3. NumPy, a powerful numerical computing library for Python, will be used to perform vector and matrix calculations. This library will assist in the simulation of the particle physics, including the implementation of Coulomb's Law and the interactions between protons, electrons, and neutrons.

4. To create an intuitive camera control system, a custom Camera class will be developed that allows users to navigate the 3D environment, zoom in and out, and rotate around the scene. This will enhance the user experience, providing a more immersive and engaging view of the particle interactions.

5. As the project evolves, a user-friendly GUI will be implemented using a library such as PyQT or tkinter. This will allow users to customize simulation parameters, adjust simulation speeds, and control the number of particles in the scene.

6. Performance optimizations and fine-tuning will be performed to ensure a balance between real-time simulation and precision, providing a smooth and visually appealing experience.

By combining these libraries and techniques, Luminous Forces will achieve its goal of creating an engaging and educational tool that merges the beauty of the visual arts with the accuracy of scientific simulation, enabling users to explore the fascinating world of particle physics.

### v0.2 Goal

The primary goals of v0.2 are to enhance the visual appearance and realism of the 3D engine. We will add lighting, rendering spheres, rendering multiple objects, coloring objects, introducing the physics engine with initial support for two objects, rendering reflective objects, rendering glowing objects, implementing skyboxes, and adding shadows.

#### Natural Language Explanation

1. Implement a basic lighting system to enhance the appearance of objects in the scene. Introduce different types of light sources (e.g., point lights, directional lights, and spotlights) and basic shading models (e.g., Phong or Lambertian shading).
2. Add support for rendering spheres as a new primitive shape. Generate sphere geometry and use vertex and index buffers to render the sphere.
3. Enable rendering of multiple objects in the scene. Maintain a list of objects in the scene and render them in the main loop.
4. Add support for coloring objects with different materials or textures. Implement materials with properties (diffuse color, specular color, shininess, etc.) and texture mapping.
5. Integrate a physics engine with initial support for two objects in the scene. Implement basic physics simulations with collision detection, gravity, and object interactions.
6. Add support for rendering reflective and glowing objects in the scene. Implement environment mapping for reflections and emissive materials for glowing objects.
7. Implement skyboxes to create an immersive background environment in the scene. Use a cube with a textured interior to create the illusion of a distant environment.
8. Add realistic shadows to the scene to improve visual depth and realism. Implement shadow mapping techniques such as shadow maps or cascaded shadow maps.

#### Pseudocode
1. Lighting
- Define light sources and their properties (position, color, intensity, etc.)
- Implement shading models (Phong or Lambertian shading)
- Calculate lighting contributions based on shading models and light sources
- Apply the lighting contributions to the objects in the scene
2. Spheres
- Define a sphere class with properties (radius, position, etc.)
- Generate sphere geometry (vertices and indices)
- Create vertex and index buffers for the sphere
- Render the sphere using the created buffers
3. Multiple Objects
- Create a list to store scene objects
- For each object in the scene, generate geometry and create vertex/index buffers
- In the main loop, render each object in the scene using its buffers
4. Material Properties
- Define a material class with properties (diffuse color, specular color, shininess, etc.)
- Assign a material to each object in the scene
- Implement texture mapping to apply images or patterns to object surfaces
- In the shading process, use the material properties and textures to determine the final object color
5. Physics Engine
- Integrate a physics engine (e.g., PyBullet, ODE, or a custom solution)
- Define rigid bodies for scene objects
- Set up the physics simulation (gravity, collision shapes, etc.)
- In the main loop, update the physics simulation and apply the results to the objects
6. Reflections and Glow
- Implement environment mapping (e.g., cube mapping) for reflective objects
- Define emissive materials for glowing objects
- In the shading process, use environment mapping and emissive materials to determine the final object appearance
7. Skyboxes
- Create a cube with inverted normals to act as a skybox
- Apply a panoramic texture to the inside faces of the cube
- Render the skybox behind all other objects in the scene
8. Shadows
- Choose a shadow mapping technique (e.g., shadow maps, cascaded shadow maps)
- Render the scene from the light's point of view, storing depth information in a shadow map
- In the main scene rendering, use the shadow map to determine if a pixel is in shadow
- Apply shadows to the objects in the scene based on the shadow map data

#### References to the functions or classes that implement this goal



## Function and Class Descriptions

This section provides an intuitive understanding of the functions
and classes used in the project. For each function or class, there
will be a subsection that includes the following:

- The goal of the function or class
- A natural language explanation of how the function or class works
- Pseudocode outlining the logic and flow of the function or class
- References to any functions or classes from the actual code that
    help implement the function or class


### App

#### Goal

The App class is responsible for initializing and running the 3D application, setting up the window, OpenGL context, shaders, and camera, as well as managing the main loop for rendering and user input processing.

#### Natural language explanation

The App class initializes the Pygame library, sets up a window for rendering, creates a ModernGL context, loads and compiles shaders, sets up buffers and vertex arrays, and initializes a Camera object. It then runs the main loop, which includes rendering the scene, handling user inputs, and updating the camera's view matrix.

#### Reference to the actual code

- __init__ method in the App class
- setup_window method in the App class
- setup_program method in the App class
- run method in the App class
- destroy method in the App class
- Camera class


### Camera

#### Goal

The Camera class provides a 3D camera for a physics simulator, allowing the user to control its position, rotation, and zoom using the keyboard and mouse.

#### Natural language explanation

The Camera class creates a camera object that can be positioned, rotated, and zoomed in a 3D environment. The class provides methods for keyboard and mouse controls, as well as functions to create view and rotation matrices. The camera can translate (move) along its axes, orbit around a specified point (fulcrum), and zoom in or out. It also maintains information about its position, rotation, and orientation (facing, up, and right vectors).

#### Pseudocode

1. Initialize the camera with position, rotation, and zoom values
2. Define methods for camera control:
   1. Keyboard controls for translation
   2. Mouse controls for orbiting around the fulcrum
   3. Mouse controls for zooming
3. Define methods for orbiting around the fulcrum and updating the camera's orientation vectors
4. Define methods for translating the camera
5. Create view and rotation matrices based on the camera's position and orientation

#### Reference to the actual code

1. Initialization: __init__(self, position=[0, 0, -5], rotation=[0, 0, math.pi], zoom=1)
2. Camera control methods:
   1. Keyboard controls: camera_control(self)
   2. Orbit control (mouse motion): orbit_control(self, event)
   3. Zoom control (mouse wheel): zoom_control(self, event)
3. Orbiting and updating orientation vectors: orbit_around_fulcrum(self, delta_x, delta_y, sensitivity=0.005)
4. Camera translation: translate(self, translation_vector)
5. Create view and rotation matrices:
   1. View matrix: create_view_matrix(self)
   2. Rotation matrix: create_rotation_matrix(self)


### User_Inputs

#### Goal

The User_Inputs class aims to handle user input events, such as keyboard and mouse inputs, to control the camera's position, rotation, and zoom levels in the 3D scene.

#### Natural language explanation

The User_Inputs class receives an instance of the App class as an argument during initialization. It then processes user inputs, such as keyboard keys and mouse movements, to translate, rotate, and zoom the camera in the 3D scene.

#### References to actual code

- event_handling method in the User_Inputs class
- orbit_control method in the User_Inputs class
- translate_control method in the User_Inputs class
- zoom_control method in the Camera class
- orbit_around_fulcrum method in the Camera class
- translate method in the Camera class


## Usage Instructions

This section will provide instructions on how to set up, install,
and run the project.


## Contributing Guidelines

We welcome contributions from the community to help improve and
extend the project. The following guidelines will help ensure a
smooth development process and maintain the quality of the code
and documentation.

1. Overall Goal: Keep the overall goal of the entire project in mind
when working on a specific version. This will provide context for
the version-specific goals and ensure that the project stays
focused on the end target.

2. Version-Specific Goals: When working on a specific version, focus
on the goals outlined for that version. These goals should be
clear, concise, and focused, guiding your development efforts.

3. Version History: Update the version history section in the
documentation with key changes, features, and improvements for
each version. This will help track progress and understand how the
project has evolved over time.

4. Branching Strategy: Create separate branches for each version in
your version control system (e.g., Git). Work on different features
or improvements in these branches without affecting the main
codebase. Once a version's goals are met and the code is stable,
merge it back into the main branch.

5. Code Structure: Organize your code into modules and classes based
on functionality. This will make it easier to maintain and understand
the code, as well as make it simpler to update or extend in future versions.

6. Documentation Updates: Update the documentation as you develop each
version, ensuring that it stays in sync with the code. Update both
the high-level goals and the detailed explanations for functions
and classes as needed.

7. Code Reviews: Conduct code reviews at the end of each version to
ensure the quality and consistency of the code. This will help identify
potential issues or areas for improvement before moving on to the next
version.
   1. Understand the purpose, requirements, and documentation: Familiarize yourself with the goals, requirements, and documentation of the code. This will help you understand the context in which the code was written and its intended functionality.

   2. Review code structure, readability, and maintainability: Examine the overall organization and modularity of the code, checking for readability, meaningful naming conventions, and adherence to best practices. Look for code smells, anti-patterns, and opportunities to improve maintainability.

   3. Test the code and assess performance: Ensure the code is thoroughly tested, both manually and with automated tests. Identify potential performance bottlenecks and opportunities for optimization.

   4. Evaluate extensibility, scalability, and provide feedback: Consider the ease of extending or modifying the code in the future and its ability to scale. Summarize your findings, provide constructive feedback, and discuss alternative approaches or solutions as needed.

Please follow these guidelines when contributing to the project. By
adhering to these principles, we can work together to develop and
document the project in a clear and organized way, making it easier
to manage, understand, and extend in the future.


## Version History
This section provides an overview of the major changes, features,
and improvements for each version of the project. It helps track the
progress of the project and understand how it has evolved over time.

For each version, include the following information:

*Version number (e.g., v0.1, v0.2, etc.)
*Release date
*A brief description of the main changes, features, or improvements in
the version
*Any known issues or limitations

Example Entry:
v0.1 - Initial Implementation (Release Date: YYYY-MM-DD)
Implemented basic window management using Pygame.
Added user input handling for camera rotation and zoom.
Set up a basic rendering pipeline using ModernGL.
Known issues/limitations:

Limited to rendering a single static object.
Camera movement not yet implemented.

-------------------------------------------------------------------

Entries:

### v0.1 - Basic 3D Environment and Camera System (Release Date: 2023-03-21)

Created a basic 3D environment with window management using Pygame.

- Set up a fundamental rendering pipeline with ModernGL, including vertex and fragment shaders, vertex and index buffers, and a projection matrix.

- Developed a simple camera system that allows for rotation and zoom based on user input, along with methods to update the camera's position, rotation, and zoom.

- Implemented user input handling for camera control and basic application functions, such as closing the window.

Known issues/limitations:

- Limited to rendering a single static object.
- Advanced camera movement and controls not yet implemented.
- Particle rendering and simulation features not yet added.