import math
from math import pi
from math import sqrt
import geo_lib


class TestCircle():

    def test_circle_2(self):
        assert geo_lib.Figure(2).circle() == (4 * pi, 4 * pi)


class TestSquare():

    def test_square_2(self):
        assert geo_lib.Figure(2).square() == (8, 4)


class TestRectangle():

    def test_rectangle_2_3(self):
        assert geo_lib.Figure(2, 3).rectangle() == (10, 6)


class TestTriangle():

    def test_trianglee_2_3_4_Perimeter(self):
        # Figure принимает последний аргумент как операцию
        # к вычислениям, где 1 - это периметр, а 2 - площадь: 
        assert geo_lib.Figure(2, 3, 4, 1).triangle() == 9

    def test_trianglee_2_3_Area(self):
        assert geo_lib.Figure(2, 3, 2).triangle() == 3


class TestBall():

    def test_ball_4(self):
        assert geo_lib.Figure(4).ball() == (64 * pi, (256 / 3) * pi)


class TestSphere():

    def test_sphere_4(self):
        assert geo_lib.Figure(4).sphere() == 64 * pi


class TestCube():

    def test_cube_5(self):
        assert geo_lib.Figure(5).cube() == (150, 125)


class TestCuboid():

    def test_cuboid_4_5_6(self):
        assert geo_lib.Figure(4, 5, 6).cuboid() == (148, 120)


class TestTriangularPyramid():

    def test_triangular_pyramid_9_3(self):
        assert geo_lib.Figure(9, 3).triangular_pyramid() == (2.25 * (9 * sqrt(3) + 18), 243 / (4 * sqrt(3)))


class TestQuadrangularPyramid():

    def test_quadrangular_pyramid_3_6(self):
        assert geo_lib.Figure(3, 6).quadrangular_pyramid() == (45, 18)

