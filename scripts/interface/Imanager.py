class IWindowManager:
    """
    class for collecting all scenes and changing them
    """
    def __init__(self):
        pass


    def is_running(self):
        """checking whether we need to close window(while WindowManager.is_running())"""
        raise NotImplementedError
    
    
    def update(self):
        """updating and changinf screens(place on infinity loop)"""
        raise NotImplementedError
