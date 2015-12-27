from key import Key
from message import Message
import numpy as np

original = np.array([1,2,0])
mapping = np.array([0,2,1])

key = Key(original)
new_key = key.substitute(mapping)
inverted_key = key.invert()

assert np.all(new_key == np.array([2,1,0]))
assert np.all(inverted_key == np.array([2,0,1]))

alpha = 'abcdefghijklmnopqrstuvwxyz'
beta = 'qwertyuiopasdfghjklzxcvbnm'
key = np.array(range(26))
key[0] = 25
key[25] = 0

message = Message(alpha)
assert message.map(key) == 'zbcdefghijklmnopqrstuvwxya'
assert np.all(message.frequencies() == [1.0/26 for x in range(26)])
