import numpy as np

class PinholeCamera(object):
    def __init__(self, f, sensor_size):
        sensor_size = np.array(sensor_size)

        # Assume 35mm focal plane
        px_pitch = 35e-3 / sensor_size[0]

        # Focal length in px
        f_px = f / px_pitch

        self.K = np.zeros([3, 4])
        self.K[0, 0] = f_px
        self.K[1, 1] = f_px
        self.K[2, 2] = 1

        # Principle point at center of focal plane
        principle_pt = np.array(sensor_size / 2)

        self.K[0, 2] = principle_pt[0]
        self.K[1, 2] = principle_pt[1]

        print(self.K)

    def project(self, x):
        x = np.matmul(self.K, x)
        x = x / x[2, :]
        return x

class Snow(object):
    def __init__(self, num_snowflakes, camera):
        self.num_snowflakes = num_snowflakes
        self.camera = camera
        self.pos = np.random.rand(3, num_snowflakes) - .5

        self.pos *= np.array([[1], [1], [10]])

        self.pos += np.array([[0], [0], [-5]])

        self.pos = np.vstack((self.pos, np.ones((1, num_snowflakes))))
        self.gravity = 300e-6

    def step(self):
        delta_pos_gravity = self.gravity * np.array([[0], [-1], [0], [0]])
        delta_pos_turbulance = np.random.normal(0, 200e-6, [3, self.num_snowflakes])
        delta_pos_turbulance = np.vstack((delta_pos_turbulance, np.zeros((1, self.num_snowflakes))))
        self.pos += delta_pos_gravity
        self.pos += delta_pos_turbulance

    def project(self):
        return self.camera.project(self.pos)
