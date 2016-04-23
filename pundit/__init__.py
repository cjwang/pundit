import itertools
import json

__version__ = "0.0.5"


'''
PunditBase Parent Class
Arguments : name
'''

class PunditBase():


	def __init__(self):
		self.mine = 'asd'
	

	'''
	Input preprocessor
	'''
	def input_preprocess(self, id, function):


		def lower(self, id):

			self.processed_input = []
			for x in self.input_set:
				if x['id'] == id:
					self.processed_input.append({'id': x['id'],'value': x['value'].lower(), 'type': x['type']})
				else:
					self.processed_input.append(x)
			return


		def upper(self, id):
			self.processed_input = []
			for x in self.input_set:
				if x['id'] == id:
					self.processed_input.append({{'id': x['id'],'value': x['value'].upper(), 'type': x['type']}})
				else:
					self.processed_input.append(x)
			return

		if function == 'lower':
			lower(self, id)
		elif function == 'upper':
			upper(self, id)
		else:
			pass


	def add_structure(self, arg1, arg2):
		self.structure.append({arg1:{}, arg2:{}})

	

'''
Condition group where conditions are set
'''

class ConditionGroup():

	def __init__(self, name):
		self.name = name
		self.condition = ["asd"]


	def add_condition(self, condition, optn, then, else_value):
		input_json = {'condition': condition, 'optn':optn, 'then': then, 'else_value':else_value}
		self.condition.append(input_json)


'''
Pundit class where structure is defined and inherited features of pundit base and condition groups
'''
class Pundit(PunditBase, ConditionGroup):

	def __init__(self, pundit, conditions):
		self.pundit = pundit
		self.conditions = conditions
		self.structure = []


	def evaluate(self, input):
		import ipdb;ipdb.set_trace()
		# input stuff
		input_json = {'id': id, 'value':value, 'type': type}
		self.input_set.append(input_json) 
		
		#check setup
		type_condition = [x for x in condition.condition if x['type'] == type]
		process_data = [x['value'] for x in self.processed_input if x['id'] == type]


		for x in type_condition:
			if x['condition'] == 'IN':
				return True if True in [x['value'] in pd for pd in process_data] else False
			else:
				pass




class MathRuler():
	"""Mathemaical rule operatons"""

	def __init__(self, for_this, then_that):
		self.condition = for_this;
		self.then = then_that


	def math(self, con):
		then_that = self.then
		for_this = self.condition
		exp_converter = then_that.replace(for_this, str(con))
		return eval(exp_converter)	



class ListRuler():
	
	def __init__(self, arg_list):
		self.list = arg_list
		self.reduced = []
		for li in self.list:
			if type(li) == list:
				for cc in list(itertools.chain(li)):
					self.reduced.append(cc)
			else:
				self.reduced.append(li)
		

	def fullfill(self, arg):
		return True if arg in self.reduced else False
		
		


