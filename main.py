import ijson
import json
import pprint
import wx

with open('AllCards.json', 'r', encoding="utf-8") as f:
    objects = ijson.items(f, "Atraxa, Praetors' Voice")
    columns = list(objects)

    if len(columns) > 0:
        print (columns[0]['manaCost'])
    
app = wx.App()
frm = wx.Frame(None, title="Magic Card Finder")
frm.show()

app.MainLoop()