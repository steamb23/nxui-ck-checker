from modulefinder import IMPORT_NAME

import clipboard
import main

while (1):
    result = main.GetReport()
    nospace = result.replace(" ","").replace("\n","").replace("\r","")
    nospace_len = len(nospace)
    print("공백제외 글자수: %d\n" % nospace_len)
    print(result)
    if (nospace_len < 200):
        print("글자 수가 적습니다. 재시도합니다...\n")
    else:
        clipboard.copy(result)
        break