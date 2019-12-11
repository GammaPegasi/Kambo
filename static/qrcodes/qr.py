import os

def create_codeQR(url, filename):
    command = "qr --factory=svg " + url  + " > " + filename
    os.popen(command)
    print('New code ', url, 'File: ', filename)

# url = "https://kambo.pythonanywhere.com/cross_header/"
# url = "https://kambo.pythonanywhere.com/find_files/"

url = "https://kambo.pythonanywhere.com/qr_code/"

filename = "qr_code.svg"

create_codeQR(url, filename)
