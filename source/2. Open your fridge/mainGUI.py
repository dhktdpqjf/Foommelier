import wx
import gui

class MainApp(gui.MainFrame): ##얘는 전체 메인화면 하면 되겠음
    def __init__(self, parent):
        gui.MainFrame.__init__(self, parent)

        self.panelOne = Panel1(self)
        self.panelTwo = Panel2(self)
        self.panelTwo.Hide()

class Panel1(gui.panel_one):
    def __init__(self, parent):
        gui.panel_one.__init__(self, parent)
        self.parent = parent

    def changeIntroPanel(self, event ):
        if self.IsShown():
            self.parent.SetTitle("수정하기")
            self.Hide()
            self.parent.panelTwo.Show()


class Panel2(gui.panel_two):
    def __init__(self, parent):
        gui.panel_two.__init__(self, parent)
        self.parent = parent

    def changeIntroPanel(self, event):
        if self.IsShown():
            self.parent.SetTitle("냉장고를 부탁해")
            # self.parent.panelOne.Refresh(True) ###user2.csv 저장하고 써보기
            # self.parent.panelOne.Show()
            self.parent.panelOne = Panel1(self.parent) ##이렇게 해도 되는지 모르겠으나 됨!
            self.Hide()

def main():
    app = wx.App()
    window = MainApp(None)
    window.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()