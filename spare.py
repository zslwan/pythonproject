#coding:utf8
#"""Spare.py is a starting point for a wxPython program.ok"""
import wxversion  
wxversion.select('2.8') 
import wx
"""
class Frame(wx.Frame):
    

    def __init__(self,image,parent=None,id=-1,pos=wx.DefaultPosition,title='Hello,wxPython!'):
        
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(),temp.GetHeight()
        wx.Frame.__init__(self,parent,id,title,pos,size)
        self.bmp = wx.StaticBitmap(parent=self,bitmap=temp)

        

class App(wx.App):
    

    def OnInit(self):
        image = wx.Image('C:/Users/Public/Pictures/Sample Pictures/菊花.jpg',wx.BITMAP_TYPE_JPEG)
        self.frame = Frame(image)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':
    app = App()
    app.MainLoop()
    
"""
class MyNewFrame(wx.Frame):
    pass
class PySimpleApp(wx.App):
    def __init__(self,redirect=False,filename=None,useBestVisual=False,clearSigInt=True):
        wx.App.__init__(self,redirect,filename,useBestVisual,clearSigInt)

    def OnInit(self):
        return True

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MyNewFrame(None)
    frame.Show(True)
    app.MainLoop()
