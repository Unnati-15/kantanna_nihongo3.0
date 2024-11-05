import codecs
from django.shortcuts import render
import nltk
nltk.download('punkt_tab')
import pyttsx3
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.conversation import Statement
import speech_recognition as sr
from manga_ocr import MangaOcr
from PIL import Image
import pykakasi
from django.contrib import messages

def indexchatbot(request):
    chatBot = ChatBot('Norman')
    trainer = ChatterBotCorpusTrainer(chatBot)

    trainer.train("chatterbot.corpus.japanese")
    
    if request.method == 'POST':
        
        form = request.POST['message']
        user_message = form
        engine = pyttsx3.init()
        jp_voiceid = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_JA-JP_HARUKA_11.0"
        engine.setProperty('voice',jp_voiceid)
        engine.say(user_message)
        engine.runAndWait()
        bot_response = chatBot.get_response(Statement(text=user_message,search_text=user_message))
        print(user_message)
        print(bot_response) 
        engine.say(bot_response)
        engine.runAndWait()
        return render(request, 'templates/chatbot.html', {'user_message': user_message, 'bot_response': bot_response})
    else:
        return render(request, 'templates/chatbot.html')


def textspeech(request):
    if request.method == 'POST':
        formts = request.POST['myfile']
        #with codecs.open(formts,'r') as file:
       #     text = file.read()
        text=formts
        print(text)
        engine = pyttsx3.init()
    #voices = engine.getProperty('voices')
    #for voice in voices:
    #    print("voice :")
    #    print("id :%s"%voice.id)
    #    print("name :%s"%voice.name)
     #   print("language :%s"%voice.languages)
      #  print("gender :%s"%voice.gender)
        jp_voiceid = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_JA-JP_HARUKA_11.0"
        engine.setProperty('voice',jp_voiceid)
   
    #text = "こんにちは！私はロボットです。"
        engine.say(text)
        engine.save_to_file(text,'speech.mp3')
        engine.runAndWait()
        messages.info(request,'audio file is ready!')
    return render(request, 'templates/t.html')

def speechtext(request):
# Initialize the recognizer
    r = sr.Recognizer()

# Load the audio file
    if request.method == 'POST' and request.FILES['myfilest']:
            myfilest = request.FILES['myfilest']
            audio_file = sr.AudioFile(myfilest)
            with audio_file as source:
                    audio_data = r.record(source)
            try:
                text = r.recognize_google(audio_data,language = "ja-JP")
                print("Transcription: ", text)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand the audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

            return render(request, 'templates/t2.html',{'text':text})

    else:
        return render(request, 'templates/t2.html')


def imgrecog(request):
     mocr = MangaOcr()
     if request.method == 'POST' and request.FILES['myfilestimg']:
            image_path = request.FILES['myfilestimg']
            image1 = Image.open(image_path)
            text = mocr(image1)
            kks = pykakasi.kakasi()   
            result = kks.convert(text)
            print(result)
            return render(request, 'templates/t3.html',{'result':result})

     else:
        return render(request, 'templates/t3.html')
'''def imgrecog(request):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust the path accordingly
    image_path = 'static\gambare.png'
    image = cv2.imread(image_path)

# Convert image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Perform OCR
    custom_config = r'--oem 3 --psm 6 -l j'  # Using Japanese language
    recognized_text = pytesseract.image_to_string(image_rgb, config=custom_config)

    print("Recognized Text:")
    print(recognized_text)'''