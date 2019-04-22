import numpy as np
import hashlib


def vectorize(profile):
    assert '_id' in profile
    assert 'name' in profile
    assert 'surname' in profile
    profile_summary = '_'.join(profile.values()).encode('utf-8')
    hash_object = hashlib.sha512(profile_summary)
    hex_dig = hash_object.hexdigest()
    return np.asarray([int(i, 16)/64 for i in hex_dig])
