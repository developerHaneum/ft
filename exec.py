# Finding Text at file and directory
import os.path
import sys
import os
x = 0
y = 0
def Isfile(file):
    if os.path.isfile(file):
        return 1
    else:
        return -1

def Isdir(path):
    if os.path.isdir(path):
        return 1
    else:
        return -1

def FindFile(path, text):
    isfile = Isfile(path)
    if isfile == -1:
        return 0
    file = open(path, "rb")
    load = file.read() # Bytes load
    file.close()
    read  = load.decode(encoding="utf-8") # Bytes -> Str
    if read.find(text) == -1:
        return -1  # Path 파일에 일치하는  text는 없어요
    else:
       return 1 # 있어요
def FindDir(path, text):
    global x
    if Isdir(path) == -1:
        return 0 # No directory
    dir_list = os.listdir(path)
    if '.git' in dir_list:
        dir_list.remove('.git')
    if '.github' in dir_list:
        dir_list.remove('.github')
    if '.DS_Store' in dir_list:
        dir_list.remove('.DS_Store')
    leng = len(dir_list) # value
    for i in range(1, leng+1):
        name = "".join(dir_list[i-1])
        file = path + '/' + dir_list[i-1]
        if name.find(".") != -1: # file
            find = FindFile(file, text)
            if find != -1:
                x = 0 + 1
                ext = "%s"%file
                print("%s"%ext)
        else: # dir
            dir = FindDir(file, text)
    if x == 0:
        return -1 # 파일에 찾는 문자열이 없다면
    return '' # No return of value (1: extant)
def TextInput():
    return sys.argv[1]

def PathInput():
    return sys.argv[2]
def NowDir():
    return os.path.dirname(os.path.abspath(__file__))
def TextLower(text):
    return text.lower()
def TextUpper(text):
    return text.upper()
def ManHelp():
    ManVer()
    now = NowDir()
    help_file = now + "/doc/help.md"
    isfile = Isfile(help_file)
    if isfile == -1:
        print("Error: No help.md file")
        return -1
    file = open(help_file, "rb")
    load = file.read()
    file.close()
    print(load.decode(encoding="utf-8")) # Prints
def ManVer():
    now = NowDir()
    ver_file = now + "/doc/version.md"
    isfile = Isfile(ver_file)
    if isfile == -1:
        print("Error: No version.md file")
        return -1
    file = open(ver_file, "rb")
    load = file.read()
    file.close()
    print(load.decode(encoding="utf-8")) # Prints
def ManIndexErrorHelp(flag):
    print("error: No '%s' flags"%flag)
    now = NowDir()
    err_file = now + "/doc/error_help.md"
    isfile = Isfile(err_file)
    if isfile == -1:
        print("Error: No error_help.md file")
        return -1
    file = open(err_file, "rb")
    load = file.read()
    file.close()
    print(load.decode(encoding="utf-8")) # Prints
try:
    text = '' # NameError 방지해요
    text = TextInput()
    # Flags
    text = TextLower(text) # Flag 때문에 소문자로 변경해요
    if (text.find("-h")==0 or text.find("--h")==0):
        ManHelp()
        sys.exit(0)
    if (text.find("-v")==0 or text.find("--v")==0):
        ManVer()
        sys.exit(0)
    path = PathInput()
    # Opptions
    if path.find("!")==0:
         path = os.getcwd()
    if len(sys.argv) > 3:
        sys.exit(1) # 비정상 종료에요
    # Find
    for i in range(1, 3):
        if i == 1:
            text = TextLower(text)
        else:
            text = TextUpper(text)
        dir = FindDir(path, text)
        if dir == -1: # -1 of dir
            #print(-1)
            y = 3
        elif dir == 0: # 0 of dir or file: 1 or -1
            file = FindFile(path, text)
            if file == 0:
                y = 2
                #print(0) # file or dir of No find value
            else:
                if i == 1:
                    print(file) # file of 1 or -1
        else: # 1
            y = 1
    if y == 2:
        print(0)
    if y == 1:
        print(1)
    if y == 3:
        print(-1)
    
except IndexError:
   ManIndexErrorHelp(text)
except UnicodeDecodeError:
    pass
