import sys

class JsonSerializable(object):
    def toJson(self):
        return self.__dict__
    
    def __repr__(self):
        return self.toJson()

class ErrorResponse(JsonSerializable):
    def __init__(self, code, message):
        self.statuscode = code
        self.message = message
        
class StackTraceFormatter:
    def exception(self, e , log):
        error_str = "Error on line {}, type error".format(sys.exc_info()[-1].tb_lineno, type(e).__name__)
        log.info(error_str)
        return error_str