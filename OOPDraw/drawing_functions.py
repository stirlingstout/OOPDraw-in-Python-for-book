import wx # type: ignore

from shape import Shape

def DrawClosedArc(dc: wx.DC, shape: Shape):
    (x, y, w, h) = shape.EnclosingRectangle()
    dc.Pen = shape.Pen()
    dc.DrawEllipticArc(x, y, w, h, 0, 360)
