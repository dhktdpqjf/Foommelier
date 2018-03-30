import wx
import csv
from filtering import Filtering as cf
from menuFilter import menufiltering as mf
from wx.lib.mixins.listctrl import CheckListCtrlMixin, ListCtrlAutoWidthMixin
import wx.lib.agw.hyperlink as hl
import health

class CheckListCtrl(wx.ListCtrl, CheckListCtrlMixin, ListCtrlAutoWidthMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        CheckListCtrlMixin.__init__(self)
        ListCtrlAutoWidthMixin.__init__(self)
class CheckListCtrl2(wx.ListCtrl, CheckListCtrlMixin, ListCtrlAutoWidthMixin, wx.lib.mixins.listctrl.TextEditMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        wx.lib.mixins.listctrl.TextEditMixin.__init__(self) ##얘가 있으면 이제 그냥 글씨부분 선택하면 편집할 수 있게 됨.
        CheckListCtrlMixin.__init__(self)
        ListCtrlAutoWidthMixin.__init__(self)
def loadUserList():
    f = open('user2.csv', 'r', encoding='EUC-KR')
    rdr = csv.reader(f)
    user_list={}

    for line in rdr:
        if line[0] != '재료':
            user_list[line[0]] = float(line[1])
            # user_list.append((line[0],line[1]))
    f.close()
    return user_list
def loadCsv(fileName = "return.csv"):
    f = open(fileName, 'r', encoding='EUC-KR')
    rdr = csv.reader(f)
    c = 0
    play = '연근조림'
    name_list = []
    mm_list = []
    sm_list = []

    for line in rdr:
        if line[0] != play:
            play = line[0]
            c += 1
            name_list.append(play)

    s = 0
    dict_list = {
        '연근조림': {
            '연근': 1,
            '간장': 1,
            '식초': 0.3,
            '양념': 0.3,
            '물엿': 0.3,
            '식용유': 0.3,
            '설탕': 0.3,
            '참기름': 0.3
        }}

    d_list = {}
    dd_list = []

    mi_list = []
    si_list = []

    ch = '연근조림'
    with open('ref_data.csv') as fr:
        reader = csv.DictReader(fr)

        for row in reader:
            #         print(row)
            if row['음식이름'] == ch:
                if row['주재료'] != '':
                    d_list.update({row['주재료']: 5.0})
                if row['부재료'] != '':
                    d_list.update({row['부재료']: 2.5})

            if row['음식이름'] != ch:
                dict_list[ch] = d_list
                s += 1
                d_list = {}
                ch = name_list[s]
                if row['주재료'] != '':
                    d_list.update({row['주재료']: 5.0})
                if row['부재료'] != '':
                    d_list.update({row['부재료']: 2.5})

            if s == 800:
                break

    return dict_list
def loadDict():
    f = open('return.csv', 'r', encoding='EUC-KR')
    rdr = csv.reader(f)
    c = 0
    play = '연근조림'
    name_list = []

    for line in rdr:
        if line[0] != play:
            play = line[0]
            c += 1
            name_list.append(play)

    s = 0
    dict_list = {
        '연근조림': {
            '연근': 1,
            '간장': 1,
            '식초': 0.3,
            '양념': 0.3,
            '물엿': 0.3,
            '식용유': 0.3,
            '설탕': 0.3,
            '참기름': 0.3
        }}

    d_list = {}

    ch = '연근조림'
    with open('return.csv') as fr:
        reader = csv.DictReader(fr)

        for row in reader:
            #         print(row)
            if row['음식이름'] == ch:
                if row['주재료'] != '':
                    d_list.update({row['주재료']: 5.0})
                if row['부재료'] != '':
                    d_list.update({row['부재료']: 2.5})

            if row['음식이름'] != ch:
                dict_list[ch] = d_list
                s += 1
                d_list = {}
                ch = name_list[s]
                if row['주재료'] != '':
                    d_list.update({row['주재료']: 5.0})
                if row['부재료'] != '':
                    d_list.update({row['부재료']: 2.5})

            if s == 800:
                break

        user_list = loadUserList()
        dict_list['사용자'] = user_list

    return dict_list
def findURL(name):
    f = open('urls_name_mat_re.csv', 'r', encoding='EUC-KR')
    rdr = csv.reader(f)

    for line in rdr:
        if line[1] == name:
            return line[0]
def saveAsCsv(namelist, datalist):
    with open('user2.csv', 'w', encoding='EUC-KR', newline='') as csvfile:
        fieldnames = ['재료', '중요도']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        count = -1
        for data in datalist:
            count += 1
            if data == 'O':
                writer.writerow({'재료': namelist[count], '중요도': 5})
            else:
                writer.writerow({'재료': namelist[count], '중요도': 2.5})

        print('새로운 url-이름-재료 테이블 생성!')

class MainFrame ( wx.Frame ):
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title="Be a great Cook!", pos = wx.DefaultPosition,
                            size = wx.Size( 500,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        #####복붙 mainGUI2
    def __del__( self ):
        pass

class panel_one ( wx.Panel ): ##얘는 메인 화면
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition,
                                             size = wx.Size( 500,550 ), style = wx.TAB_TRAVERSAL )

        self.vbox = wx.BoxSizer(wx.VERTICAL)  # 얘는 재료랑 이름 뜨는 부분
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.lowerPanel = wx.Panel(self)

        ## 재료랑 중요도 리스트박스 뜨는 부분
        self.list = CheckListCtrl(self)
        self.list.InsertColumn(0, '재료', width=200)
        self.list.InsertColumn(1, '중요도', width=100)

        user_list = loadUserList()
        name_list = list(user_list.keys())
        imp_list = list(user_list.values())
        n=-1
        for i in imp_list:
            n+=1
            if i == 5.0:  # 가중치가 5이면 (=주재료면) O라고 보이고 아니면 X라고 보이게 하려고.
                index = self.list.InsertItem(200, name_list[n])
                self.list.SetItem(index, 1, 'O')
                self.list.CheckItem(index, True)  ###주재료면 체크 표시된 채로 띄우기
            else:
                index = self.list.InsertItem(200, name_list[n])
                self.list.SetItem(index, 1, 'X')

        ##화면 하단 버튼 넣기
        self.backButton = wx.Button(self.lowerPanel, label="식단")  ##식단 메뉴로 감
        self.exitButton = wx.Button(self.lowerPanel, label="종료")
        self.updateButton = wx.Button(self.lowerPanel, label="수정")  ##패널 바꾸는 버튼이 됨
        self.searchButton = wx.Button(self.lowerPanel, label="검색")

        self.hbox.Add(self.backButton)
        self.hbox.Add(self.exitButton)
        self.hbox.Add(self.updateButton)
        self.hbox.Add(self.searchButton)

        self.backButton.Bind(wx.EVT_BUTTON, self.onBack)
        self.exitButton.Bind(wx.EVT_BUTTON, self.OnClose)
        self.searchButton.Bind(wx.EVT_BUTTON, self.OnSearch)
        self.updateButton.Bind(wx.EVT_BUTTON, self.changeIntroPanel)

        self.lowerPanel.SetSizer(self.hbox)

        ##배치하기
        vtBoxSizer = wx.BoxSizer(wx.VERTICAL)  # 수직
        vtBoxSizer.Add(self.list, 1, wx.EXPAND|wx.ALL, 5) ##upperPanel 이었음
        vtBoxSizer.Add((-1, 10))
        vtBoxSizer.Add(self.lowerPanel, 0, wx.ALL, 5)
        vtBoxSizer.Add((-1, 10))
        self.SetSizer(vtBoxSizer)
        self.Layout()


        # Connect Events
        # self.m_button2.Bind( wx.EVT_BUTTON, self.OnUpdate ) ##누르면 수정화면으로


    def __del__( self ):
        pass

    def onBack(self, event):
        event.Skip()

    ## 닫기버튼
    def OnClose(self, event):
            if wx.MessageBox("윈도우를 닫을까요?", "확인", wx.YES_NO) != wx.YES:
                event.Skip(False)
            else:
                self.parent.Destroy()

    ## '검색' 했을 때 새 창 띄우기
    def OnSearch(self, event):
        matchlist = cf.top_match(cf, loadDict() , '사용자')
        ch = 0
        gap = -20

        fr = wx.Frame(parent=None, title="음식 추천 순위", size=(320, 200))
        fr.pnl = wx.Panel(fr)

        for m in matchlist:
            gap += 20
            ch += 1
            hl.HyperLinkCtrl(fr.pnl, -1, m[1], pos=(30, 20 + gap), URL=findURL(m[1]))

        fr.Centre()
        fr.Show(True)

    def changeIntroPanel( self, event ):
        event.Skip()
        # self.panel.Refresh() #####이런 것도 있음!!!!!

class panel_two ( wx.Panel ): ##얘는 수정하는 화면
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,550 ), style = wx.TAB_TRAVERSAL )

        ## 재료랑 중요도 리스트 뜨는 부분
        self.list = CheckListCtrl2(self)
        self.list.InsertColumn(0, '재료', width=200)
        self.list.InsertColumn(1, '중요도', width=100)

        user_list = loadUserList()
        name_list = list(user_list.keys())
        imp_list = list(user_list.values())
        n = -1
        for i in imp_list:
            n += 1
            if i == 5.0:  # 가중치가 5이면 (=주재료면) O라고 보이고 아니면 X라고 보이게 하려고.
                index = self.list.InsertItem(200, name_list[n])
                self.list.SetItem(index, 1, 'O')
                self.list.CheckItem(index, True)  ###주재료면 체크 표시된 채로 띄우기
            else:
                index = self.list.InsertItem(200, name_list[n])
                self.list.SetItem(index, 1, 'X')

        ##버튼 부분
        self.vbox2 = wx.BoxSizer(wx.VERTICAL)  # 버튼 부분
        self.rightPanel = wx.Panel(self)

        self.new = wx.Button(self.rightPanel, label='New', size=(90, 30))
        self.dlt = wx.Button(self.rightPanel, label='Delete', size=(90, 30))
        self.sav = wx.Button(self.rightPanel, label='Save', size=(90, 30))
        self.goto = wx.Button(self.rightPanel, label = 'Main', size=(90, 30))

        self.new.Bind(wx.EVT_BUTTON, self.NewItem)
        self.dlt.Bind(wx.EVT_BUTTON, self.OnDelete)
        self.sav.Bind(wx.EVT_BUTTON, self.OnSave) #self.changeIntroPanel) ##self.OnSave)
        self.goto.Bind( wx.EVT_BUTTON, self.changeIntroPanel )


        self.vbox2.Add((-1, 20))
        self.vbox2.Add(self.new)
        self.vbox2.Add(self.dlt, 0, wx.TOP, 5)
        self.vbox2.Add(self.sav, 0, wx.TOP, 5)
        self.vbox2.Add(self.goto, 0, wx.TOP, 5)

        self.rightPanel.SetSizer(self.vbox2)

        hbox = wx.BoxSizer(wx.HORIZONTAL)  # 전체
        hbox.Add((10, -1))
        hbox.Add(self.list, 1, wx.EXPAND | wx.RIGHT, 5) ###leftpanel 없앰
        hbox.Add(self.rightPanel, 0, wx.EXPAND | wx.RIGHT, 5)
        hbox.Add((5, -1))

        self.SetSizer(hbox)
        self.Layout()

        self.Centre()
        self.Show(True)


    def NewItem(self, event):
        mat = wx.TextEntryDialog(self,'추가할 재료', '추가하기') #이름은 텍스트 대화창으로 받고
        if mat.ShowModal() == wx.ID_OK:
            priority = wx.MessageDialog(None, '최우선으로 검색할까요?', 'Question', wx.YES_NO) #가중치는 선택하기
            if priority.ShowModal() == wx.ID_YES:
                index = self.list.Append([mat.GetValue(),'O'])
                self.list.CheckItem(index, True)
            else:
                self.list.Append([mat.GetValue(), 'X'])
        priority.Destroy()

    ##선택한 애 삭제하는 거
    def OnDelete(self, event):
        sel = self.list.GetFirstSelected()
        self.list.DeleteItem(sel)

    #저장하는 거. 아직 못함...
    def OnSave(self, event):
        num = self.list.GetItemCount()
        nlist =[]
        plist=[]
        index = -1
        for i in range(num):
            nlist.append(self.list.GetItemText(i,0))
            if self.list.IsChecked(i):
                plist.append('O')
            else:
                plist.append('X')


        saving = wx.MessageDialog(self, '저장할까요?', 'Question', wx.YES_NO)
        if saving.ShowModal() != wx.ID_YES:
            return
        else:
            self.list.DeleteAllItems()
            ch = -1
            for n in nlist:
                ch+=1
                index = self.list.InsertItem(200, n)
                if plist[ch] == 'O':  # 가중치가 5.0이면 (=주재료면) O라고 보이고 아니면 X라고 보이게 하려고.
                    self.list.SetItem(index, 1, 'O')
                    self.list.CheckItem(index, True)  ###주재료면 체크 표시된 채로 띄우기
                else:
                    self.list.SetItem(index, 1, 'X')
            saving.Destroy()

            saveAsCsv(nlist,plist)
            print('완료')
            print(self.list.GetItemCount())


    def __del__( self ):
        pass

    def changeIntroPanel( self, event ): ##메인 화면으로 바뀌면서 수정된 리스트를 전달해야 함.
        event.Skip()

