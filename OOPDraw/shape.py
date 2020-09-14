from abc import ABC, abstractmethod
import wx # type: ignore
from typing import Tuple

class Shape(ABC):
    """I define methods common to all the shapes that
    will be used in OOPDraw. I can't be instantiated
    myself since I'm abstract"""

    def __init__(self, p: wx.Pen, x1: int, y1: int, x2: int=None, y2: int=None):
        self.__Pen = p
        self.__X1 = x1
        self.__Y1 = y1
        self.__X2 = x2 if x2 else x1
        self.__Y2 = y2 if y2 else y1

    def Pen(self):
        return self.__Pen

    def X1(self):
        return self.__X1

    def Y1(self):
        return self.__Y1

    def X2(self):
        return self.__X2

    def Y2(self):
        return self.__Y2

    def SetX2(self, value: int):
        self.__X2 = value

    def SetY2(self, value: int):
        self.__Y2 = value
      
    @abstractmethod
    def Draw(self, dc: wx.DC):
        pass

    def GrowTo(self, x2: int, y2: int):
        self.SetX2(x2)
        self.SetY2(y2)

    def EnclosingRectangle(self) -> Tuple[int, int, int, int]:
        x = min([self.__X1, self.__X2])
        y = min([self.__Y1, self.__Y2])  
        w = max([self.__X1, self.__X2]) - x
        h = max([self.__Y1, self.__Y2]) - y
        return (x, y, w, h)
