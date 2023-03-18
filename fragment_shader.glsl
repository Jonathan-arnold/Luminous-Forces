#version 330 core

in vec3 vertex_color; // Color received from the vertex shader

out vec4 frag_color; // Output color

void main() {
    frag_color = vec4(vertex_color, 1.0);
}
