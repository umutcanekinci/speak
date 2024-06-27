from gtts import gTTS
from io import BytesIO
from pygame import mixer
from os import remove

FILE = 'sound.mp3'
LANGUAGE = 'tr'

def Speak(text, language) -> None:

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

    print('_____________________________________________________________________________________________________')
    print('What do you want me to say? (Enter exit() to quit, !tr for Turkish, !en for English, etc.)')
    print('_____________________________________________________________________________________________________')

    return str(input('\n=> '))

def Main():

    read = TakeInput()

    if read.startswith('!'):

        Main.language = read[1:]
        print(f'\nLanguage set to {Main.language}.')
        read = TakeInput()

    if read != 'exit()':

        Speak(read, Main.language)
        mixer.music.unload()
        remove(FILE)
        Main()
    

if __name__ == '__main__':

    Main.language = LANGUAGE
    Main()