class panel_meal(wx.Panel):  ##얘는 수정하는 화면
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 550),
                          style=wx.TAB_TRAVERSAL)

        ###############복붙
        self.vbox2 = wx.BoxSizer(wx.VERTICAL)  # 버튼 부분
        self.leftPanel = wx.Panel(self)

        self.bt1 = wx.Button(self.leftPanel, -1, label='오늘의 식단')
        self.bt4 = wx.Button(self.leftPanel, -1, label='내 정보')
        self.bt5 = wx.Button(self.leftPanel, -1, label='홈')

        ##버튼 별 함수 만들기
        self.bt1.Bind(wx.EVT_BUTTON, self.showMeal)
        self.bt4.Bind(wx.EVT_BUTTON, self.OnSetting)
        self.bt5.Bind(wx.EVT_BUTTON, self.changeIntroPanel)

        self.vbox2.Add(self.bt1, 1)
        self.vbox2.Add(self.bt4, 1)
        self.vbox2.Add(self.bt5, 1)

        self.leftPanel.SetSizer(self.vbox2)
        # self.rightPanel = wx.Panel(self)

        hbox = wx.BoxSizer(wx.HORIZONTAL)  # 전체
        hbox.Add((10, -1))
        hbox.Add(self.leftPanel, 0, wx.EXPAND | wx.RIGHT, 5)
        # hbox.Add(self.rightPanel, 1, wx.EXPAND | wx.RIGHT, 5)  ##이제 여기다가  버튼 누른 결과를 출력해야 함
        hbox.Add((5, -1))

        self.SetSizer(hbox)
        self.Layout()

        self.Centre()
        self.Show(True)

    def showMeal(self, event):
        # rlist = ['임신부','수험생'] ####rlist 는 설정값에서 받아와야 함
        # getList = mf.getData(mf,rlist)
        # menuList = list(getList.keys())
        # ch = 0
        # gap = -20
        # fr = wx.Frame(parent=None, title="오늘의 식단", size=(320, 200))
        # fr.pnl = wx.Panel(fr)
        #
        # for m in menuList:
        #     gap += 20
        #     ch += 1
        #     hl.HyperLinkCtrl(fr.pnl, -1, m, pos=(30, 20 + gap), URL=findURL(m))
        # fr.Centre()
        # fr.Show(True)
        rlist = ['감기','금연']  ####rlist 는 설정값에서 받아와야 함
        getList = mf.getData(mf, rlist)
        menuList = list(getList.keys())
        ch = 0
        gap = -20

        fr = wx.Frame(parent=None, title="오늘의 식단", size=(320, 200))
        fr.pnl = wx.Panel(fr)

        # font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        # heading = wx.StaticText(self, label='오늘의 식단', pos=(130, 15))
        # heading.SetFont(font)

        # pnl = wx.Panel(self)
        for m in menuList:
            gap += 20
            ch += 1
            hl.HyperLinkCtrl(fr.pnl, -1, m, pos=(60, 20 + gap), URL=findURL(m))
            # hl.HyperLinkCtrl(self, -1, m, pos=(200, 80 + gap), URL=findURL(m))

        fr.Centre()
        fr.Show(True)

    def OnSetting(self, event):

        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        heading = wx.StaticText(self, label='나태호 님 건강 정보', pos=(130, 15))
        heading.SetFont(font)

        hlist = [174, 70, 27, 1, 2]
        user = health.healthMain(hlist[0],hlist[1],hlist[2],hlist[3],hlist[4])

        gap = -20
        for u in user:
            gap +=20
            wx.StaticText(self, label=u, pos=(150, 80+gap))
            wx.StaticText(self, label=str(user[u]), pos=(250, 80+gap))

def changeIntroPanel( self, event ): ##메인 화면으로 바뀌면서 수정된 리스트를 전달해야 함.
        event.Skip()