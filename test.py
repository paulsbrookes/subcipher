from key import Key
from message import Message
from key import Key
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


with open('sample.txt','r') as source:
    text = source.read()
my_message = Message(text)
my_message = my_message.filter()

encipher_key = Key()
encipher_key.random_key()

enciphered_message = my_message.map(encipher_key)
enciphered_message.text
decipher_key = encipher_key.invert()
deciphered_message = enciphered_message.map(decipher_key)

assert deciphered_message.text == my_message.text
