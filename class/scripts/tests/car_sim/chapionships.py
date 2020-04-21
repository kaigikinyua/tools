from threading import *
from random import randrange

from database import *

class Drivers:
	def settings(self):
		d=DB()
		drivers=d.get_all_Drivers()
		for driver in drivers:
			print(driver)
			print(self.prob_win(driver))
	#add vehicle capability
	def prob_win(self,driver):
		rand_constant=randrange(10)
		prob=(driver[2]*rand_constant)/driver[3]
		return prob

class Race:
	def load_race(self):
		pass
	def race(self):
		pass

class Championship:
	def championship(self):
		pass
	def winner(self):
		pass
	def sort_positions(self):
		pass	

d=Drivers()
d.settings()