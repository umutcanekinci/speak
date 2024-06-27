from gtts import gTTS
from io import BytesIO
from pygame import mixer
from os import remove

FILE = 'sound.mp3'

def Speak(text, language='tr') -> None:

    mixer.init()
    
    mp3_fo = BytesIO()
    tts = gTTS(text, lang=language)
    tts.write_to_fp(mp3_fo)
    mp3_fo.seek(0)

    with open(FILE, 'wb') as f:

        f.write(mp3_fo.read())
        
    mixer.music.load(FILE)
    
    
    print('Speaking..')

    mixer.music.play()
    while mixer.music.get_busy():
        continue

    print('Speaking ended.')

def TakeInput() -> str:

    print('_________________________________________________________________')
    print('What do you want me to say? (Enter exit() to quit)')
    print('_________________________________________________________________')

    return str(input('\n=> '))

def Main():

    read = TakeInput()

    if read != 'exit()':

        Speak(read)
        mixer.music.unload()
        remove(FILE)
        Main()
    

if __name__ == '__main__':

    Main()