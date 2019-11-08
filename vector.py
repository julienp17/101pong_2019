# -*-coding:Utf-8 -*
##
## EPITECH PROJECT, 2019
## 101pong
## File description:
## Class Vector
##

class Vector:

    """This class represents a vector.

    It holds its x, y, and z value."""

    def __init__(self, x:float, y:float, z:float):
        self.x = x
        self.y = y
        self.z = z

def get_velocity_vector(vector_1: Vector, vector_2: Vector):
    velocity_vector = Vector(0, 0, 0)
    velocity_vector.x = vector_2.x - vector_1.x
    velocity_vector.y = vector_2.y - vector_1.y
    velocity_vector.z = vector_2.z - vector_1.z
    return (velocity_vector)