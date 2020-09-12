from abc import ABC, abstractmethod
import wx # type: ignore

class Shape(ABC):
    """I define methods common to all the shapes that
    will be used in OOPDraw. I can't be instantiated
    myself since I'm abstract"""

    @abstractmethod
    def Draw(self, dc: wx.DC):
        pass

    @abstractmethod
    def GrowTo(self, x2: int, y2: int):
        pass
