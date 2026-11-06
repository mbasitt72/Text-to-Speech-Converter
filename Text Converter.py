from gtts import gTTS
import os
print("------Text to audio Converter------")
print("-----MENU----")
print("1. English (en)")
print("2. Urdu (ur)")
print("3. Hindi (hi)")
print("4. Arabic (ar)")
print("5. French (fr)")
print("6. Spanish (es)")
choice = int(input("Select a language: "))
 
filename = input("\nEnter output filename: ")

if choice ==1:
    text=str(input("Enter text to convert to audio:"))
    print("Normal Audio or Slowed")
    a=input()
    if a=="Normal":
        tts=gTTS(text=text ,lang="en")
        tts.save(filename + ".mp3")
    elif a=="Slowed":
        tts=gTTS(text=text ,lang="en",slow=True)
        tts.save(filename + ".mp3")
    
elif choice==2:
    text=str(input("Enter text to convert to audio:"))
    print("Normal Audio or Slowed")
    a=input()
    if a=="Normal":
        tts=gTTS(text=text ,lang="ur")
        tts.save(filename + ".mp3")
    elif a=="Slowed":
        tts=gTTS(text=text ,lang="ur",slow=True)
        tts.save(filename + ".mp3")

elif choice==3:
    text=str(input("Enter text to convert to audio:"))
    print("Normal Audio or Slowed")
    a=input()
    if a=="Normal":
        tts=gTTS(text=text ,lang="hi")
        tts.save(filename + ".mp3")
    elif a=="Slowed":
            tts=gTTS(text=text ,lang="hi",slow=True)
            tts.save(filename + ".mp3")

elif choice==4:
    text=str(input("Enter text to convert to audio:"))
    print("Normal Audio or Slowed")
    a=input()
    if a=="Normal":
        tts=gTTS(text=text ,lang="ar")
        tts.save(filename + ".mp3")
    elif a=="Slowed":
        tts=gTTS(text=text ,lang="ar",slow=True)
        tts.save(filename + ".mp3")

elif choice==5:
    text=str(input("Enter text to convert to audio:"))
    print("Normal Audio or Slowed")
    a=input()
    if a=="Normal":
        tts=gTTS(text=text ,lang="fr")
        tts.save(filename + ".mp3")
    elif a=="Slowed":
        tts=gTTS(text=text ,lang="fr",slow=True)
        tts.save(filename + ".mp3")

elif choice==6:
    text=str(input("Enter text to convert to audio:"))
    print("Normal Audio or Slowed")
    a=input()
    if a=="Normal":
        tts=gTTS(text=text ,lang="es")
        tts.save(filename + ".mp3")
    elif a=="Slowed":
        tts=gTTS(text=text ,lang="es",slow=True)
        tts.save(filename + ".mp3")

        
print("\nAudio generated successfully!")
print("File saved as:", os.path.abspath(filename))
 


   