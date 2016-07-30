import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
    def plus(self, v):
        n = len(self.coordinates)
        new_coords = []
        for i in range(n):
            new_coords.append(self.coordinates[i] + v.coordinates[i])
        return Vector(new_coords)
    def minus(self, v):
        n = len(self.coordinates)
        new_coords = []
        for i in range(n):
            new_coords.append(self.coordinates[i] - v.coordinates[i])
        return Vector(new_coords)
    def scalar_multiply(self, mult):
        n = len(self.coordinates)
        new_coords = []
        for i in range(n):
            new_coords.append(self.coordinates[i] * mult)
        return Vector(new_coords)
    def magnitude(self):
        # ||x|| = sqrt(x_1^2 + x_2^2... + x_n^2)
        n = len(self.coordinates)
        total = 0
        for i in range(n):
            total += self.coordinates[i] * self.coordinates[i]
        return math.sqrt(total)
    def direction(self):
        mag = self.magnitude()
        n = len(self.coordinates)
        direction = []
        for i in range(n):
            direction.append(self.coordinates[i] / mag)
        return Vector(direction)
    def dot_product(self, v):
        # Multiply (v_1 * self_1) + (v2 * self_2) + ... + (v_3 * self_n)
        n = len(self.coordinates)
        total = 0
        for i in range(n):
            total += self.coordinates[i] * v.coordinates[i]
        return total
    def angle(self, v):
        # Calculate dot_product, then divide by mag(self)*mag(v)
        rads = self.dot_product(v) / (self.magnitude() * v.magnitude())
        return math.acos(rads)
    def compute_parallel(self, b):
        # self_parallel = b_normalization * (self.dotproduct(normalization(b)))
        parallel = b.direction().scalar_multiply(self.dot_product(b.direction()))
        return parallel
    def is_orthogonal_to(self, b, tolerance=1e-10):
        return abs(self.dot(b)) < tolerance
    def compute_orthogonal(self, b):
        parallel = self.compute_parallel(b)
        # self = self_parallel + self_perpendicular
        orthogonal = self.minus(parallel)
        return orthogonal
    def cross_product(self, v):
        #y_1x_1 x1_z_2 z_2y_2 (vertical)
        if 2 <= len(self.coordinates) <= 3:
            cross = []
            x_1 = self.coordinates[0]
            y_1 = self.coordinates[1]
            z_1 = self.coordinates[2]
            x_2 = v.coordinates[0]
            y_2 = v.coordinates[1]
            z_2 = v.coordinates[2]
            cross.append((y_1 * z_2) - (y_2*z_1))
            cross.append(-((x_1*z_2) - (x_2*z_1)))
            cross.append((x_1*y_2) - (x_2*y_1))
            return Vector(cross)
        else:
            return "Cross product for dimensions greater than 3 is not useful"

#my_vec = Vector([1,2,3])
#my_vec2 = Vector([1,2,3,])
#my_vec3 = Vector([3,4])
#my_quiz1 = Vector([-0.221, 7.437])
#my_quiz2 = Vector([5.581, -2.136])
#print my_vec.plus(my_vec2)
#print my_vec.minus(my_vec2)
#print my_vec.scalar_multiply(3)
#print my_quiz1.magnitude()
#print my_quiz2.direction()
#inner_1 = Vector([1,2,3])
#inner_2 = Vector([1,2,3])
# 1*1 + 2*2 + 3*3 = (1 + 4 + 9) = 14
#print inner_1.dot_product(inner_2)
#print my_vec.angle(my_vec2)
#dot_productv_1 = Vector([7.887, 4.138])
#dot_productw_1 = Vector([-8.802, 6.776])
#dot_productv_2 = Vector([-5.955, -4.904, -1.874])
#dot_productw_2 = Vector([-4.496, -8.755, 7.103])
#print dot_productv_1.dot_product(dot_productw_1)
#print dot_productv_2.dot_product(dot_productw_2)
#angle_1_v = Vector([3.183, -7.627])
#angle_1_w = Vector([-2.668, 5.319])
#angle_2_v = Vector([7.35, 0.221, 5.188])
#angle_2_w = Vector([2.751, 8.259, 3.985])
#print angle_1_v.angle(angle_1_w)
#print angle_2_v.angle(angle_2_w)

#parallelv_1 = Vector([-7.579, -7.88])
#parallelw_1 = Vector([22.737, 23.64])

#print parallelv_1.scalar_multiply(3)
#print parallelv_1.dot_product(parallelw_1)

#parallelv_2 = Vector([-2.029, 9.97, 4.172])
#parallelw_2 = Vector([-9.231, -6.639, -7.245])

#print parallelv_2.scalar_multiply(4.5)
#print parallelv_2.dot_product(parallelw_2)

#parallelv_3 = Vector([-2.328, -7.284, -1.214])
#parallelw_3 = Vector([-1.821, 1.072, -2.94])

#print "Q3"
#print parallelv_3.dot_product(parallelw_3)

#print "\nQuiz Coding Vector Projections"
#print "Q1:\n"
#proj_parallel_v = Vector([3.039, 1.879])
#proj_parallel_b = Vector([0.825, 2.036])
#print proj_parallel_v.compute_parallel(proj_parallel_b)
#print "Q2:\n"
#orthogonal_v_1 = Vector([-9.88, -3.264, -8.159])
#orthogonal_b_1 = Vector([-2.155, -9.353, -9.473])
#print orthogonal_v_1.compute_orthogonal(orthogonal_b_1)

#print "Q3:\n"
#parallel_v_2 = Vector([3.009,-6.172, 3.692, -2.51])
#parallel_b_2 = Vector([6.404, -9.144, 2.759, 8.718])
#print parallel_v_2.compute_parallel(parallel_b_2)
#print parallel_v_2.compute_orthogonal(parallel_b_2)

print "Quiz Coding Cross Products"
v = Vector([8.462, 7.893, -8.187])
w = Vector([6.984, -5.975, 4.778])
cross = v.cross_product(w)
print "Cross Product: %s" % (cross)
v = Vector([-8.987, -9.838, 5.031])
w = Vector([-4.268, -1.861, -8.866])
cross = v.cross_product(w)
print "Area of parallelogram = %s" % (cross.magnitude())
v = Vector([1.5, 9.547, 3.691])
w = Vector([-6.007, 0.124, 5.772])
cross = v.cross_product(w)
print "Area of triangle = %s" % (cross.magnitude() / 2)
