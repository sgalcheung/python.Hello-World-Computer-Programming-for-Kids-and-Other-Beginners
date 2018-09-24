from PythonCard import model

# old version
# class MainWindow(model.Background):

# 	def on_btnCtoF_mouseClick(self, event):
# 		cel = float(self.components.tfCel.text)
# 		fahr = cel * 9.0 / 5 + 32
# 		self.components.spinFahr.value = int(fahr)

# 	def on_btnFtoC_mouseClick(self, event):
# 		fahr = self.components.spinFahr.value
# 		cel = (fahr - 32) * 5.0 / 9
# 		celStr = '%.2f' % cel
# 		self.components.tfCel.text = celStr

# 	def on_menuConvertCtoF_select(self, event):
# 		cel = float(self.components.tfCel.text)
# 		fahr = cel * 9.0 / 5 + 32
# 		self.components.spinFahr.value = int(fahr)	

# 	def on_menuConvertFtoC_select(self, event):
# 		fahr = self.components.spinFahr.value
# 		cel = (fahr - 32) * 5.0 / 9
# 		celStr = '%.2f' % cel
# 		self.components.tfCel.text = celStr

# new version1
# def CtoF(self):
# 	cel = float(self.components.tfCel.text)
# 	fahr = cel * 9.0 / 5 + 32
# 	self.components.spinFahr.value = int(fahr)

# def FtoC(self):
# 	fahr = self.components.spinFahr.value
# 	cel = (fahr - 32) * 5.0 / 9
# 	celStr = '%.2f' % cel
# 	self.components.tfCel.text = celStr

class MainWindow(model.Background):

	# new version1
	# def on_btnCtoF_mouseClick(self, event):
	# 	CtoF(self)

	# def on_btnFtoC_mouseClick(self, event):
	# 	FtoC(self)

	# def on_menuConvertCtoF_select(self, event):
	# 	CtoF(self)	

	# def on_menuConvertFtoC_select(self, event):
	# 	FtoC(self)

	# new version2 application command
	def on_cmdCtoF_command(self, event):
		cel = float(self.components.tfCel.text)
		fahr = cel * 9.0 / 5 + 32
		self.components.spinFahr.value = int(fahr)

	def on_cmdFtoC_command(self, event):
		fahr = self.components.spinFahr.value
		cel = (fahr - 32) * 5.0 / 9
		celStr = '%.2f' % cel
		self.components.tfCel.text = celStr

app = model.Application(MainWindow)
app.MainLoop()