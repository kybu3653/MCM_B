import numpy as np
import pandas as pd

def benefit_country(data):
	pass

if __name__=="__main__":
	data = pd.read_csv("./data/data.csv",index_col=0)
	
	countries = np.unique(data["Country"])
	
	for country in countries:
		subset = data[data["Country"]==country]
		print(np.unique(subset["Year"]))