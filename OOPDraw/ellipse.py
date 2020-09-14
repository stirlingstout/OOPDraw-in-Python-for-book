import wx # type: ignore

from shape import Shape
from drawing_functions import DrawClosedArc


class Ellipse(Shape):
    """I represent an ellipse in the OOPDraw system"""

    def Draw(self, dc: wx.DC):
        DrawClosedArc(dc, self)
