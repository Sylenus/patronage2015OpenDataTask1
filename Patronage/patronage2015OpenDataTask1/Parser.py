
import json  
import csv
import os

class Parser():		

	def __init__(self):
		try:
			try:
				#Open csv file
				f = open('Csv.csv', 'rU')  

				# Create 2 readers, one for keys, second for take keys argument

				readerForKey = csv.DictReader(f)
				reader = csv.DictReader(f, readerForKey.fieldnames)

				# Destroy readerForKey, no more needed 
				readerForKey = None
			
				try:
					#create and fill variable in json format
					toSave = json.dumps( [ row for row in reader ] )   

					#Creating json file
					f = open( 'jsonFile.json', 'w')  
					#Save json file
					f.write(toSave)  
					print "File parsed, all works fine!"  
					os.system('pause')

				except Exception:
					print("Problem with saving file, check local system permissions")

			except Exception:
				print("Error, can't open file. Csv file need to be in the same folder")
				
		except Exception:
			print("Unknown error, please contact with provider ", Exception)

if __name__ == "__main__":
	Parser()