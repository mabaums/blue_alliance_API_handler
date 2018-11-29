import wx
import tbapy
tba = tbapy.TBA("ydQbaifEuIbNjHS2cKFNXGfVDGrMsjwSOyqws9InphNYaQfyh6D11NHnyEuPWglc")

class testFrame(wx.Frame):

    def __init__(self, *args, **kw):
        super(testFrame, self).__init__(*args, **kw)
        self.events = tba.team_events(5829, "2018", True, False)
        panel_one = wx.Panel(self)

        title = wx.StaticText(panel_one, label="Test App Title", pos=(600,15))
        font_one = title.GetFont()
        font_one.PointSize += 10
        font_one = font_one.Bold()
        title.SetFont(font_one)

        self.makeMenuBar()

        self.CreateStatusBar()
        self.SetStatusText("Welcome to Scouting App V1")

    def makeMenuBar(self):
        fileMenu = wx.Menu()
        team_city_item = fileMenu.Append(-1, "Team City...\tCtrl-T", "Help string shown in menu for this item")
        team_events_item = fileMenu.Append(0, "Team events...\tCtrl-E", "Help")
        alliance_info_item = fileMenu.Append(1, "Alliance Info...\tCtrl-A", "Help")
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&Get Info")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.get_team_city, team_city_item)
        self.Bind(wx.EVT_MENU, self.team_events, team_events_item)
        self.Bind(wx.EVT_MENU, self.get_alliance_event_data, alliance_info_item)

    def get_team_city(self, event):
        box = wx.TextEntryDialog(None, "Which team would you like to check?", "Team City Checker", "5829")
        if box.ShowModal() == wx.ID_OK:
            team = box.GetValue()
            team = int(team)
            team = tba.team(team)
            wx.MessageBox("The team is from %s" %(team.city))
            alliance_data = tba.event_alliances("2018onwat")

    def team_events(self, event):
        box = wx.TextEntryDialog(None, "Which team would you like to check?", "Team Event Checker", "5829")
        if box.ShowModal() == wx.ID_OK:
            team = int(box.GetValue())
            team_events = tba.team.team_events(team)
            wx.MessageBox("%s"%team_events)
    def get_alliance_event_data(self, event):
        box = wx.TextEntryDialog(None, "Which event?", "Which event?", "2018onwat")
        if box.ShowModal() == wx.ID_OK:
            event = box.GetValue()
            alliance_data = tba.event_alliances(event)
            box_two = wx.TextEntryDialog(None, "Which Alliance?", "Which Alliance?", "1")
            if box_two.ShowModal() == wx.ID_OK:
                alliance = int(box_two.GetValue()) - 1
                specific_alliance_data = alliance_data[alliance]
                print(specific_alliance_data)
                backup = specific_alliance_data["backup"]
                declines = specific_alliance_data["declines"]
                picks = specific_alliance_data["picks"]
                losses = specific_alliance_data["status"]["record"]["losses"]
                ties = specific_alliance_data["status"]["record"]["ties"]
                wins = specific_alliance_data["status"]["record"]["wins"]

                wx.MessageBox("Alliance %s had backup bot %s and was led by %s. \nThey were declined by %s\nTheir "
                              "first pick was %s and second pick was %s\nThey had %s loss/losses)\nThey had %s tie("
                              "s)\nThey had %s win(s)"%(alliance+1, backup, picks[0], declines, picks[1], picks[2],
                                                        losses, ties, wins))
        elif box.ShowModal() == wx.ID_CANCEL:
            quit()
