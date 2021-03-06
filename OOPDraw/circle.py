import wx # type: ignore

from shape import Shape
from drawing_functions import DrawClosedArc


class Circle(Shape):
    """I represent a circle in the OOPDraw system"""

    def __init__(self, p: wx.Pen, x1: int, y1: int, x2: int=None, y2: int=None):
        Shape.__init__(self, p, x1, y1, x2, y2)
        self.GrowTo(self.X2(), self.Y2())

    def Draw(self, dc: wx.DC):
        DrawClosedArc(dc, self)

    def GrowTo(self, x2: int, y2: int):
        diameter = max([x2 - self.X1(), y2 - self.Y1()])

        self.SetX2(self.X1() + diameter)
        self.SetY2(self.Y1() + diameter)