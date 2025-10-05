from django.shortcuts import render

# Create your views here.

def signupfunc(request):
    # render(描写する)は引数を3つとる
    # requestオブジェクト、テンプレート名、テンプレートに渡す辞書の3つの情報を編集して返す
    return render(request, 'signup.html', {'some':100})