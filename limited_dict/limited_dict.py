from collections import MutableMapping
from bisect import bisect


class LimitedDict(MutableMapping):
    def __init__(self, max_length, cache_mapping=True):
        self._keys = list()
        self._values = list()
        self._internal_mapping = dict() if cache_mapping else None
        self._max_length = max_length
        self._at_max_length = False

    def __setitem__(self, key, value):
        try:
            index = self._keys.index(key)
            exists = True
        except:
            index = bisect(self._values, value)
            exists = False

        if exists:
            self._values[index] = value
        else:
            self._values.insert(index, value)
            self._keys.insert(index, key)

        if self._internal_mapping is not None:
            self._internal_mapping[key] = value

        if self._at_max_length:
            if self._internal_mapping is not None:
                del self._internal_mapping[self._keys[self._max_length]]
            del self._keys[self._max_length]
            del self._values[self._max_length]
        else:
            if len(self._keys) == self._max_length:
                self._at_max_length = True

    def __getitem__(self, key):
        if self._internal_mapping is not None:
            return self._internal_mapping[key]
        else:
            index = self._keys.index(key)
            return self._values[index]

    def __delitem__(self, key):
        index = bisect(self._keys, key) - 1
        del self._keys[index]
        del self._values[index]
        del self._internal_mapping[key]
        self._at_max_length = False

    def __iter__(self):
        return self._keys.__iter__()

    def __len__(self):
        return len(self._keys)

    def __repr__(self):
        return zip(self._keys, self._values).__str__()
