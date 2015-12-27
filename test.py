from key import Key
import numpy as np

original = np.array([1,2,0])
mapping = np.array([0,2,1])

key = Key(original)
new_key = key.substitute(mapping)
inverted_key = key.invert()

assert np.all(new_key == np.array([2,1,0]))
assert np.all(inverted_key == np.array([2,0,1]))
