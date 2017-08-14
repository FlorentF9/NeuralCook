"""
@file data_utils.py
@author FlorentF9

Neural Cook

Dataset class
"""

from collections import Counter
import numpy as np


class Dataset:
    def __init__(self, file):
        # Load file
        with open(file, 'r') as f:
            self.raw_data = f.read()
        # Get symbol dictionary
        count = Counter(self.raw_data).most_common()
        self.dictionary = dict()
        for symbol, _ in count:
            self.dictionary[symbol] = len(self.dictionary)
        self.reverse_dictionary = dict(zip(self.dictionary.values(),
                                           self.dictionary.keys()))
        self.n_symbols = len(self.dictionary)
        # Convert to symbols
        self.data = [self.dictionary[symbol] for symbol in self.raw_data]

    def batch(self, batch_size, n_steps):
        if batch_size*n_steps + 1 > len(self.data):
            print('Not enough data in training set. Try reducing batch_size or n_steps.')
            return
        offset = 0
        while True:
            # Output should have shape (batch_size, n_steps, n_symbols)
            x = np.zeros((batch_size, n_steps, self.n_symbols))
            y = np.zeros((batch_size, self.n_symbols))

            if offset + batch_size*n_steps + 1 > len(self.data):
                offset = 0

            for i in range(batch_size):
                for j in range(n_steps):
                    x[i, j, self.data[offset+i*n_steps+j]] = 1.0
                y[i, self.data[offset+(i+1)*n_steps]] = 1.0

            offset += 1

            yield x, y
