import json
import sys
from .DevelopmentInstance import *
class ModuleImplemetation:
    def __init__(self) -> None:
        pass
    
    def FindClassObject(self):
        with open("filestoragemodule/storage.json" , "r") as headerfile:
            listModules = json.load(headerfile)['storageclasses']
            getModuleclass = listModules[self.module]
            return get_class(getModuleclass)
    
def get_class(class_name):
    return getattr(sys.modules[__name__], class_name)