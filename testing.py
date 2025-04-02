# Requirements
# You are given the initial starting point (x,y) of a rover and the direction (N,S,E,W) it is facing.
# The rover receives a character array of commands.
#
# Implement commands that move the rover forward/backward (f,b).
# Implement commands that turn the rover left/right (l,r).
# Implement wrapping at edges. But be careful, planets are spheres.
# Implement obstacle detection before each move to a new square.
# If a given sequence of commands encounters an obstacle,
# the rover moves up to the last possible point, aborts the sequence and reports the obstacle.

from rover import Rover

def test_rover_position():
    assert Rover([0, 0], "N").position() == [0, 0]

def test_rover_direction():
    assert Rover([0, 0], "N").direction() == "N"

def test_rover_forward():
    assert Rover([0, 0], "N").forward() == [0, 1]

def test_rover_backward():
    assert Rover([0, 0], "N").backward() == [0, -1]


