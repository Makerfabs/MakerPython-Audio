from machine import I2S
from machine import Pin
import array
import speech


bck_pin = Pin(26)
ws_pin = Pin(25)
sdout_pin = Pin(27)


audio_out = I2S(I2S.NUM0,
                bck=bck_pin,
                ws=ws_pin,
                sdout=sdout_pin,
                standard=I2S.PHILIPS,
                mode=I2S.MASTER_TX,
                dataformat=I2S.B16,
                channelformat=I2S.ONLY_RIGHT,
                samplerate=16000,
                dmacount=16,
                dmalen=512)

a = bytearray(16000*8)
size = speech.say('the temperature is twenty six degree', a)
audio_out.write(a[:size])

def say(text):
    a = bytearray(16000*8)
    size = speech.say(text, a)
    audio_out.write(a[:size])
    
    
def close():
    audio_out.deinit()
