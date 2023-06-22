from krita import *

class MyExtension(Extension):

	def __init__(self, parent):
		super().__init__(parent)

	def setup(self):
		pass

	def createActions(self, window):
		action = window.createAction("FLTV_ID", "FLTV", "tools/scripts")
		action.triggered.connect(self.toggleVisibility)
		
	def toggleVisibility(self):
		doc =  Krita.instance().activeDocument()
		if doc is not None:
			nodesList = doc.topLevelNodes()
			length = len(nodesList)
			firstLayer = nodesList[length - 1]
			
			if firstLayer.visible() is True:
				firstLayer.setVisible(False)
			else:
				firstLayer.setVisible(True)
				
			doc.refreshProjection()

Krita.instance().addExtension(MyExtension(Krita.instance()))