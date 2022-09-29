import os

filePath = r'D:\FastSpeech2-master\wen10'
txt_file = os.listdir(filePath)

file = open('D:\FastSpeech2-master\wen10\standard.txt', 'w' , encoding='utf-8')
for filename in txt_file:
    idx = filename[:-4]
    with open('%s/%s'%(filePath,filename), 'r') as f:
        line = f.readline()
        if line.endswith('\n'):
            line = f.readline()[-1]
    print("%s|%s|%s" % (idx, line, line), end='', file=file)
    if filename != txt_file[-1]:
        print('', file=file)
file.close()