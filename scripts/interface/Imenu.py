class IMainMenu:
    """
    class for the menu screen
    """
    def __init__(self):
        pass


    def change_state(self):
        """changing screens(do not forget to change state to none after updating manager_scene)"""
        raise NotImplementedError
    
    
    def update(self):
        """placing all objects on the screen(place on infinity loop for changing every frame)"""
        raise NotImplementedError
