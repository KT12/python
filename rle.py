# Detecting consecutive values in data (ie run length encoding)
# https://stackoverflow.com/a/37252/6832816

import numpy as np
import pandas as pd
from itertools import groupby
from collections import Counter

vals = [True, False]

runs = pd.Series(random.choices(vals, k=100))

runs_list = [(c, len(list(cgen))) for c, cgen in groupby(runs)]
