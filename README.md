# Intrusion detection system
In this project, we will build a classifier that attempts to pick out malicious intruders in a network. Our constraints are as follows:
1. Our model should be lightweight. We want to pass suspicious events on to more detailed analysis as quickly as possible.
2. Our model should be as sensitive as possible. Presumably, malicious traffic is a small fraction of our overall network traffic, so if we're slightly overzealous with our initial flagging we should still only be considering a small fraction of our overall data. 
    - Nonetheless, if our follow-up analysis is expensive, we want to ensure we're not overly saturating downstream analysis with false positives.