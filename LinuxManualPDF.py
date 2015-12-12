#Author and Created by Pramod B Gosavi, feel free to write,
#mail:gosavi.pramod@gmail.com
#Please read readme.en before execute

import os
os.system("rm -rf LinuxManualPDF/")
os.system("mkdir LinuxManualPDF")
os.system("ls /usr/bin >> LinuxManualPDF/LinuxCommand")
f=open("LinuxManualPDF/LinuxCommand")
for line in f:
    command = "man -t "+str(line[:-1])+" | pdf2ps - LinuxManualPDF/"+str(line[:-1])+".pdf"
    os.system(command)

f.close()
