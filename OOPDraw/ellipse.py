import wx # type: ignore

from shape import Shape


class Ellipse(Shape):
    """I represent an ellipse in the OOPDraw system"""

    def Draw(self, dc: wx.DC):
        (x, y, w, h) = self.EnclosingRectangle()

        dc.Pen = self.Pen()
        dc.DrawEllipticArc(x, y, w, h, 0, 360)
