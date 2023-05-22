from django.db import models

# Create your models here.

class CMasterData(models.Model):
    # user = models.ForeignKey(Master, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    json_dict = models.JSONField(default=dict)
    json_dict = models.JSONField(default=list)
    status = (('draft','Draft'),('submited','Submitted'))
    c_status = models.CharField(choices=status, default='draft')
    craeted_date = models.DateTimeField(auto_now_add=True, max_length=100)
    created_by = models.CharField(default='admin')
    
    class Meta:
        db_table = 'tbl_cmasterdata'
        
    def __str__(self) -> str:
        return self.name
    
    
    

# Not create migrate
class MasterData(models.Model):
    # user = models.ForeignKey(Master, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    json_dict = models.JSONField(default=dict)
    json_dict = models.JSONField(default=list)
    status = (('draft','Draft'),('submited','Submitted'))
    c_status = models.CharField(choices=status, default='draft')
    craeted_date = models.DateTimeField(auto_now_add=True, max_length=100)
    created_by = models.CharField(default='admin')
    
    class Meta:
        db_table = 'tbl_cmasterdata'
        manage = False
        
    def __str__(self) -> str:
        return self.name