import requests
import json
from tkinter import *
import tkinter as tk

DEBUG = False

lang = "mandalorian"
url = "https://api.funtranslations.com/translate/" + lang + ".json?text="
global userInput
userInput = ""
finalValue = "Translated text here"

class toTranslate(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)

		global textVar
		textVar = tk.StringVar(self, value="Translated text here")

		self.title("Translation")
		self.geometry('350x200')
		self.inputField = tk.Entry(width=100)
		self.inputField.pack()
		self.btn = tk.Button(self, text="Translate", command=self.on_button)
		self.btn.pack()
		self.showLabel = Label(textvariable=textVar)
		self.showLabel.pack()

	def cleanString(inputString):
		inputString = inputString.replace(" ", "%20").replace("'", "%27d")
		return inputString

	def on_button(self):
		content = self.inputField.get()
		if DEBUG: print("DEBUG: content=%s" % content)
		toTranslate.doTranslation(content)

	def doTranslation(userInput):
		cleanedString = toTranslate.cleanString(userInput)
		if DEBUG: print("DEBUG: userInput=%s" % userInput)
		if DEBUG: print("DEBUG: cleanedString=%s" % cleanedString)
		fullURL = url + cleanedString
		if DEBUG: print(fullURL)

		grab = True
		if grab == True:
			resp = requests.get(fullURL)
			data = resp.json()
			if DEBUG: print(resp)
			if DEBUG: print(json.dumps(data, indent=4, sort_keys=True))

			try:
				translated = data["contents"]["translated"]
				if DEBUG: print("Translated text: " + str(translated))
				finalValue = translated
			except:
				#For if too many API hits
				translated = data["error"]["message"]
				if DEBUG: print(str(translated))
				#finalValue = translated
				finalValue = "Error: probably too many requests"

		textVar.set("Translation: " + str(finalValue))

app = toTranslate()
app.mainloop()