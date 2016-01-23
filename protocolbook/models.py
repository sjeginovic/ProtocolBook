from django.db import models

# Create your models here.

class Company(models.Model):
	companyName = models.CharField(max_length=50)
	companyDesc = models.CharField(max_length=300)
	def __str__(self):
		return self.companyName

class Protocol(models.Model):
	protocolNo = models.CharField(max_length=15)
	documentNo = models.CharField(max_length=30)
	documentDesc = models.CharField(max_length=300)
	documentDate = models.DateTimeField('document date')
	documentValue = models.DecimalField(max_digits=10, decimal_places=2)
	documentFrom = models.ForeignKey(Company, related_name='comanyFrom', on_delete=models.CASCADE)
	documentTo = models.ForeignKey(Company, related_name='comanyTo', on_delete=models.CASCADE) 
	def __str__(self):
		return self.protocolNo    