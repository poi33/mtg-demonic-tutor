import wx
from wx import StaticText, ListBox, TextCtrl
from search import SearchCard, GetCardByName


# TODO convert the input field into a dropdown suggestion box

class UI(wx.Frame):
    def __init__(self, *args, **kw):
        super(UI, self).__init__(*args, **kw)

        self.APPFONT = wx.Font(14, wx.FONTFAMILY_TELETYPE,
                               wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.APPFONTSMAL = wx.Font(10, wx.FONTFAMILY_TELETYPE,
                                   wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

        # panel = wx.Panel(frame)
        sizer = wx.GridSizer(1, 2, 0, 2)
        leftText = StaticText(self, -1, label="",
                              style=wx.ALIGN_CENTRE_HORIZONTAL)

        # cardInfo.SetBackgroundColour('black')
        # cardInfo.SetForegroundColour('white')

        #sizer.Add(leftText, 1, wx.EXPAND, 0)
        sizer.Add(self.CreateCenterSection(), 1, wx.EXPAND, 0)
        sizer.Add(self.CreateRightSection(), 2, wx.EXPAND, 0)

        self.SetSizer(sizer)

        self.CreateStatusBar()
        self.SetStatusText("Working on adding UI search")

        # Needs to be called when all components are added
        sizer.SetSizeHints(self)
        sizer.Fit(self)

    def CreateRightSection(self):
        rightPanel = wx.BoxSizer(orient=wx.VERTICAL)
        label = StaticText(
            self, -1, label="Press on a result to show the card", style=wx.ALIGN_CENTER_HORIZONTAL)
        label.SetBackgroundColour('white')
        label.SetFont(self.APPFONT)
        resultList = ListBox(self)

        # moreText.SetFont(font)
        resultList.SetFont(self.APPFONTSMAL)
        resultList.Bind(wx.EVT_LISTBOX, self.ResultClick)

        self.resultList = resultList

        rightPanel.Add(label, 1, wx.EXPAND, 0)
        rightPanel.Add(resultList, 20, wx.EXPAND, 0)
        rightPanel.SetSizeHints(self)
        return rightPanel

    def CreateCenterSection(self):
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        top = wx.BoxSizer(orient=wx.HORIZONTAL)

        submit_button = wx.Button(self, label="Search", size=wx.Size(10, 30))
        submit_button.Bind(wx.EVT_BUTTON, self.SearchFieldInput)

        searchField = TextCtrl(self, size=wx.Size(250, 30))
        #searchField.Bind(wx.EVT_KEY_UP, self.SearchFieldInput)
        searchField.SetFont(self.APPFONT)
        searchField.SetHint("Search for a card name here")
        searchField.SetFocus()

        cardInfo = StaticText(
            self, label="No card selected", size=wx.Size(250, 500))

        cardInfo.SetFont(self.APPFONT)
        cardInfo.SetBackgroundColour("white")

        self.cardInfo = cardInfo
        self.searchField = searchField

        top.Add(searchField, 2, wx.EXPAND, 1)
        top.Add(submit_button, 1, wx.EXPAND, 5)

        sizer.Add(top, 0, wx.EXPAND, 1)
        sizer.Add(cardInfo, 0, wx.EXPAND, 10)
        sizer.SetSizeHints(self)
        self.centerSizer = sizer

        return sizer

    def ResultClick(self, event):
        index = self.resultList.GetSelection()
        if index != wx.NOT_FOUND:
            cardName = self.resultList.GetString(index)
            cardData = GetCardByName(cardName)
            text = concatString(cardData)
            self.cardInfo.SetLabel(text)
            # self.cardInfo.Wrap(390)
            # self.centerSizer.SetSizeHints(self)


    def SearchFieldInput(self, event):
        #print (event)
        #print (event.GetKeyCode())
        event.Skip()
        result = SearchCard(
            self.searchField.GetLineText(0).replace("\n", ""))
        if isinstance(result, list):
            self.resultList.Clear()
            self.resultList.InsertItems(result, 0)
        else:
            # TODO show card in a meaningfull way
            pass

# class MyTextCompleter(wx.TextCompleterSimple):
#     def __init__(self, result):
#         wx.TextCompleterSimple.__init__(self)
#         print(result)
#         self._autoCompleteList = result

#     def GetCompletions(self, prefix):
#         return self._autoCompleteList


def concatString(text):
    cardText = ""
    for key in text:
        cardText += "\n"
        cardText += text[key]
    return cardText


def CreateUI():
    app = wx.App(useBestVisual=True)
    frame = UI(None, title="Demonic tutor, card finder")
    frame.Show()

    app.MainLoop()
