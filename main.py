import tbapy
import wx
from mainGUIPage import testFrame

tba = tbapy.TBA("ydQbaifEuIbNjHS2cKFNXGfVDGrMsjwSOyqws9InphNYaQfyh6D11NHnyEuPWglc")

if __name__ == '__main__':
    app = wx.App()
    frm = testFrame(None, title="Mark's super scouting app!")
    frm.Show()
    app.MainLoop()