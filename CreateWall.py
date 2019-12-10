"""
CreateWall
"""
__author__ = 'Danny Bentley - danny_bentley@hotmail.com'
__twitter__ = '@danbentley'
__Website__ = 'http://dannybentley.tech/'
__version__ = '1.0.0'

"""
Sample on how to create a Wall.
Use this sample along with the Video on Youtube.
"""
import clr
#Import module for Revit 
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
#import module for the Document and transactions
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
#import Revit API 
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
#get the current document in Revit.
doc = DocumentManager.Instance.CurrentDBDocument

#Dynamo input 
baseLevel = UnwrapElement(IN[0])
topLevel = UnwrapElement(IN[1])
wallType = UnwrapElement(IN[2])
#create point for line 
pt1 = XYZ(0, 0, 0)
pt2 = XYZ(10, 0, 0)
#use safe transaction with Revit 
TransactionManager.Instance.EnsureInTransaction(doc)
#create line
line = Line.CreateBound(pt1, pt2)
#create wall using Revit API
wall = Wall.Create(doc, line, baseLevel.Id, False)
#Set the wall type to Dynamo input
wall.WallType = wallType
#Get the top constarint parameter using built in parameter
#Revit Document shows it as WALL_HEIGHT_TYPE
topConstraint = wall.get_Parameter(BuiltInParameter.WALL_HEIGHT_TYPE)
#Set the top constraint 
topConstraint.Set(topLevel.Id)
#Finish Transaction with task done
TransactionManager.Instance.TransactionTaskDone()

OUT = wall