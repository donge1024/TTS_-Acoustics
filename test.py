import os

txt = open('D:\FastSpeech2-master\preprocessed_data\obmgrid\\metadata.txt', 'r+')


lines = txt.readlines()
#print (len(lines))
#提取每一行，两个|之间的内容到新的txt
with open('D:\FastSpeech2-master\preprocessed_data\obmgrid\\stand.txt', 'r') as reader:
     # Read and print the entire file line by line
     line = reader.readline()
     while line != '':  # The EOF char is an empty string
         #print(line, end='')
         start = (line.find('|'))
         end = (line.rfind('|'))
         number = line[0:3]
         print(number)
         line = line[start + 1:end]
         print(line)

         file = open("D:\FastSpeech2-master\preprocessed_data\obmgrid\%s.txt"%number, "w")
         file.write(str(line))

         line = reader.readline()

