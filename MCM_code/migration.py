import pandas as pd
import numpy as np



if __name__=="__main__":
	data = pd.read_excel("./data/migration_full.xlsx",sheetname = "1990")
	data.fillna(0,inplace=True)
	print(data)