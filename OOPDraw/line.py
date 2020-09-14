import wx # type: ignore

from shape import Shape

class Line(Shape):
    """I represent a line in the OOPDraw application, holding
the (x, y) coordinates of my start and end points, and the pen
that I am to be drawn in
"""

    def Draw(self, dc: wx.DC):
        dc.SetPen(self.Pen())
        dc.DrawLine(self.X1(), self.Y1(), self.X2(), self.Y2())
 

 