from src.pycounts_ubc import pycounts_ubc
#from src.pycounts_ubc import *
from src.pycounts_ubc import plotting

counts = pycounts_ubc.count_words("zen.txt")
fig = plotting.plot_words(counts, 10)
print(counts)
