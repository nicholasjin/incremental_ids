#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from skmultiflow.data import DataStream
from skmultiflow.anomaly_detection import HalfSpaceTrees
from skmultiflow.evaluation import EvaluatePrequential

import h5py


# Read in the http data
arrays = {}
f = h5py.File("http.mat")
for k,v in f.items():
    arrays[k] = np.array(v)


X = pd.DataFrame(arrays["X"]).T
y = pd.DataFrame(arrays["y"]).astype(int).T


stream = DataStream(data=X, y=y)
stream.prepare_for_use()

hst = HalfSpaceTrees(n_features=3)
evaluator = EvaluatePrequential(show_plot = False,
                                pretrain_size=250,
                                max_samples=1_000_000)

evaluator.evaluate(stream=stream, model=hst)
