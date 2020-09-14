import wx # type: ignore

from shape import Shape


class Ellipse(Shape):
    """I represent an ellipse in the OOPDraw system"""

    def Draw(self, dc: wx.DC):
        x = min([self.X1(), self.X2()])
        y = min([self.Y1(), self.Y2()])

        w = max([self.X1(), self.X2()]) - x
        h = max([self.Y1(), self.Y2()]) - y

        dc.Pen = self.Pen()
        dc.DrawEllipticArc(x, y, w, h, 0, 360)
