import wx # type: ignore

from typing import List, Callable, Optional

from line import Line
from rectangle import Rectangle
from ellipse import Ellipse
from circle import Circle


class OOPDrawIntermediate(wx.Frame):
    """ OOPDrawIntermediate is a subclass of wx.Frame which contains all the wx.Windows (labels, comboboxes and
    panel on which graphic elements are drawn. It's used as a stepping stone to the ful OOPDraw package """

    def __init__(self):
        def AddChoice(name: str, label: str, options: List[str], handler: Callable):
            vBox.AddSpacer(10)

            hBox = wx.BoxSizer(wx.HORIZONTAL)
            hBox.AddSpacer(10)
            hBox.Add(wx.StaticText(panel, wx.ID_ANY, label))
            vBox.Add(hBox)

            hBox = wx.BoxSizer(wx.HORIZONTAL)
            cb = wx.ComboBox(panel, wx.ID_ANY, "", choices=options, name=name)
            cb.Bind(wx.EVT_TEXT, handler, cb)
            cb.SetValue(options[0])

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

        # hBox is responsible for sizing the panel for controls and the panel for drawing on (canvas)
        hBox = wx.BoxSizer(wx.HORIZONTAL)
        self.Sizer = hBox
        hBox.Add(panel, 0, wx.EXPAND)
        hBox.AddSpacer(10)
        self.Canvas = wx.Panel(self, wx.ID_ANY, style=wx.BORDER_SIMPLE, name="Canvas")
        hBox.Add(self.Canvas, 1, wx.EXPAND)

        self.Canvas.Bind(wx.EVT_PAINT, self.OnPaint)

        self.CurrentBrush = wx.Brush(wx.BLACK, style=wx.BRUSHSTYLE_TRANSPARENT)
        self.Canvas.SetDoubleBuffered(True) 
        self.CurrentPen = wx.Pen(wx.BLACK)   

        # User's code for user controls will go here
        AddChoice("LineWidth", "Line width:", ["Thin", "Medium", "Thick"], self.OnLineWidthChanged)
        AddChoice("Colour", "Colour:", ["Red", "Green", "Blue"], self.OnColourChanged)
        AddChoice("Shape", "Shape:", ["Ellipse", "Circle", "Line", "Rectangle"], None)
        AddChoice("Action", "Action:", ["Draw", "Move"], None)


class OOPDraw(OOPDrawIntermediate):
    def __init__(self):
        super().__init__()
 
        # Code for OOPDraw functionality goes here

        self.Canvas.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
        self.Canvas.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
        self.Canvas.Bind(wx.EVT_MOTION, self.OnMouseMove)

        self.dragging = False
        self.startOfDrag = wx.Point()
        self.lastMousePosition = wx.Point()

        self.shapes = []

    def OnPaint(self: wx.Frame, e: wx.Event):
        dc = wx.BufferedPaintDC(self.Canvas)
        dc.Clear()
        dc.Brush = self.CurrentBrush

        dc.Pen = self.CurrentPen
        for shape in self.shapes:
            shape.Draw(dc)

    def AddShape(self, e: wx.MouseEvent):
        if self.FindWindow("Shape").Value == "Line":
            self.shapes.append(Line(self.CurrentPen, e.x, e.y))
        elif self.FindWindow("Shape").Value == "Rectangle":
            self.shapes.append(Rectangle(self.CurrentPen, e.x, e.y))
        elif self.FindWindow("Shape").Value == "Ellipse":
            self.shapes.append(Ellipse(self.CurrentPen, e.x, e.y))
        elif self.FindWindow("Shape").Value == "Circle":
            self.shapes.append(Circle(self.CurrentPen, e.x, e.y))

    def OnMouseDown(self: wx.Window, e: wx.MouseEvent):
        self.dragging = True
        self.startOfDrag = self.lastMousePosition = e.GetPosition()
        if self.FindWindow("Action").Value == "Draw":
            self.AddShape(e)
        e.Skip()

    def OnMouseUp(self: wx.Window, e: wx.MouseEvent):
        self.dragging = False
        self.lastMousePosition = wx.Point()
        self.Refresh()

    def OnMouseMove(self: wx.Window, e: wx.MouseEvent):
        if self.dragging:
            shape = self.shapes[-1]
            if self.FindWindow("Action").Value == "Move":
                if not self.lastMousePosition.IsFullySpecified():
                    self.lastMousePosition = e.GetPosition()
                shape.MoveBy(e.x - self.lastMousePosition.x, 
                             e.y - self.lastMousePosition.y)
            elif self.FindWindow("Action").Value == "Draw":
                shape.GrowTo(e.x, e.y)

            self.lastMousePosition = e.GetPosition()
            self.Refresh()

    def OnLineWidthChanged(self: wx.Frame, e: wx.Event):
        width = self.CurrentPen.Width
        if e.String == "Thin":
            width = 2
        elif e.String == "Medium":
            width = 4
        elif e.String == "Thick":
            width = 8
        self.CurrentPen = wx.Pen(self.CurrentPen.Colour, width)

    def OnColourChanged(self: wx.Frame, e: wx.Event):
        colour = self.CurrentPen.Colour
        if e.String == "Red":
            colour = wx.RED
        elif e.String == "Green":
            colour = wx.GREEN
        elif e.String == "Blue":
            colour = wx.BLUE
        self.CurrentPen = wx.Pen(colour, self.CurrentPen.Width)

if __name__ == '__main__':
    app = wx.App()

    frame = OOPDraw()
    frame.Show()

    app.MainLoop()


