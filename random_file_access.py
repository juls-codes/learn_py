import struct

def ReadData():
    f = open('test.bin','rb')
    byteData = f.read()
    f.close()
    tupD = struct.unpack('i 20s 12s', byteData)
    print(tupD[0], tupD[1], tupD[2]) #tupD[0] is memberID, tupD[1] is memberName, tupD[2] is memberPhone
    return

memberID=1234
memberName='John Smith'
memberPhone='519-222-2222'

f = open('test.bin','wb') #write in binary form to test.bin
f.write(struct.pack('i 20s 12s', memberID, bytes(memberName,'utf-8'),bytes(memberPhone,'utf-8'))) #in this case, .pack() will package the data in binary form

f.close()

ReadData()

#because John Smith is less than 20 characters, the rest of the characters in the print statement is occupied by NULL
#bytes() is a function that will encode the data assigned to the variable in utf-8

