from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic

from .forms import StoreInfoForm
from accounts.forms import LoginForm, UserCreateForm
from .models import StoreInfo

from django.contrib.auth.decorators import login_required


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

@login_required
def store_setting(request):
    params = {'message': '', 'form': None}

    if request.method == 'POST':
        form = StoreInfoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)      #変更を加える場合は(commit=False)オプション。　それ以外はform.saveで良い(このときpost変数に受ける必要もない)
            post.STORE_EMAIL = request.user          #ログインユーザーEmail取得(不正html操作で書き換えられてもここで正確に入力する)
            post.save()
            return redirect('myapp:store_mypage')
        else:
            params['message'] = '再入力して下さい'
            params['form'] = form
    else:
        store_email = StoreInfo(STORE_EMAIL=request.user)   #form入力以外で設定したいのでインスタンスを作成しておく
        params['form'] = StoreInfoForm(instance=store_email)
    return render(request, 'myapp/store_setting.html', params)

@login_required
def store_mypage(request):
    if StoreInfo.objects.filter(STORE_EMAIL=request.user).exists():
        '''============================memo============================
        datas = StoreInfo.objects.get(STORE_EMAIL=request.user)の場合
        datas.STORE_EMAIL   等でアクセスできる。

        datas = StoreInfo.objects.filter(STORE_EMAIL=request.user)の場合
        for data in datas:
            data.STORE_EMAIL    等でアクセスできる。
        ※filterの場合は、htmlへ投げる辞書を作成する際はこのまま投げることができる。
        params = {'message': '店舗情報', 'data': datas}
        ============================memo============================'''
#if 1
        # <T.B.D>こっちの検討も...first()なので大規模になった際は速度が早い
        data_buf = StoreInfo.objects.filter(STORE_EMAIL=request.user).first()
        data = {
            'E_Mail': data_buf.STORE_EMAIL,
            '店舗名': data_buf.STORE_NAME,
            '郵便番号': data_buf.STORE_POSTAL_CODE,
            '住所': data_buf.STORE_ADDRESS,
            '電話番号': data_buf.STORE_TEL
        }
#else
        # data = StoreInfo.objects.filter(STORE_EMAIL=request.user)
#endif

        params = {'message': '店舗情報', 'data': data}
        return render(request, 'myapp/debug_mypage.html', params)
    else:
        return redirect('myapp:store_setting')