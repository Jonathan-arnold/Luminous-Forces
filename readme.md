# Project Title

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
   1. [Function/Class 1](#functionclass-1)
   2. [Function/Class 2](#functionclass-2)
   3. [Function/Class N](#functionclass-n)
3. [Usage Instructions](#usage-instructions)
4. [Contributing Guidelines](#contributing-guidelines)
5. [Version History](#version-history)


## Goals

This section will describe the main goals of the project and provide a conceptual
understanding of the approach used to achieve those goals.


### Overall Project Goal

Luminous Forces is a 3D particle simulator that aims to provide an immersive and visually stunning experience while accurately simulating electric forces between charged particles. Drawing inspiration from Coulomb's Law, the project focuses on the interaction of protons, electrons, and neutrons within a confined space. By incorporating high-quality aesthetics, such as smooth, glowing spheres with distinct warm and cool color palettes for protons and electrons, Luminous Forces aims to create a captivating visual representation of the underlying physics.

The project is designed to offer a balance between real-time simulation and precision, with adjustable simulation speeds and a scalable number of particles. As the project evolves, Luminous Forces will incorporate additional features such as a user-friendly GUI, customizable simulation parameters, and an intuitive camera control system to enhance the overall user experience.

Luminous Forces strives to combine the beauty of the visual arts with the accuracy of scientific simulation, creating an engaging and educational tool for exploring the fascinating world of particle physics.


### v0.1 Goal

Create a basic 3D environment with a simple camera system, window management, and user input handling. This version should set up the foundation for future development, including rendering particles and simulating their interactions.

#### Natural Language Explanation

1. Implement window management using Pygame.
2. Set up a basic rendering pipeline using ModernGL.
3. Develop a simple camera system that allows for rotation and zoom based on user input.
4. Add user input handling for camera control and basic application functions, such as closing the window.

#### Pseudocode

1. Initialize Pygame and create a window.

    1.1. Import Pygame library.

    1.2. Initialize Pygame using pygame.init().

    1.3. Set the window size and title.

    1.4. Create a window using pygame.display.set_mode().

2. Set up a basic rendering pipeline using ModernGL.

    2.1. Import ModernGL library.
    
        ModernGL is a Python wrapper for OpenGL that simplifies shader and buffer management. Importing the library allows us to access its functionality.
    
    2.2. Create a standalone ModernGL context.
    
        A context represents the state of the OpenGL rendering pipeline. Creating a context allows us to configure and use the OpenGL pipeline through ModernGL.

    2.3. Load vertex and fragment shaders from files.

        Shaders are small programs that run on the GPU and determine how the geometry and appearance of 3D objects are rendered. Loading vertex and fragment shaders will allow us to customize the rendering process.

    2.4. Compile shaders and create a shader program.

        Compiling the shaders and creating a shader program link the shaders together, allowing them to work in tandem during the rendering process.

    2.5. Define vertex and index buffers for rendering geometry.
    
        Vertex buffers store the position and other attributes of vertices, while index buffers define how the vertices are connected to form triangles. These buffers are used by the GPU to render 3D geometry.

    2.6. Set up a projection matrix and pass it to the shaders.

        A projection matrix defines how 3D coordinates are transformed into 2D screen coordinates. Passing this matrix to the shaders allows the rendered scene to be displayed correctly on the screen.

3. Develop a simple camera system that allows for rotation and zoom based on user input.

   3.1. Create a Camera class with position, rotation, and zoom attributes.
   
   3.2. Implement methods to update the camera's position, rotation, and zoom based on user input.
   
   3.3. Create a view matrix that represents the camera's transformation.
   
   3.4. Pass the view matrix to the shaders for rendering the scene from the camera's perspective.

4. Implement user input handling for controlling the camera and basic application functions.

   4.1. Define key bindings for camera control and other application functions.
   
   4.2. In the main loop, use pygame.event.get() to retrieve user events.
   
   4.3. Process keyboard and mouse input to control the camera's rotation and zoom.
   
   4.4. Handle the window close event to properly terminate the application.

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


### Function/Class 1

- Goal
- Natural language explanation
- Pseudocode
- Reference to the actual code


### Function/Class 2

- Goal
- Natural language explanation
- Pseudocode
- Reference to the actual code

... (continue with other functions and classes)


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

