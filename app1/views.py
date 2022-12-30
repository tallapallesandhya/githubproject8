from django.shortcuts import render

# Create your views here.
def jinja_print3(request):
    d={'name':'sandhya','batchcode':'74de5','mno':'6305680113'}
    return render(request,'jinja_print3.html',context=d)
