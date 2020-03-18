# Intrusion detection using online machine learning
An Intrusion Detection Systems (IDS) is a system that monitors networks for malicious activity.
## Introduction

We will utilize a variety of approaches in this project. We will conduct analysis on the `KDD99` dataset, which is a large, labelled dataset consisting packet metadata from about 5 million packets. Of these, about 3 million (60%) are malicious, and the rest are background. We show that building a good classifier on this dataset is remarkably trivial ― both logistic regression and isolation forests perform extremely well. We also build an incrementally-trained logistic regression on the shuffled dataset, and show that this achieves excellent performance.

Having shown the tractability of using the entirety of `KDD99`, we then hone in on a more realistic scenario, where the data is simply an unlabeled stream of majority background traffic. A subset of the `KDD99` dataset, known as `HTTP (KDD99)`, simulates this environment with an extreme class imbalance (0.35% in the positive class). We attempt to replicate the results found in this [paper](https://www.ijcai.org/Proceedings/11/Papers/254.pdf). Using two different libraries (`creme` and `skmultiflow`), we demonstrate that the original paper's reported results for `HTTP` are too good; the authors incorrectly preprocessed their data. 

Our incremental learning was done using the python library `creme`. Between the beginning and end of this project (around notebook 07), creme updated to a new minor version (`0.4.4 -> 0.5`).
## Contents

## Further work:
