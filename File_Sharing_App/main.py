import os 
import platform
import http.server 
import socket 
import socketserver 
import webbrowser
import pyqrcode 
from pyqrcode import QRCode 
import png 

def FileSharing():
    PORT = 8010
    if platform.system() == "Windows":   
        desktop = os.path.join(os.getenv('USERPROFILE'),'Downloads')
    else:
        desktop=os.path.expanduser("~/Downloads")
    os.chdir(desktop)
    # creating a http request
    Handler = http.server.SimpleHTTPRequestHandler
    # returns, host name of the system
    hostname = socket.gethostname()
    # finding the IP address of the PC
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)##UDP protocol
    s.connect(("8.8.8.8", 80))
    IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
    link = IP
    # converting the IP address into the form of a QRcode
    url = pyqrcode.create(link)
    # saves the Qrcode in form of svg
    url.svg("FileSharing.svg", scale=8)
    # opens the Qrcode image in the web browser
    webbrowser.open('FileSharing.svg')
    # Creating the HTTP request and  serving the
    # folder in the PORT 8010,and the pyqrcode is generated
    # continuous stream of data between client and server
    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        print("serving at port", PORT)
        print("Type this in your Browser", IP)
        print("or Use the QRCode")
        httpd.serve_forever()
if __name__=='__main__':
    FileSharing()