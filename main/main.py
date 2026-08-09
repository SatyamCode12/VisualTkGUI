import VTkGMainApp
import VTkGToolBox
import VTkGDesignerOrText
import VTkGPropertiesArea
import VTkGStartScreen
import VTkGNewProject
import VTkGOpenProject

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1) # this line is to make app DPI aware

if __name__ == "__main__":
    app_start = VTkGStartScreen.VTkGStartScreen() # start screen of app
    app_start.mainloop() # starting start screen
    is_new_project = app_start.is_new_project
    is_open_project = app_start.is_open_project
    is_close_window = app_start.is_close_window
    if(is_new_project):
        new_project_window = VTkGNewProject.VTkGNewProject() # new project window
        new_project_window.mainloop() # starting new project window

    if(is_open_project):
        new_project_window = VTkGOpenProject.VTkGOpenProject() # open project window
        new_project_window.mainloop() # starting open project window

    #if(not is_close_window):
        #app = VTkGMainApp.VTkGMainApp() # initiating main app
        
        #properties = VTkGPropertiesArea.VTkGPropertiesArea(app) # initiating properties area
        #designer_or_text = VTkGDesignerOrText.VTkGDesignerOrText(app, properties) # initiating design/ text area
        #tool_box = VTkGToolBox.VTkGToolBox(app, designer_or_text.design_canvas) # initiating toolbox
        
        #app.mainloop() # starting main app

    
    