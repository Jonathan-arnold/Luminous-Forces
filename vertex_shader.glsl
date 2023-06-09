#version 330 core

layout (location = 0) in vec3 in_vert;

uniform mat4 projection_matrix;
uniform mat4 view_matrix;

void main() {
    gl_Position = projection_matrix * view_matrix * vec4(in_vert, 1.0);
}