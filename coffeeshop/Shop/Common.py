#공통 모듈
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
                print('관리자에게 문의 부탁드립니다.')
            else:
                f.close()

    def txtRead(self,filename):
        try:
            f = open(filename, 'r')
        except FileNotFoundError as e:
            print('파일이 없습니다')
        else:
            try:
                print('=' * 15)
                print(f.read())
                print('=' * 15)
                input('메뉴 확인 완료!')
            except Exception as e:
                print('관리자에게 문의 부탁드립니다.')
            else:
                f.close()
