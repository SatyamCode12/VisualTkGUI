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

    project_name = ""
    project_path = ""
    if is_new_project:
        new_project_window = VTkGNewProject.VTkGNewProject() # new project window
        new_project_window.mainloop() # starting new project window
        project_name = new_project_window.NAME.get()
        project_path = new_project_window.PATHTOPROJECT.get()

    if is_open_project:
        open_project_window = VTkGOpenProject.VTkGOpenProject() # open project window
        open_project_window.mainloop() # starting open project window
        project_path = open_project_window.PATHTOPROJECT.get()

    #print(project_name)
    #print(project_path)

    if not is_close_window:
        app = VTkGMainApp.VTkGMainApp() # initiating main app
        
        properties = VTkGPropertiesArea.VTkGPropertiesArea(app) # initiating properties area
        designer_or_text = VTkGDesignerOrText.VTkGDesignerOrText(app, properties) # initiating design/ text area
        tool_box = VTkGToolBox.VTkGToolBox(app, designer_or_text.design_canvas) # initiating toolbox
        
        app.mainloop() # starting main app

    
    