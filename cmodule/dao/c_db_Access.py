from cmodule.models import CMasterData

class CDBAccess:
    
    def getdata(self):
        try:
            CMasterData.objects.filter()
        except Exception as error:
            pass