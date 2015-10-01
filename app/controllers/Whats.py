
from system.core.controller import *

class Whats(Controller):
    def __init__(self, action):
        super(Whats, self).__init__(action)
     
    def index(self):
      
        return self.load_view('index.html')
