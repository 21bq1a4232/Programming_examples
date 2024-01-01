import PyPDF2,pyttsx3
path=open(r'C:\Users\prana\OneDrive\Desktop\Programming\Sem\AI\Unit-1.pdf','rb')
pdfReader=PyPDF2.pdfFileReader(path)
speak=pyttsx3.init()
for pages in range(pdfReader.numPages):
    text=pdfReader.getPage(pages).extractText()
    speak.say(text)
    speak.runAndWait()
speak.stop()