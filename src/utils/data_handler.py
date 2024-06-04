#!/usr/bin/env python3

import numpy as np
import pandas as pd

class DataHandler:
    def __init__(self, source=None):
        self.source = source

    def from_numpy(self, X, y):
        self.X = X
        self.y = y

    # def from_csv(self, file_path):
    #     data = pd.read_csv(file_path)
    #     self.X = data.iloc[:, :-1].values
    #     self.y = data.iloc[:, -1].values

    def from_xlsx(self, file_path):
        data = pd.read_excel(file_path)
        self.X = data.iloc[:, :-1].values
        self.y = data.iloc[:, -1].values

    def get_features(self):
        return self.X

    def get_labels(self):
        return self.y
