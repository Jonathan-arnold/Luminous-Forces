import pytest
from helper_functions import load_shader
import os

def test_load_shader_valid_file():
    shader_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'vertex_shader.glsl'))
    shader_content = load_shader(shader_file_path) # '../vertex_shader.glsl'
    assert shader_content is not None
    assert isinstance(shader_content, str)


def test_load_shader_invalid_file():
    with pytest.raises(FileNotFoundError):
        load_shader('nonexistent_file.glsl')
