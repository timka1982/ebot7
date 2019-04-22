import numpy as np


def vectorize(profile):
    assert '_id' in profile
    assert 'name' in profile
    assert 'surname' in profile
    return np.random.rand(1024)
