from django import forms
from .models import Jobs, Workers, Storage, Menu, Order

class JobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ['idjob', 'jobname', 'jobsalary', 'jobtodo', 'jobrules']
class DeleteJobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ['jobname']

class WorkerForm(forms.ModelForm):
    class Meta:
        model = Workers
        fields = ['idworker', 'workername', 'workerage', 'workergender', 'workeraddress','workerpass', 'workerjob' ]
class DeleteWorkerForm(forms.ModelForm):
    class Meta:
        model = Workers
        fields = ['workername']

class StorageForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = ['idstorage', 'itemname', 'itemdate', 'itemvalue', 'itemtouse', 'itemcost', 'itemprovider']
class DeleteStorageForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = ['itemname', 'itemprovider']


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['idmenu', 'menuname', 'price', 'cooktime', 'idfirstitem', 'firstitemvalue', 'idsecondtitem', 'seconditemvalue', 'idthirdtitem', 'thirditemvalue']
class DeleteMenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['menuname']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['idorder', 'orderdatetime', 'ordername', 'orderphone', 'orderfirstdish', 'orderseconddish', 'orderthirddish', 'orderprice', 'ordercomplete', 'orderworker']
class DeleteOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['ordername', 'orderworker']
