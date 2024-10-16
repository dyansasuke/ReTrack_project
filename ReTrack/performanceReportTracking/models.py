from django.db import models

#STAFF
class Staff(models.Model):
    staffID = models.CharField(max_length = 8, primary_key = True)
    staffName = models.TextField()
    staffPassword = models.TextField()
    staffEmail = models.TextField()
    
#ADMIN
class Admin(models.Model):
    adminID = models.CharField(max_length = 8, primary_key = True)
    adminName = models.TextField()
    adminPassword = models.TextField()
    adminEmail = models.TextField()
     
#ADSPLATFORM 
class customerPlatform(models.Model):
    ads = models.CharField(max_length = 100, primary_key = True)
    
#CATOGERY
class customerCatogery(models.Model):
    katogeri = models.CharField(max_length = 100, primary_key = True)
    
#PACKAGE
class customerPackage(models.Model):
    pakej = models.CharField(max_length = 100, primary_key = True)
    
#CUSTOMER   
class Customer(models.Model):
    companyName = models.CharField(max_length = 100, primary_key = True)
    customerEmail = models.TextField()
    adsPlatform = models.ForeignKey(customerPlatform, on_delete=models.CASCADE)
    package = models.ForeignKey(customerPackage, on_delete=models.CASCADE)
    catogery = models.ForeignKey(customerCatogery, on_delete=models.CASCADE)
    
#PERFORMANCE REPORT  
class performanceReport(models.Model):
    companyName = models.ForeignKey(Customer, on_delete=models.CASCADE)
    staffID = models.ForeignKey(Staff, on_delete=models.CASCADE)
    dateSubmission = models.DateField()
    submittedReport = models.IntegerField(default=1000)
    remark = models.TextField()
    duration = models.TextField()
    report = models.FileField(upload_to='report/%Y', blank=True, null=True) 
    
    def _str_(self):
        return str(self.report)
    
