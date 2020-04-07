# Intrusion detection using online machine learning
# Introduction
Grand View Research estimated the network security management market to be valued at ~4 billion USD in 2018, with projected annual growth of 14.5%. It is an enormous market with enormous growth due to the growing ubiquity of cyberattacks worldwide.

An **Intrusion Detection System** (IDS) is a system that monitors networks for malicious activity. In this project, we utilize a variety of approaches to construct an IDS from scratch.

# Classifying KDD99
Our analysis will be focused on the `KDD99` dataset, a large, labelled dataset consisting of packet metadata from about 5 million packets. Of these, about 3 million (60%) are malicious, and the rest are background. We show that building a good classifier on this dataset is remarkably trivial ― both logistic regression and isolation forests perform extremely well. We also build an incrementally-trained logistic regression on the shuffled dataset, and show that this achieves excellent performance.

# Benchmarking Half-Space Trees
Having shown the tractability of using the entirety of `KDD99`, we then hone in on a more realistic scenario, where the data is simply an unlabeled stream of majority background traffic. A subset of the `KDD99` dataset, known as `HTTP (KDD99)`, simulates this environment with an extreme class imbalance (0.35% in the positive class). We attempt to replicate the results found in this [paper](https://www.ijcai.org/Proceedings/11/Papers/254.pdf). Using two different libraries (`creme` and `skmultiflow`), we demonstrate that the original paper's reported results for `HTTP` are too good; the authors incorrectly preprocessed their data.
