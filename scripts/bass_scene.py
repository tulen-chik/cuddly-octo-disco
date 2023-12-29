class Scene:
    def __init__(self, display):
        self.state = None
        self.display = display
    
    def change_state(self, protocol):
        """method for changing current display of the game"""
        raise NotImplementedError('method isn\'t initialized')
    
    def update(self):
        """method for updating current display of the game"""
        raise NotImplementedError('method isn\'t initialized')
