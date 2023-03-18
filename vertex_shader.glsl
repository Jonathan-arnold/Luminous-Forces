#version 330 core

layout (location = 0) in vec3 in_vert; // Vertex position
layout (location = 1) in vec3 in_color; // Vertex color

uniform mat4 projection_matrix;
uniform mat4 view_matrix;

out vec3 vertex_color; // Color to be passed to the fragment shader

void main() {
    vertex_color = in_color;
    gl_Position = projection_matrix * view_matrix * vec4(in_vert, 1.0);
}