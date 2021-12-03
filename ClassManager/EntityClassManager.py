from ClassManager.ClassManager import ClassManager
from ClassManager import consts
from Entity.Entity import Entity

class EntityClassManager(ClassManager): # Class to load Entities from the Entitties dir and get them from name 
    def __init__(self):
        ClassManager.__init__(self)
        self.baseClass = Entity
        self.GetModulesFilename(consts.ENTITIES_PATH) 
        # self.GetModulesFilename(consts.CUSTOM_ENTITIES_PATH) # TODO Decide if I'll use customs