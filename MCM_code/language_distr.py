import pandas as pd
import numpy as np


class migrate(object):
	def __init__(self):
		self.years = list(range(1996,2016))
	
		languages_temp = pd.read_excel("./data/country_languages.xlsx",sheetname="country",index_col=0)
		
		keep = np.logical_and(languages_temp["L1"]!=0,  languages_temp["L1"].notnull())
		languages_temp = languages_temp[keep]
		
		self.pop_in = pd.DataFrame({},index = languages_temp.index, columns = self.years)
		self.pop_out = pd.DataFrame({},index = languages_temp.index, columns = self.years)
		self.pop_total = pd.DataFrame({},index = languages_temp.index, columns = self.years)
		
		
		nums = list(range(1,7))
		Ls = ["L" + str(a) for a in nums]
		
		self.lang_dict = {}
		
		initial_pop = pd.read_excel("./data/population_full.xlsx").ix[languages_temp.index,]
		
		init_year = self.years[0]
		for country in languages_temp.index:
			#determine population a year before migration data
			temp = str(initial_pop.ix[country,init_year])
			pop = float(temp.replace(" ",""))
			
			langs = languages_temp.ix[country,Ls]
		
			langs.dropna(inplace=True)
			langs = langs.tolist()
			self.lang_dict[country] = langs
			
			if len(langs)>1:
				print(langs)
			else:
				self.pop_total.ix[country,init_year] = {langs[0]:pop}
				
		print(self.pop_total)
		
		
	def simulate(self):
		pass
		
	def model_ts(self):
		pass
		

if __name__=="__main__":
	data = migrate()