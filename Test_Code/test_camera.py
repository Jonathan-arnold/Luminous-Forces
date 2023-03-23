import numpy as np
import pytest
from Camera import Camera

def test_camera_initial_position():
    camera = Camera(position=[0, 0, -5])
    assert np.array_equal(camera.position, [0, 0, -5])

def test_camera_translate():
    camera = Camera(position=[0, 0, -5])
    camera.translate([0, 1, 0])
    assert np.array_equal(camera.position, [0, 1, -5])

# Add more tests for other methods
