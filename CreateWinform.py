"""
CreateWinform
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__version__ = '1.0.0'

"""
Sample on how to create a Windows form.
Use this sample along with the Video on Youtube.
"""
import clr
# import windows form 
clr.AddReference("System.Windows.Forms")
#import system drawing 
clr.AddReference("System.Drawing")
# import system
import System

from System.Windows.Forms import *
from System.Drawing import *

# Create a Class Form
class CreateWindow(Form):
    def __init__(self): 
    
        # Create the Form
        self.Name = "Create Window"
        self.Text = "Create Window"
        self.Size = Size(500, 150)        
        self.CenterToScreen()

        self.values = []

        # Create Label for Sheet Name
        labelSheetName = Label(Text = "Sheet Name")
        labelSheetName.Parent = self
        labelSheetName.Location = Point(30, 20)

        # Create Label for Sheet Number
        labelSheetNumber = Label(Text = "Sheet Number")
        labelSheetNumber.Parent = self
        labelSheetNumber.Location = Point(30, 50)
        

        # Create TextBox for Sheet Name
        self.textboxSheetName = TextBox()
        self.textboxSheetName.Parent = self
        self.textboxSheetName.Text = "Sheet Name"
        self.textboxSheetName.Location = Point(150, 20)
        self.textboxSheetName.Width = 150
        
        # Create TextBox for Sheet Number
        self.textboxSheetNumber = TextBox()
        self.textboxSheetNumber.Parent = self
        self.textboxSheetNumber.Text = "Sheet Number"
        self.textboxSheetNumber.Location = Point(150, 50)
        self.textboxSheetNumber.Width = 150

        # Create Button = button
        button = Button()
        button.Parent = self
        button.Text = "Ok"
        button.Location = Point(400, 60)
        # Register event
        button.Click += self.ButtonClicked
        
    # Create button event
    def ButtonClicked(self, sender, args):
        if sender.Click:
            self.values.append(self.textboxSheetName.Text)
            self.values.append(self.textboxSheetNumber.Text)
            self.Close()            

if IN[0]:
	form = CreateWindow()
	Application.Run(form)
	
	OUT = form.values