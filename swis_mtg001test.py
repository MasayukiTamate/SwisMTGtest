import random

minna = "たま","かわ","おお","あい","しが","かし","りょ"


#クラス　プレイヤーデータ
class PlayerData:
    def __init__(self, name, no):
        self.namae = name
        self.No = no
        self.Mpoint = 0
        self.MpointPar = 0.000
        self.OpMpPar = 0.000
        self.TaisenAite = []
        self.TaisenAiteNo = []
        self.KaisuTaisen = 0
    def Hyouji(self):
        print(f"{self.No+1} {self.namae} 勝ち点：{self.Mpoint} mp%：{self.MpointPar} opmp%：{self.OpMpPar} 対戦履歴：{self.TaisenAite}")
    def TaisenNyuryoku(self, aite, no):
        self.TaisenAite.append(aite)
        self.TaisenAiteNo.append(no)

#クラス　初席決め
class RandmInit:
    def __init__(self, ninsu):
        self.ninsu = ninsu
        self.suretu = [x for x in range(self.ninsu)]
        self.kariList = []
        self.honList = []
        pass

    def karifuru(self, minna):
        for m in minna:
            x = int(random.random()*len(self.suretu))
            index = self.suretu.pop(x)
            self.kariList.append([index, m])
        pass

    def honfuri(self):
        for i in range(self.ninsu):
            for j in range(self.ninsu):
                if i == self.kariList[j][0]:
                    self.honList.append([i,self.kariList[j][1]])


        return self.honList

    
#クラス　対戦
class Taisen:
    def __init__(self, machi):
        self.retu = len(machi) /2
        self.tList = []
        self.errFlag = True

        for i in machi:
            self.tList.append([ i.No, i.namae])

    #勝利数入力時のエラーチェック
    def ErrorCheck(self,kekka):
        for i in kekka:
            if i == [""] or not i:
                print("勝ち数を入力してください。")
                return self.errFlag

        msg = ""
        if not kekka == "":
            self.errFlag = False
        k = kekka
#        print(f"{len(k)=} {k=} {self.retu=}")
        if not len(k) == self.retu -1 and k:
            msg = "勝負の数の数字が少ないか多いです。"
            self.errFlag = True
        for i in k:
            if not len(i) == 2:
                msg = "スペースを入力していないか数字が不足してます。"
                self.errFlag = True
        
        for i in k:
            for j in i:
                if j.isdecimal():
                    if not int(j) < 3:
                        msg = "数字が大きいです。"
                        self.errFlag = True
                else:
                    msg = "数字以外が入力されてます。"
                    self.errFlag = True
        for i in k:
            if i[0].isdecimal() and i[1].isdecimal():
                if int(i[0])+int(i[1]) > 3:
                    msg = "勝利数がおかしいです。"
                    self.errFlag = True
            else:
                    msg = "数字以外が入力されてます。"
                    self.errFlag = True                
        if msg:
            msg += "\n\nエラーです。やり直して下さい。"
        if self.errFlag:
            print(f"{msg}")
        return self.errFlag

    def AiteKettei(self,pData):
        tekito = 0


    def Hyouji(self):
        
        for i in range(0,len(self.tList), 2):
            print(f"{self.tList[i][1]} VS {self.tList[i+1][1]}")

#クラス表示「勝ち」「負け」
class HyoujiKatiMake:
    def __init__(self):
        self.tatakaiSu = 0
        pass
    def kekkaIre(self, kekka):
        hidari = 0
        migi = 0

        if kekka[0] == "2":
            hidari = 3
            migi = 0
        elif kekka[1] == "2":
            hidari = 0
            migi = 3
        elif kekka[0] == "1":
            if kekka[1] == "1":
                hidari = 1
                migi = 1
            elif kekka[1] == "0":
                hidari = 3
                migi = 0
        elif kekka[1] == "1":
            if kekka[0] == 0:
                hidari = 0
                migi = 3

        return hidari,migi

    def hyouji(self, kekka):

        hidari = ""
        mannaka = " "
        migi = ""
        if kekka[0] == "2":
            hidari = "勝ち"
        elif kekka[0] == "1":
            if kekka[1] == "0":
                hidari = "勝ち"
            elif kekka[1] == "1":
                mannaka = "引き分け"
            elif kekka[1] == "2":
                hidari = "負け"
        elif kekka[0] == "0":
            if kekka[1] == "0":
                mannaka = "引き分け"
            elif kekka[1] == "1" or kekka[1] == "2":
                hidari = "負け"

        if hidari == "勝ち":
            migi = "負け"
        elif hidari == "負け":
            migi = "勝ち"

        #表示 拡張あり
        if mannaka == "引き分け":
            print(f"{self.tatakaiSu +1}席目：{mannaka}")
        else:
            print(f"{self.tatakaiSu +1}席目：{hidari} {mannaka} {migi}")
        self.tatakaiSu += 1
    
