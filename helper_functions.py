# takes the file path of a shader, reads its content, and returns it as a string
def load_shader(shader_file):
    with open(shader_file, "r") as file:
        return file.read()