import unittest

from cupy import testing


@testing.gpu
class TestSpecial(unittest.TestCase):

    @testing.for_dtypes(['e', 'f', 'd'])
    @testing.numpy_cupy_allclose(rtol=1e-3)
    def test_i0(self, xp, dtype):
        a = testing.shaped_random((2, 3), xp, dtype)
        return xp.i0(a)

    @testing.for_dtypes(['e', 'f', 'd'])
    @testing.numpy_cupy_allclose(atol=1e-3)
    def test_sinc(self, xp, dtype):
        a = testing.shaped_random((2, 3), xp, dtype)
        return xp.sinc(a)
