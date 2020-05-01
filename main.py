import ijson
import json
import pprint
import wx

with open('AllCards.json', 'r', encoding="utf-8") as f:
    objects = ijson.items(f, "Atraxa, Praetors' Voice")
    columns = list(objects)

    if len(columns) > 0:
        print(columns[0]['manaCost'])

app = wx.App()
frame = wx.Frame(None, title="Magic Card Finder")
#panel = wx.Panel(frame)
sizer = wx.GridSizer(0, 3, 10, 10)
staticText = wx.StaticText(frame, -1, label="Card finder",
                           style=wx.ALIGN_CENTRE_HORIZONTAL)
moreText = wx.StaticText(frame, -1, label="second item")
another = wx.StaticText(frame, -1, label="third item")

sizer.Add(staticText)
sizer.Add(moreText)
sizer.Add(another)
frame.SetSizer(sizer)

font = staticText.GetFont()
font.PointSize += 10
staticText.SetFont(font)
moreText.SetFont(font)
another.SetFont(font)
frame.Show()

app.MainLoop()
