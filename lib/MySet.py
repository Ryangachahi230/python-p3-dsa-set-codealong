class MySet:
    def __init__(self, enumerable=[]):
        # Use dictionary keys to ensure uniqueness
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        # Check membership in O(1) time
        return value in self.dictionary

    def add(self, value):
        # Add value as key
        self.dictionary[value] = True
        return self

    def delete(self, value):
        # Remove if exists
        self.dictionary.pop(value, None)
        return self

    def size(self):
        # Return number of elements
        return len(self.dictionary)

    def clear(self):
        # Remove all elements
        self.dictionary.clear()
        return self

    def __str__(self):
        # Nicely format set elements
        set_list = [str(key) for key in self.dictionary.keys()]
        return f"MySet: {{{', '.join(set_list)}}}"
