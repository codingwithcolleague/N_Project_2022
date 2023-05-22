import abc

class StorageIntance(abc.ABC):
    
    def __init__(self) -> None:
        return None
    
    @abc.abstractmethod
    def get(self):
        raise NotImplementedError
    
    @abc.abstractmethod
    def create(self):
        raise NotImplementedError