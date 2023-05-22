import base64
from filestoragemodule.filestorageservice import FileStorageService

class FileStorageOperation:
    
    def __init__(self) -> None:
        pass
    
    def uploadfile(self, file, modulename):
        try:
            file_encode = base64.b64decode(file.read())
            filename = file.name
            contentType = file.content_type
            file_details = { "file":file_encode, "filename" : filename,"contentType" : contentType}
            fileobj = FileStorageService().storefile(file_details, modulename)
        except:
            pass