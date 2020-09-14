import wx # type: ignore

from shape import Shape


class Rectangle(Shape):
    """I represent a rectangle in the OOPDraw program. I have a
    Pen, and the start and end points of my top left and bottom 
    corners of the rectangle.
    My size can be changed using my GrowTo method"""

    def Draw(self, dc: wx.DC):
        dc.SetPen(self.Pen()) 
        x = min([self.X1(), self.X2()])
        y = min([self.Y1(), self.Y2()])
        w = max([self.X1(), self.X2()]) - x
        h = max([self.Y1(), self.Y2()]) - y
        dc.DrawRectangle(x, y, w, h)




