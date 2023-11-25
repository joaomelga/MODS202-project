import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('wage1.raw', delim_whitespace=True, header=None)

wage = df[0]
plt.hist(wage, 'auto')

