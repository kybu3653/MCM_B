import pandas as pd
import numpy as np
import datetime as dt

#calculates the benefit of putting a building at a given point
def calculate_benefit(point,weight = 1/10):
	languages = point.keys()

	english = []
	non_english = []
	
	#separate english speakers from non-english speakers
	for language in languages:
		lang = language.split("-")
		if "English" in lang:
			english.append(language)
		else:
			non_english.append(language)
			
	benefit = 0
	for element in english:
		lang = element.split("-")
		if len(lang)==1: 
			benefit+=point[element[0]]
		else:
			for i in element:
				if i != "English":
					try:
						num_speakers = point[i]
					except(KeyError):
						num_speakers = 0
					benefit += (1+weight * num_speakers)*point[
			
		



if __name__ == "__main__":
	data = {"English":4,"1":5,"2":5,"3":6,"English-Lingual":6}
	calculate_benefit(data)