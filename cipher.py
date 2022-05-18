
class FileDecoder:
    def __init__(self, key, filename, alphabet):
        self.key        = key
        self.filename   = filename
        self.alphabet   = alphabet
        self.listIndex  = 0
        self.decodeList = self.getDecodeList()
        
    def __str__(self):
        return "FileDecoder(key=" + self.key + "', file='"+ self.filename +"')"

    def __len__(self):
        return len(self.decodeList)

    def __iter__(self):
        return self

    def __next__(self):
        if self.listIndex >= len(self.decodeList):
            raise StopIteration
        index = self.listIndex
        self.listIndex += 1
        return self.decodeList[index]

    def getDecodeList(self):
        file_handle    = open(self.filename,'r')
        keyIndex       = 0
        decodeLineList = []
        tempString     = ''

        for line in file_handle:
            for char in line:
                encrpyt    = self.alphabet.index(char)
                keyVal     = self.alphabet.index(self.key[keyIndex])
                decode     = (encrpyt - keyVal) % len(self.alphabet)
                tempString = tempString + self.alphabet[decode]

                if(self.alphabet[decode] == '\n'):
                    decodeLineList.append(tempString)
                    tempString = ''
        
                keyIndex+=1
                if(keyIndex == len(self.key)):
                    keyIndex = 0
        return decodeLineList

            

    