from filestoragemodule.findimplemetation import ModuleImplemetation

class FileStorageService:
    
    def __init__(self) -> None:
        pass
    
    def storefile(self, file_details, modulename):
        try:
            getModule = ModuleImplemetation(modulename)
            selectedmodule = getModule.FindClassObject()
            fileobj = selectedmodule().create(file_details)
            return fileobj
        except Exception as error:
            pass
        
        