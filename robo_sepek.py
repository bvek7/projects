import os
if __name__=="__main__":
    while True:
        x=input("enter what u want me to speak")
        if(x=="e"):
            break
        command = f'powershell.exe -Command "Add-Type -AssemblyName System.Speech; $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; $speak.Speak(\'{x}\')"'
        os.system(command) 
        