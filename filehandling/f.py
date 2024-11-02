try:
    f=open('/home/novavi/Desktop/shino/exam/filehandling/sample.txt','w')
    f.write('welcome home')
except:
    print('file exists')
f=open('/home/novavi/Desktop/shino/exam/filehandling/sample.txt','r')
print(f.read())


    


