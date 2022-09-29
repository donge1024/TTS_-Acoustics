import textgrid as tg
import os





filePath = r'D:\FastSpeech2-master\preprocessed_data\obmgrid'
textgrid_file = os.listdir(filePath)

data = open(".\data.txt", 'w+')

for filename in textgrid_file:
    tgrid = tg.TextGrid()
    tgrid.read('D:\FastSpeech2-master\preprocessed_data\obmgrid\%s'%filename)
    # print('D:\FastSpeech2-master\preprocessed_data\obmgrid\%s'%filename)
    # tgrid = tg.read_textgrid(r'D:\FastSpeech2-master\preprocessed_data\LJSpeech\TextGrid\01.TextGrid', 'Phon')
    # for entry in tgrid:
    #     print(entry.name)
    # print(tgrid.tiers[0][21].mark)

    id = filename[:-9]
    print(id)

    print(id+"|LJSpeech|{",  end="", file=data)

    for i in range(len(tgrid.tiers[1])):
        if(i == (len(tgrid.tiers[1])-1)):
            print(tgrid.tiers[1][i].mark, end="", file=data)
        else:
            print(tgrid.tiers[1][i].mark, "", end="", file=data)

    print('}|', end="", file=data)

    txt = open('D:\FastSpeech2-master\wenben\%s.txt'%id, 'r+', encoding='gb18030', errors='ignore')
    line = txt.readline()
    if line.endswith('\n'):
        line = line[:-1]

    if (filename == textgrid_file[-1]):
        print(line, end='', file=data)
    else:
        print(line, file=data)




