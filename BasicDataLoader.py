from pathlib import Path

def SGFDataLoader():
    def __init__(self):
        self.Size=0
        self.Rule=0


def PrcoessLocationInfo(loc):
    return (int(loc[0]-int(ascii('a'))),int(loc[1]-int(ascii('a'))))


def ProcessText(text):
    return

def readData(filePath):
    print(filePath)
    with open(filePath,"rb") as f:
        text=f.readlines()
        for i in text:
            print(i)
        f.close()


if __name__ == '__main__':
    filePath="Data/kgs-19-2019-04-new"
    file=list(Path(filePath).glob("*.sgf"))[0]
    readData(file)
