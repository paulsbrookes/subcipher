from ciphertext import Ciphertext
import time

c = Ciphertext()
c.text_in('hello')
assert c.text_out() == 'hello'

d = Ciphertext()
d.text_in('No King of the Isles had ever needed a Hand')
with open('sample.txt','r') as source:
    natural_text = source.read()

natural = Ciphertext()
natural.text_in(natural_text)
natural.pair_frequencies()
natural.triplet_frequencies()
natural.quadruplet_frequencies()
