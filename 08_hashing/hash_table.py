"""A tiny hash table with chaining, to demystify Python's dict."""


class HashTable:
    def __init__(self, capacity=8):
        self._buckets = [[] for _ in range(capacity)]
        self._size = 0

    def _bucket(self, key):
        return self._buckets[hash(key) % len(self._buckets)]

    def put(self, key, value):
        bucket = self._bucket(key)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self._size += 1
        if self._size / len(self._buckets) > 0.7:
            self._resize(len(self._buckets) * 2)

    def get(self, key, default=None):
        for k, v in self._bucket(key):
            if k == key:
                return v
        return default

    def remove(self, key):
        bucket = self._bucket(key)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._size -= 1
                return True
        return False

    def _resize(self, new_cap):
        old = self._buckets
        self._buckets = [[] for _ in range(new_cap)]
        self._size = 0
        for bucket in old:
            for k, v in bucket:
                self.put(k, v)

    def __len__(self):
        return self._size

    def __contains__(self, key):
        return any(k == key for k, _ in self._bucket(key))

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        for k, v in self._bucket(key):
            if k == key:
                return v
        raise KeyError(key)


if __name__ == "__main__":
    h = HashTable()
    for i, k in enumerate("abcdefghij"):
        h.put(k, i)
    print("len:", len(h))
    print("get c:", h.get("c"))
    h.remove("c")
    print("get c after remove:", h.get("c"))
