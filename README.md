## Python Trie, a simple implementation


### Briefly
Provide an interface to the Trie data structure for the Python language.
Please note: The code is fairly young and was NOT extensively tested.

### Usage
```python
>>> from trie import Trie
>>> foo = Trie()
>>> foo.insert('bahamas')
>>> foo.insert('banana')
>>> foo.has_prefix('ba')
True
>>> foo.has_prefix('bahamas')
True
>>> foo.has_prefix('bai')
False
>>> foo.has_word('banana')
True
>>> foo.has_word('ba')
False
>>> foo.has_word('BANANA')
False
>>> foo.dump()
. b a h a m a s
      n a n a
```
