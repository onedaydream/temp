from os.path import isfile, join
from os import listdir
from shutil import copyfile
import os
import csv

filenames = []
categorys_1 = []
categorys_2 = []
categorys_3 = []


def loadCsvFile():
    with open('Pictures.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter = ',')

		global filenames
		global categorys_1
		global categorys_2
		global categorys_3

		for row in readCSV:
			filename = row[0]
			category_1 = row[1]
			category_2 = row[3]
			category_3 = row[5]

			filenames.append(filename)
			categorys_1.append(category_1)
			categorys_2.append(category_2)
			categorys_3.append(category_3)

	
'''
def seperateData(data_dir):
    for filename in listdir(data_dir):
        if isfile(join(data_dir, filename)):
            tokens = filename.split('.')
            image_path = join(data_dir, filename)
            for file in filenames:
            	if 
            if not os.path.exists(join(data_dir, tokens[0])):
                os.makedirs(join(data_dir, tokens[0]))
            copyfile(image_path, join(join(data_dir, tokens[0]), filename))
            os.remove(image_path)
'''

if __name__=="__main__":
    loadCsvFile()
 #   seperateData("./picture")
    print (filenames)

