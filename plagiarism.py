#!/usr/bin/python

#Importing Libaries and Initializing Variables :p
import requests as req
import os,sys
#from bs4 import BeautifulSoup
try:
	from googletrans import Translator
except Exception:
	print("Installing the Dependencies...")
	os.system("python -m pip install googletrans --user && clear")
	print("Please, Execute the Script Again!")
	sys.exit(0)
def main():
	translator = Translator()
	version = "1.0"


	#Print Banner
	print("""
__   __         _   ______           ______ _             _            _               
\ \ / /        | |  |  ___|          | ___ \ |           (_)          (_)              
 \ V /   _  ___| | _| |_ ___  _   _  | |_/ / | __ _  __ _ _  __ _ _ __ _ ___ _ __ ___  
  \ / | | |/ __| |/ /  _/ _ \| | | | |  __/| |/ _` |/ _` | |/ _` | '__| / __| '_ ` _ \ 
  | | |_| | (__|   <| || (_) | |_| | | |   | | (_| | (_| | | (_| | |  | \__ \ | | | | |
  \_/\__,_|\___|_|\_\_| \___/ \__,_| \_|   |_|\__,_|\__, |_|\__,_|_|  |_|___/_| |_| |_|
                                                     __/ |                             
                                                    |___/                   Version {}
---------------------------------------------------------------------------------------""".format(version))
	filename = input("Enter Text File Name: ")
	print("---------------------------------------------------------------------------------------")

	#Opening the text file and Getting it's Content
	with open(filename,'r') as f:
		content = f.read()

	#Translating the Content with Multiple Languages
	russian = translator.translate(content,src='en', dest='ru')
	spanish = translator.translate(russian.text, src='ru', dest='es')
	french = translator.translate(spanish.text, src='es', dest='fr')
	arabic = translator.translate(french.text, src='fr', dest='ar')
	english = translator.translate(arabic.text, src='ar', dest='en')

	#Printing on Screen
	print("Original Content: \n{}".format(content))
	print("\n\nNew Content: \n{}".format(english.text))

	#Getting filename without Extention and Creating new Filename for output
	newFilename = filename.split(".")
	new_filename = newFilename[0] + "_new.txt"

	#Writing the New Content in Output File
	with open(new_filename,'w') as ff:
		ff.write(english.text)
	print("\nOutput File: {}".format(new_filename))

if __name__ == "__main__":
	main()

#Coded by Farjaal Ahmad
#Creation Date: 15-01-2020
#YuckFou_Plagiarism v1.0
#Coded on Manjaro KDE
