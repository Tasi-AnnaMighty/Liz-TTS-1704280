from nltk import *
import nltk
from tkinter import *
import tkinter
from gtts import gTTS
import os
import eel
import PyPDF2
from requests import NullHandler
import urllib


eel.init("web")

os.system('cls || clear')

@eel.expose
def speak(data):
    #print(2)
    text=data
    tokenize(text)

    output= gTTS(text,lang="en",slow=False)

    #output.save("C:/Users/My PC/Documents/UTECH/Sem 9/APL/Liz/web/output.mp3")
    output.save("output.mp3")
    #Opens media player
    os.system("start output.mp3")

    #path= "output.mp3"

    return text
	
@eel.expose
def filespeak(file):
    print(file)
    fh=open(file,"r")
    print(fh)
    mytext = fh.read().replace("/n"," ")
    speak(mytext)
    return None

@eel.expose
def urlspeak(article):
    print(article)

    url = urllib.request.urlopen(article)
    urlData = url.read().decode("utf8")

    #Cleaning the hex codes
    cleanr = re.compile('<.*?>')
    cleanText = re.sub(cleanr, '', urlData)

    for r in (("&#x27;", "'"), ("&quot", " ")):

        urlText = cleanText.replace(*r)
  
    #print(urlText)
    speak(urlText)
    #tokenize(urlText)

    return None

@eel.expose
def open_file():
    self=Tk()
    file = tkinter.filedialog.askopenfilename(initialdir="/",title="Select file", filetypes=[('Text files', '*.txt'),('Pdf files','*.pdf')])
    if file is not None:
        content=file.split('.')
        if (content[1]=="txt"):
            filespeak(file)
        else:
            pdfspeak(file)
        pass
        Tk.destroy(self)
    return None

def pdfspeak(file):
    pdf_obj=open(file,'rb')
    pdf_reader= PyPDF2.PdfFileReader(pdf_obj)
	
    print(pdf_reader.numPages)
	
    page_obj=pdf_reader.getPage(0)
    speak(page_obj.extractText())
    pdf_obj.close()
	
    return None

def tokenize(data):
    print("------ Length of Text -----")
    x = len(word_tokenize(data))
    print("You typed", x, "words.", "\n")
    print ("------ Word Tokenization -----")
    print(word_tokenize(data))
    print("\n")
    print ("------ Sentence Tokenization -----")
    print(sent_tokenize(data))
    print ("\n")
    print ("------ Punctuation Tokenization -----")
    print(WordPunctTokenizer().tokenize(data))
    print ("\n")
    print ("------ Regular Expression Tokenizer -----")
    print(regexp_tokenize(data, "[\w']+"))
   
    return None 

eel.start("Home.html", port = 9000)