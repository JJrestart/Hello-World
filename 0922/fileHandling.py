# fread = None

# try : 
#     fread = open('test.dat', 'r')
#     # result = fread.readline()
#     # while result :
#     #     print(result, end='')
#     #     result = fread.readline()
#     for line in fread.readlines():
#         print(line, end='')
# except : 
#     print("File Not Found")
# finally : 
#     fread.close()

# poet = """
# 죽는 날까지 하늘을 우러러
# 한 점 부끄럼이 없기를,
# 잎새에 이는 바람에도
# 나는 괴로워했다.
# 별을 노래하는 마음으로
# 모든 죽어 가는 것을 사랑해야지
# 그리고 나한테 주어진 길을
# 걸어가야겠다.

# 오늘 밤에도 별이 바람에 스치운다.
# """

# fwrite = None
# try:
#     fwrite = open('test2.txt','w')
#     fwrite.write(poet)
# except Exception as err:
#     print(err)
# finally:
#     fwrite.close()

with open('test2.txt', 'rt') as fread :
    try : 
        count = 1
        for line in fread.readlines() :
            print(f'{count} : {line}',end='')
            count += 1
    except : 
        print("File Not Found")