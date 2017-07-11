from django.db import models


class Jobs(models.Model):

    idjob = models.AutoField( primary_key=True)
    jobname = models.CharField("Job", max_length=20, null=False)
    jobsalary = models.IntegerField("Salary", null=False)
    jobtodo = models.CharField("What to do", max_length=45, null=False)
    jobrules = models.CharField("Rules", max_length=45, null=False)

    def __str__(self):
        #return 'id=%s; %s; Salary=%s; %s; %s' % (self.idjob, self.jobname, self.jobsalary, self.jobtodo, self.jobrules)
        return  '%s; Salary: %s' %(self.jobname, self.jobsalary)
# class Worker(models.Model)
# Create your models here.
class Workers(models.Model):
    idworker = models.AutoField(primary_key=True)
    workername = models.CharField("Worker",max_length=50, null=False)
    workerage = models.IntegerField("Age",default=20, null=False)
    workergender = models.CharField("Gender",max_length=10, null=False)
    workeraddress = models.CharField("Address",max_length=50, null=False)
    workerpass = models.CharField("Passport",max_length=70, null=False)
    workerjob = models.ForeignKey(Jobs, verbose_name="Job")

    def __str__(self):
        #return 'id=%s; %s; Age=%s; %s; %s; %s; %s' % (self.idworker, self.workername, self.workerage, self.workergender, self.workeraddress, self.workerpass, self.workerjob)
        return '%s; %s'%(self.workername,self.workerjob)

class Storage(models.Model):
    idstorage = models.AutoField(primary_key=True)
    itemname = models.CharField("Product",max_length=50, null=False)
    itemdate = models.DateField("Date of production",null=False)
    itemvalue = models.IntegerField("Value",null=False,default=100)
    itemtouse = models.DateField("Date to use",null=False)
    itemcost = models.IntegerField("Cost",null=False, default=100)
    itemprovider = models.CharField("Provider",null=False, max_length=50)

    def __str__(self):
        #return 'id=%s; %s; %s; Value=%s; %s; Cost=%s; %s' % (self.idstorage, self.itemname, self.itemdate, self.itemvalue, self.itemtouse, self.itemcost, self.itemprovider)
        return '%s; Cost: %s; %s'%(self.itemname, self.itemcost, self.itemprovider)

class Menu(models.Model):
    idmenu = models.AutoField(primary_key=True)
    menuname = models.CharField("Dish",max_length=50, null=False)
    idfirstitem = models.ForeignKey(Storage, related_name="%(app_label)s_%(class)s_firstitemrelated", verbose_name="First product")
    firstitemvalue = models.IntegerField("Value of the first",null=False)
    idsecondtitem = models.ForeignKey(Storage, related_name="%(app_label)s_%(class)s_seconditemrelated", verbose_name="Second product")
    seconditemvalue = models.IntegerField("Value of the second",null=False)
    idthirdtitem = models.ForeignKey(Storage, related_name="%(app_label)s_%(class)s_thirditemrelated", verbose_name="Third product")
    thirditemvalue = models.IntegerField("Value of the third",null=False)
    price = models.IntegerField("Price",null=False)
    cooktime = models.TimeField("Cook time",null=False)

    def __str__(self):
        return '%s; %s; Value1=%s; %s; Value2=%s; %s; Value3=%s; Price=%s; %s' % (self.menuname,self.idfirstitem, self.firstitemvalue, self.idsecondtitem, self.seconditemvalue, self.idthirdtitem, self.thirditemvalue, self.price, self.cooktime)


class Order(models.Model):
    idorder = models.AutoField(primary_key=True)
    orderdatetime = models.DateTimeField("Order date and time",null=False)
    ordername = models.CharField("Customer",max_length=50, null=False)
    orderphone = models.IntegerField("Customer's phone", null=False)
    orderfirstdish = models.ForeignKey(Menu, related_name="%(app_label)s_%(class)s_firstrelated", verbose_name="First dish")
    orderseconddish = models.ForeignKey(Menu, related_name="%(app_label)s_%(class)s_secondrelated", null=True, blank=True, verbose_name="Second dish")
    orderthirddish = models.ForeignKey(Menu, related_name="%(app_label)s_%(class)s_thirdrelated", null=True, blank=True, verbose_name="Third dish")
    orderprice = models.IntegerField("Total price",null=False)
    ordercomplete = models.CharField("Status",max_length=50, null=False)
    orderworker = models.ForeignKey(Workers, null=True, verbose_name="Order waiter")

    def __str__(self):
        return 'id=%s; %s; %s; Phone=%s; %s; %s; %s; Price=%s; %s; %s' % (self.idorder, self.orderdatetime, self.ordername, self.orderphone, self.orderfirstdish, self.orderseconddish,self.orderthirddish, self.orderprice, self.ordercomplete, self.orderworker)

