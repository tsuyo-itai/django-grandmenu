from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from .forms import StoreInfoForm, StoreMenuForm
from .models import StoreInfo, StoreMenu
from django.utils.safestring import mark_safe
import json

# Create your views here.
class Home(generic.TemplateView):
    template_name = 'myapp/home.html'

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
        params['form'] = StoreInfoForm()
    return render(request, 'myapp/store_setting.html', params)

@login_required
def store_show_menu(request):
    params = {'message': '', 'form': None}

    if request.method == 'POST':
        form = StoreMenuForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.STORE_INFO = StoreInfo.objects.get(STORE_EMAIL=request.user)
            post.save()
            return redirect('myapp:store_show_menu')
    else:
        #店舗情報が入力されているか?
        if StoreInfo.objects.filter(STORE_EMAIL=request.user).exists():
            params['form'] = StoreMenuForm()
        else:
            return redirect('myapp:store_setting')

    return render(request, 'myapp/debug_store_show_menu.html', params)

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

@login_required
def store_mypage_edit(request):
    params = {'message': '', 'form': None, 'data': None}
    if request.method == 'POST':
        form_instance = StoreInfo(STORE_EMAIL=request.user)     #現在のユーザー名のインスタンスをmodelから取得
        form = StoreInfoForm(request.POST, instance=form_instance)
        if form.is_valid():
            # StoreInfo.objects.filter(STORE_EMAIL=request.user).update(STORE_EMAIL=None)     #Emailがユニークキーなので厄介。一旦NULLに書き換えた後にformの内容で更新
            StoreInfo.objects.filter(STORE_EMAIL=request.user).delete()     #上記updateを行うとゴミmodel情報(EMAIL=NULL)が残るのでdeleteで消してしまう。
            form.save()
            return redirect('myapp:store_mypage')
        else:
            params['message'] = '再入力して下さい'
            params['form'] = form
    else:
        data_buf = StoreInfo.objects.filter(STORE_EMAIL=request.user).first()
        data = {
            'STORE_EMAIL': data_buf.STORE_EMAIL,
            'STORE_NAME': data_buf.STORE_NAME,
            'STORE_POSTAL_CODE': data_buf.STORE_POSTAL_CODE,
            'STORE_ADDRESS': data_buf.STORE_ADDRESS,
            'STORE_TEL': data_buf.STORE_TEL
        }

        params['form'] = StoreInfoForm()
        params['data'] = data
    return render(request, 'myapp/debug_mypage_edit.html', params)


def debug_websocket(request):
    # return render(request, 'myapp/debug_websocket.html', {})
    return render(request, 'myapp/debug_websocket.html')

def debug_websocket_room(request, room_name):
    return render(request, 'myapp/debug_websocket_room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })