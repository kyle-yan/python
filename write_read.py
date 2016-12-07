fw = open('sample.txt', 'w')  #open a txt document and make it writable
fw.write('ahahahahaha\n')
fw.write('hohohohohoh\n')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()
