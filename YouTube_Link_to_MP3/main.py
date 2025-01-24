from pytubefix import YouTube
import os 
import platform

def YouTube2Mp3():
    ##URL and Youtube object creation
    yt=YouTube(str(input('Enter your URL: ')),'WEB')
    
    ##extract the audio
    video=yt.streams.filter(only_audio=True).first()
    
    ##destination allocation
    # print('Enter your destination folder(leave blank for current directory)')
    if platform.system() == 'Windows':
        destination=os.path.join(os.getenv('USERPROFILE'),'Music')
    else:
        destination=os.path.expanduser("~/Music")
    
    ##video download
    out_file=video.download(output_path=destination)
    
    ##save the file
    base,extension=os.path.splitext(out_file)
    new_file=base+'.mp3'
    os.rename(out_file,new_file)
    
    ##success
    print(yt.title+" has been successfully downloaded and saved to "+destination)
    print('File Extension: '+extension)
    print('File base: '+base)
    print('OutFile: '+out_file)
    print('Destination: '+destination)

if __name__=="__main__":
    YouTube2Mp3()
    