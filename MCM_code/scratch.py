import pandas as pd
import numpy as np

if __name__=="__main__":
	data = pd.read_excel("./data/languages.xlsx")
	regions = data.index.tolist()
	print(regions)
	
		