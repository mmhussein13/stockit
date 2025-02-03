from django.db import models
    
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    part_number = models.CharField(max_length=50, blank=False, null=True, unique=True)
    bin_location = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, unique=True)
    quantity = models.FloatField(default=0)
    cost_per_item = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    reorder_level = models.IntegerField(default=0, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
	    return self.name +'  **  ' + str(self.part_number) +' ** ' + str(self.quantity)+' ** ' + str(self.cost_per_item)
 