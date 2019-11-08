##
## EPITECH PROJECT, 2019
## 101pong
## File description:
## Manipulate vectors
##

import sys
sys.path.insert(1, "../")
from classes import Vector

def get_velocity_vector(vector_1: Vector, vector_2: Vector):
    velocity_vector = Vector.Vector(0, 0, 0)
    velocity_vector.x = vector_2.x - vector_1.x
    velocity_vector.y = vector_2.y - vector_1.y
    velocity_vector.z = vector_2.z - vector_1.z
    return (velocity_vector)

def get_ball_coordinates(vector_1: Vector, vel_vector: Vector, t: int):
    ball_coordinates = Vector.Vector(0, 0, 0)
    ball_coordinates.x = vel_vector.x * (t + 1) + vector_1.x
    ball_coordinates.y = vel_vector.y * (t + 1) + vector_1.y
    ball_coordinates.z = vel_vector.z * (t + 1) + vector_1.z
    return (ball_coordinates)