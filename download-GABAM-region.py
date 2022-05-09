##finds ftp files of a certain region and downloads them, e.g. 
#ftp://124.16.184.141/GABAM/burned%20area/2009/N10W080.TIF
import ftplib
import numpy as np
import urllib.request

region = "N10W070"

ftp = ftplib.FTP("124.16.184.141")
ftp.login("", "")
ftp.cwd('GABAM/burned area')

##if wanting more information about the files in a directory:
#data = []
#ftp.dir(data.append)

filelist = ftp.nlst()
print("total files: ",len(filelist))
ftp.quit()

for year in filelist:
  FTPaddress = "ftp://124.16.184.141/GABAM/burned%20area/"+year+"/"+region+".TIF"
  FileOutput = year+"_"+region+".TIF"
  print("Downloading",FTPaddress,"to",FileOutput)
  urllib.request.urlretrieve(FTPaddress, FileOutput)
print("done")