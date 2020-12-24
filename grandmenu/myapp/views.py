from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic

from .forms import StoreInfoForm
from .models import StoreInfo



# Create your views here.
class Home(generic.TemplateView):
    template_name = 'myapp/home.html'

def debug_storeinfo(request):
    params = {'message': '', 'form': None}
    if request.method == 'POST':
        form = StoreInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:debug_storeinfolist')
        else:
            params['message'] = '再入力して下さい'
            params['form'] = form
    else:
        params['form'] = StoreInfoForm()
    return render(request, 'myapp/debug_storeinfo.html', params)
 
 
def debug_storeinfolist(request):
    data = StoreInfo.objects.all()
    params = {'message': '店情報の一覧', 'data': data}
    return render(request, 'myapp/debug_storeinfolist.html', params)