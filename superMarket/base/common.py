#공통모듈
class Common:
    def txtWrite(self,filename,data):
        try:
            f = open(filename, 'a')
        except FileNotFoundError as e:
            print('파일이 없습니다')
        else:
            try:
                f.write(data + '\n')
            except Exception as e:
                print('예외발생')
            else:
                f.close()

    def txtRead(self,filename):
        try:
            f = open(filename, 'r')
        except FileNotFoundError as e:
            print('파일이 없습니다')
        else:
            try:
                print('-' * 15)
                print(f.read())
                print('-' * 15)
                input('상품조회 완료...')
            except Exception as e:
                print('예외발생')
            else:
                f.close()


#
# def fileWrite(fileName):
#