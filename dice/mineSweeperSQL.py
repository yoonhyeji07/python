from cx_Oracle import *


class PlayerToServer:
    def __init__(self):
        pass

    def playerList(self):
        conn = connect('hr/hr@localhost:1521/xe')
        cur = conn.cursor()
        cur.execute('select MP.playerName\
                    from minePlayer MP\
                    join minePlayerStatus MPS\
                    on(MP.playerName = MPS.playerName)')
        playerList_ = cur
        cur.close()
        conn.close()
        if playerList_: return playerList_
        else:
            print("Player doesn't exist!")
            return

    def register(self, data):  # data = (playerName, playerPassword)
        try:
            conn = connect('hr/hr@localhost:1521/xe')
            cur = conn.cursor()
            cur.execute('insert into minePlayer\
                        values(:1, :2)', data)
            playerID, playerPW = data
            data = (playerID, 0, 0)
            cur.execute('insert into minePlayerStatus\
                        values(:1, :2, :3)', data)
            cur.close()
            conn.commit()
            conn.close()
        except KeyboardInterrupt:
            exit(0)

        print("\nAutomatically login with registered account...\n")

    # def login(self, data):  # data = (playerName, playerPassword)
    #     playerID, playerPW = data  # unpacking tuple-type data
    #     self.playerFind((playerID,))  # search ID
    #
    # def playerFind(self, data):  # data = playerName or 'separation of name'
    #     conn = connect('hr/hr@localhost:1521/xe')
    #     cur = conn.cursor()
    #     cur.execute('''select *
    #                 from minePlayer MP
    #                 join minePlayerStatus MPS
    #                 on(MP.playerName = MPS.playerName)
    #                 where MP.playerName like '%' || :1 || '%' ''', data)
    #     if not cur: return False
    #
    #     for info in cur:
    #         print(info)
    #     cur.close()
    #     conn.close()

    def login2(self, data):  # data = (playerName, playerPassword)
        playerID, playerPW = data  # unpacking tuple-type data
        dataID = (playerID,)
        conn = connect('hr/hr@localhost:1521/xe')
        cur = conn.cursor()
        if ServerToPlayer.playerCheck(dataID):
            print("login with '%s'..." % playerID)
        else: print("unavailable ID")
        cur.close()
        conn.close()

    def winCount(self, data):
        conn = connect('hr/hr@localhost:1521/xe')
        cur = conn.cursor
        cur.execute('Update ')
        cur.close()
        conn.close()
        print("winCount +1")

    def lostCount(self, data):
        conn = connect('hr/hr@localhost:1521/xe')
        cur = conn.cursor
        cur.execute('')
        cur.close()
        conn.close()
        print("lostCount +1")

    def __del__(self):
        pass

class ServerToPlayer:
    def playerCheck(self, dataID):  # data = (playerID,)
        conn = connect('hr/hr@localhost:1521/xe')
        cur = conn.cursor()
        cur.execute('select playerName from minePlayer')
        for names in cur:
            if names == dataID: return True
        cur.close()
        conn.close()

    def passwordCheck(self, dataPW):  # data = (playerPW,)
        conn = connect('hr/hr@localhost:1521/xe')
        cur = conn.cursor()
        cur.execute('select playerPassword from minePlayer')
        for password in cur:
            if password == dataPW:
                return True
            else:
                return False
        cur.close()
        conn.close()

    def getWinCount(self, data):  # data = (playerID,)
        conn = connect('hr/hr@localhostL1521/xe')
        cur = conn.cursor
        cur.execute('select winCount from minePlayerStatus')
        cur.close()
        conn.close()

    def getLoseCount(self, data):  # data = (playerID,)
        conn = connect('hr/hr@localhostL1521/xe')
        cur = conn.cursor
        cur.execute('select lostCount from minePlayerStatus')
        cur.close()
        conn.close()

# print(PlayerToServer.playerList(''))
# dataTemp = ('id', 'pw')
# dataTemp2 = ('id2', 'pw2')
# dataTemp3 = ('id3', 'pw3')
# dataTemp4 = ('id4', 'pw4')
# player = PlayerToServer()
# player.register(dataTemp3)
# player.login2(dataTemp2)
