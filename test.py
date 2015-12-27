from key import Key
from message import Message
import numpy as np

map0 = np.array([1,2,0])
map1 = np.array([0,2,1])

key0 = Key(map0)
key1 = Key(map1)

key3 = key0.substitute(key1.map)
inverted_key0 = key0.invert()

assert np.all(key3.map == np.array([2,1,0]))
assert np.all(inverted_key0.map == np.array([2,0,1]))

alpha = 'abcdefghijklmnopqrstuvwxyz'
beta = 'qwertyuiopasdfghjklzxcvbnm'
key = np.array(range(26))
key[0] = 25
key[25] = 0
key = Key(key)
predicted_frequencies = [1.0/26 for x in range(26)]
predicted_frequencies.append(0)

message = Message(alpha)
assert message.map(key).text == 'zbcdefghijklmnopqrstuvwxya'
assert np.all(message.frequencies() == predicted_frequencies)
