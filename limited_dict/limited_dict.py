from collections import MutableMapping
from bisect import bisect


class LimitedDict(MutableMapping):
    def __init__(self, max_length):
        self._keys = list()
        self._values = list()
        self._internal_mapping = dict()
        self._max_length = max_length
        self._at_max_length = False

    def __setitem__(self, key, value):
        index = bisect(self._values, value)
        self._values.insert(index, value)
        self._keys.insert(index, key)
        self._internal_mapping[key] = value

        if self._at_max_length:
            del self._internal_mapping[self._keys[self._max_length]]
            del self._keys[self._max_length]
            del self._values[self._max_length]
        else:
            if len(self._keys) == self._max_length:
                self._at_max_length = True

    def __getitem__(self, key):
        return self._internal_mapping[key]

    def __delitem__(self, key):
        index = bisect(self._keys, key) - 1
        del self._keys[index]
        del self._values[index]
        del self._internal_mapping[key]
        self._at_max_length = False

    def __iter__(self):
        return self._internal_mapping.__iter__()

    def __len__(self):
        return len(self._keys)

    def __repr__(self):
        return zip(self._keys, self._values).__str__()
