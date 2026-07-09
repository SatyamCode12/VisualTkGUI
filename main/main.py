
import VTkGMainApp
import VTkGToolBox
import VTkGDesignerOrText
import VTkGPropertiesArea

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

def printHello():
    print("Hello World!")

def dragStart(event):
    widget = event.widget
    widget.StartX = event.x
    widget.StartY = event.y

def dragMotion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.StartX + event.x
    y = widget.winfo_y() - widget.StartY + event.y
    widget.place(x=x, y=y)

def SetWindowToCenter(mainWindow):
    screen_width = mainWindow.winfo_screenwidth()
    screen_height = mainWindow.winfo_screenheight()
    global windowOffsetX, windowOffsetY
    windowOffsetX = (int)(screen_width/2) - (int)(windowWidth/2)
    windowOffsetY = (int)(screen_height/2) - (int)(windowHeight/2)
    
windowHeight = 900
windowWidth = 1600
windowOffsetX = 0
windowOffsetY = 0
windowOpacity = 1 # 0 <= windowOpacity <= 1
isHeightResizable = False
isWidthResizable = False
IsAlwaysOnTop = 0 # 0 = No, 1 = Yes
iconPath = ""
limitMinimumSize = False
minimumHeight = 100
minimumWidth = 100
limitMaximumSize = False
maximumHeight = 800
maximumWidth = 1000

if __name__ == "__main__":
    app = VTkGMainApp.VTkGMainApp()
    tool_box = VTkGToolBox.VTkGToolBox(app)
    designer_or_text = VTkGDesignerOrText.VTkGDesignerOrText(app)
    properties = VTkGPropertiesArea.VTkGPropertiesArea(app)
    app.mainloop()

# toolBox = ttk.Frame(mainWindow, height=900, width=300)
# toolBox['borderwidth'] = 5
# toolBox['relief'] = 'groove'
# toolBox.grid(row=0, column=0, sticky="nw")


# designOrTextArea = ttk.Frame(mainWindow, height=900, width=1000)
# designOrTextArea['borderwidth'] = 5
# designOrTextArea['relief'] = 'groove'
# designOrTextArea.grid(row=0, column=1, sticky="ns")


# properties = ttk.Frame(mainWindow, height=900, width=300)
# properties['borderwidth'] = 5
# properties['relief'] = 'groove'
# properties.grid(row=0, column=2, sticky="ne")