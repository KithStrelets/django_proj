from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.template.loader import get_template
from django.template import Context
from .models import Jobs, Workers, Storage,Menu,Order
from .forms import JobForm, WorkerForm, StorageForm, MenuForm, OrderForm, DeleteJobForm, DeleteWorkerForm,DeleteStorageForm, DeleteMenuForm,DeleteOrderForm

# def template(request):
#    view = "template1"
#    t = get_template('job.html')
#    html = t.render(Context({'name': view}))
#    return HttpResponse(html)

def index(request):
    return render(request, 'index.html')

def jobs(request):
    jform = JobForm()
    if request.method == 'POST':
        if "Add" in request.POST:
            jform = JobForm(request.POST)
            if jform.is_valid():
                job = jform.save(commit=False)
                job.save()
                jform = JobForm()
    elif request.method == 'GET':
        if "Delete" in request.GET:
            deljobname = request.GET['jobname']
            Jobs.objects.filter(jobname=deljobname).delete()
    else:
        jform = JobForm()
    return render(request, 'jobs.html', {'jobs': Jobs.objects.all().order_by('jobname'), 'form': jform, 'jobnames':Jobs.objects.order_by('jobname').values_list('jobname', flat=True).distinct()})

def workers(request):
    wform = WorkerForm()
    if request.method == 'POST':
        if "Add" in request.POST:
            wform = WorkerForm(request.POST)
            if wform.is_valid():
                worker = wform.save(commit=False)
                worker.save()
                wform = WorkerForm()
    elif request.method == 'GET':
        if "Delete" in request.GET:
            delworkername = request.GET['workername']
            Workers.objects.filter(workername=delworkername).delete()
    else:
        wform = WorkerForm()
    return render(request, 'workers.html', {'workers': Workers.objects.all(), 'form': wform, 'workernames':Workers.objects.order_by('workername').values_list('workername', flat=True).distinct()})

def storage(request):
    sform = StorageForm()
    if request.method == 'POST':
        if "Add" in request.POST:
            sform = StorageForm(request.POST)
            if sform.is_valid():
                item = sform.save(commit=False)
                item.save()
                sform = StorageForm()
    elif request.method == 'GET':
        if "Delete" in request.GET:
            delitemname = request.GET['itemname']
            delitemprovider = request.GET['itemprovider']
            Storage.objects.filter(itemname=delitemname, itemprovider=delitemprovider).delete()
    else:
        sform = StorageForm()

    return render(request, 'storage.html', {'storage': Storage.objects.all(), 'form': sform,'providers': Storage.objects.order_by('itemprovider').values_list('itemprovider', flat=True).distinct(),
 'products':Storage.objects.order_by('itemname').values_list('itemname', flat=True).distinct()})

def menu(request):
    mform = MenuForm()
    if request.method == 'POST':
        if "Add" in request.POST:
            mform = MenuForm(request.POST)
            if mform.is_valid():
                dish = mform.save(commit=False)
                dish.save()
                mform = MenuForm()
    elif request.method == 'GET':
        if "Delete" in request.GET:
            delmenu = request.GET['menuname']
            Menu.objects.filter(menuname=delmenu).delete()
    else:
        mform = MenuForm()
    return render(request, 'menu.html', {'menu': Menu.objects.all(), 'form': mform, 'dishnames':Menu.objects.order_by('menuname').values_list('menuname', flat=True).distinct()})

def order(request):
    oform = OrderForm()
    delorder = DeleteOrderForm()
    if request.method == 'POST':
        if "Add" in request.POST:
            oform = OrderForm(request.POST)
            if oform.is_valid():
                order = oform.save(commit=False)
                order.save()
                oform = MenuForm()
    elif request.method == 'GET':
        if "Delete" in request.GET:
            delorder = request.GET['ordername']
            delorderworker = request.GET['orderworker']
            Order.objects.filter(ordername=delorder, orderworker=delorderworker).delete()
    else:
        oform = OrderForm()

    return render(request, 'order.html', {'orders': Order.objects.all(), 'form': oform, 'dform': delorder})

def personneldep(request):
    simplerender = render(request, 'personneldep.html',{'personnel': Workers.objects.all(), 'fields': Workers._meta.get_fields()})
    if request.method == 'GET':
        orderby = str(request.GET.get('orderby'))
        if(orderby=='None' or orderby=='order'):
           return simplerender
        #orderfield = str(request.GET['orderfield'])
        return render(request, 'personneldep.html', {'personnel': Workers.objects.all().order_by(orderby), 'fields': Workers._meta.get_fields()})
    else:
        return simplerender

def restmenu(request):
    simplerender = render(request, 'restmenu.html',{'menu': Menu.objects.all(), 'fields': Storage.objects.order_by('itemprovider').values_list('itemprovider', flat=True).distinct()})
    if request.method == 'GET':
        orderby = str(request.GET.get('orderby'))
        if (orderby=='None' or orderby=='all'):
           return simplerender
        return render(request, 'restmenu.html',{'menu': Menu.objects.all().filter(idfirstitem__itemprovider=orderby), 'fields': Storage.objects.order_by('itemprovider').values_list('itemprovider', flat=True).distinct()})
    else:
        return simplerender

def orderqueue(request):
    simplerender = render(request, 'orderqueue.html', {'orders': Order.objects.all(), 'fields': Order._meta.get_fields()})
    if request.method == 'GET':
        orderby = str(request.GET.get('orderby'))
        if (orderby=='None' or orderby == 'all'):
            return simplerender
        return render(request, 'orderqueue.html',{'orders': Order.objects.all().filter(ordercomplete = orderby), 'fields': Order._meta.get_fields()})
    else:
        return simplerender
# def job(request, job_id=1):
# return render_to_response('job.html',{'job': Jobs.objects.get(id=job_id)})
# Create your views here.
