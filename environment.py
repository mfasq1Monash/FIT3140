class Environment(dict):

    def __init__(self, parms=(), expressions=(), outer=None):
        """When evaluating, procedures will pass in their parameters"""
        self.update(zip(parms, expressions))
        self.outer = outer
        
    def find(self, variable):
        """Returns the lowest level Environment which has variable"""
        if variable in self:
            return self
        return self.outer.find(variable)
		
	def add_new(self, variable, value):
		"""Adds a new definition to the environment. If the variable is already present, raises a VariableAlreadyPresentError"""
		if variable in self:
			raise(VariableAlreadyPresentError)
		self[variable] = value