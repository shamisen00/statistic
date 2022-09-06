# %%
from sklearn import datasets
wine = datasets.load_wine(as_frame=True)
# %%
targets = wine.target