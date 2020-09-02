import wx # type: ignore

from typing import List, Callable, Optional

class OOPDrawIntermediate(wx.Frame):
    """ OOPDrawIntermediate is a subclass of wx.Frame which contains all the wx.Windows (labels, comboboxes and
    panel on which graphic elements are drawn. It's used as a stepping stone to the ful OOPDraw package """

    def __init__(self):
        def AddChoice(name: str, label: str, y: int, options: List[str], handler: Callable):
            vBox.AddSpacer(10)

            hBox = wx.BoxSizer(wx.HORIZONTAL)
            hBox.AddSpacer(10)
            hBox.Add(wx.StaticText(panel, wx.ID_ANY, label))
            vBox.Add(hBox)

            hBox = wx.BoxSizer(wx.HORIZONTAL)
            cb = wx.ComboBox(panel, wx.ID_ANY, options[0], choices=options, style=wx.CB_READONLY, name=name)
            cb.Bind(wx.EVT_COMBOBOX, handler, cb)

            hBox.AddSpacer(10)
            hBox.Add(cb)
            hBox.AddSpacer(10)

            vBox.Add(hBox)

        def AddButton(name: str, label: str, handler: Callable):
            vBox.AddSpacer(10)

            hBox = wx.BoxSizer(wx.HORIZONTAL)
            b = wx.Button(panel, wx.ID_ANY, label=label, name=name)
            hBox.Add(b)
            b.Bind(wx.EVT_BUTTON, handler, b)
            hBox.AddSpacer(10)
            
            vBox.Add(hBox)
           
        super().__init__(None, wx.ID_ANY, 'OOPDraw in Python', size=(800, 600))
        self.Size = (0, 0, 800, 600)

        # panel contains all the controls (label + combobox for each option)
        panel = wx.Panel(self, wx.ID_ANY)
        # vBox is responsible for sizing all the controls and placing them within panel
        vBox = wx.BoxSizer(wx.VERTICAL)
        panel.Sizer = vBox

        # Code for user controls will go here

        # hBox is responsible for sizing the panel for controls and the panel for drawing on (canvas)
        hBox = wx.BoxSizer(wx.HORIZONTAL)
        self.Sizer = hBox
        hBox.Add(panel, 0, wx.EXPAND)
        hBox.AddSpacer(10)
        self.Canvas = wx.Panel(self, wx.ID_ANY, style=wx.BORDER_SIMPLE, name="Canvas")
        hBox.Add(self.Canvas, 1, wx.EXPAND)

        self.Canvas.Bind(wx.EVT_PAINT, self.OnPaint)


class OOPDraw(OOPDrawIntermediate):
    def __init__(self):
        super().__init__()
        self.CurrentBrush = wx.Brush(wx.BLACK, style=wx.BRUSHSTYLE_TRANSPARENT)
        self.Canvas.SetDoubleBuffered(True) 
        self.CurrentPen = wx.Pen(wx.GREEN, 4)   
 
        # Code for OOPDraw functionality goes here

        self.Canvas.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
        self.Canvas.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
        self.Canvas.Bind(wx.EVT_MOTION, self.OnMouseMove)

        self.dragging = False
        self.startOfDrag = wx.Point()
        self.lastMousePosition = wx.Point()

    def OnPaint(self: wx.Frame, e: wx.Event):
        dc = wx.BufferedPaintDC(self.Canvas)
        dc.Clear()
        dc.Brush = self.CurrentBrush

        dc.Pen = self.CurrentPen
        dc.DrawLine(self.startOfDrag, self.lastMousePosition)
    
    def OnMouseDown(self: wx.Window, e: wx.MouseEvent):
        self.dragging = True
        self.startOfDrag = self.lastMousePosition = e.GetPosition()
        e.Skip()

    def OnMouseUp(self: wx.Window, e: wx.MouseEvent):
        self.dragging = False

    def OnMouseMove(self: wx.Window, e: wx.MouseEvent):
        if self.dragging:
            self.lastMousePosition = e.GetPosition()
            self.Refresh()


if __name__ == '__main__':
    app = wx.App()

    frame = OOPDraw()
    frame.Show()

    app.MainLoop()

