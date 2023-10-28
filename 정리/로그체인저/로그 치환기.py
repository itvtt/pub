import sys
import win32con, win32api, os
import codecs  # utf-8 읽어 오기 위해


class CReplaceAllText():
    def __init__(self, path, fromText, toText):
        self.cntFiles = 0
        self.path = path
        self.FromText = fromText.lower()  # 대소문자 구분 없이 변경하기 위해 fromText를 소문자로 변환
        self.ToText = toText.lower()  # 대소문자 구분 없이 변경하기 위해 toText를 소문자로 변환

    # lookupExt : 대상 확장자(.java)
    def startReplaceText(self, path, lookupExt):
        for fname in os.listdir(path) :
            fullname = os.path.join(path, fname)

            if os.path.isdir(fullname) :
                self.startReplaceText(fullname, lookupExt)

            elif os.path.isfile(fullname) :
                ext = os.path.splitext(fullname)[-1]
                if ext != lookupExt:
                    continue

                ret = self.replaceText(fullname)
                self.cntFiles += ret

        if (path == self.path) :
            print('%s --> %s 로 변경, 변경 개수 %d' %(self.FromText, self.ToText, self.cntFiles))



    def replaceText(self,filename):
        bIsUtf = False
        f = open(filename, "r")
        try :
            lines = f.readlines()
        except:
            bIsUtf = True
            f.close()
            f = codecs.open(filename, "r", 'utf-8')
            lines = f.readlines()
        f.close()

        bFind = False
        wlines = []
        for line in lines:
            wline = line.lower()  # 대소문자 구분 없이 변경하기 위해 line을 소문자로 변환
            if self.FromText in wline:
                bFind = True
                wline = wline.replace(self.FromText, self.ToText)
                wline = line.replace(line, wline)  # 원래의 대/소문자 그대로 출력하기 위해 line으로 변경
            wlines.append(wline)


        if bFind == False:
            return 0

        # 파일이 읽기 전용일 경우 쓰기 가능으로 변경
        win32api.SetFileAttributes(filename, win32con.FILE_ATTRIBUTE_NORMAL)

        if bIsUtf == False:
            f = open(filename, 'w')
            print('%s --> %s 로 변경 %s' % (self.FromText, self.ToText, filename))
        else:
            f = codecs.open(filename, "w", 'utf-8')
            print('%s --> %s 로 변경 %s(utf-8 format)' % (self.FromText, self.ToText, filename))

        f.writelines(wlines)
        f.close()
        return 1


if __name__ == "__main__":
    lookupPath = 'D:\\logchanger'
    # D:\dev\prj\hello\log
    objRep = CReplaceAllText(lookupPath, 'a', '*****')
    objRep.startReplaceText(lookupPath, '.xlsx')