class TaisenKime:
    def __init__(self, pdata):
        #勝ち点で層を作る
        self.sou = []
        self.souKata = []
        self.souKazu = 0

        self.souSyurui = []

        for i in playerdata:
            if not i.Mpoint in self.souSyurui:
                self.souSyurui.append(i.Mpoint)
            
        self.souSyurui.sort(reverse=True)
        self.souKazu = len(self.souSyurui)

        for i in self.souSyurui:
            kazuSyurui = 0
            for j in playerdata:
                if j.Mpoint == i:
                    self.sou.append(j.No)
                    kazuSyurui = kazuSyurui + 1
            self.souKata.append(kazuSyurui)

        pass

#======================================================
#メイン
#======================================================
#プレイヤーデータ作成
#対戦決め
#対戦表示


#プレイヤーリスト
playerdata = []

#乱数
No_warifuri = RandmInit(len(minna))


#No振り分け
No_warifuri.karifuru(minna)
kari = No_warifuri.honfuri()

for i in range(len(kari)):
    playerdata.append(PlayerData(kari[i][1],i))

if len(minna) % 2:
    playerdata.append(PlayerData("byb ",len(minna)))

#最初の対戦相手決定
for i in range(len(playerdata)):
    if i % 2:
        playerdata[i].TaisenNyuryoku(playerdata[i-1].namae,playerdata[i-1].No)
    else:
        playerdata[i].TaisenNyuryoku(playerdata[i+1].namae,playerdata[i+1].No)


#プレイヤーデータ表示１回目
for i in range(len(playerdata)):
    playerdata[i].Hyouji()


tisen1 = Taisen(playerdata)
tisen1.Hyouji()

katimake = HyoujiKatiMake()
syoubuSu = int(len(minna)/2)
kekka = ""

while tisen1.ErrorCheck(kekka):

    print("勝った数の数字を左と右の方を連続で入力して下さい。\n席ごとにスペースで区切って下さい\n（2か1か0）")
    kekka = input("入力:").split(" ")




ireruMp = []
for i in range(syoubuSu):
    katimake.hyouji(kekka[i])
    no = tisen1.tList[i][0]
    ire = katimake.kekkaIre(kekka[i])
    ireruMp.append(ire[0])
    ireruMp.append(ire[1])


#マッチポイントとマッチポイントパーとオポメントポイントパーをプレイヤーデータに入れる。アプデ：クラス化する。
ind = 0
for i in tisen1.tList:

    for j in range(len(ireruMp)):
        
        if playerdata[j].No == i[0]:
            playerdata[j].Mpoint = ireruMp[ind]
            playerdata[j].KaisuTaisen = playerdata[j].KaisuTaisen +1
            mpper = playerdata[j].Mpoint / ( playerdata[j].KaisuTaisen * 3)

            if mpper >= 0.333:
                playerdata[j].MpointPar = "{:.3f}".format(mpper)
            else:
                playerdata[j].MpointPar = 0.333
            opp = 0.000
            for k in playerdata[j].TaisenAiteNo:
                opp = opp + playerdata[k].Mpoint

            playerdata[j].OpMpPar = opp
    ind = ind + 1

print("")
for i in range(len(playerdata)):
    playerdata[i].Hyouji()

taiKime = TaisenKime(playerdata)
print(taiKime.sou)
print(taiKime.souKata)

#課題：順位の入れ替わりを表示。マッチポイントの入り方を表示

