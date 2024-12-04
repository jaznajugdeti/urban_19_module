# from django.shortcuts import render
# from django.http import HttpResponse
# from .forms import UserRegister
# from .models import Buyer, Game
#
# # if password == repeat_password and int(age) >= 18 and username not in buyers:
# #
# # Buyer.object.create(name=username, balance=2000.0, age=age)
#
# buyers = ['user1', 'user2', 'user3', 'user4']
# def sign_up_by_html(request):
#     info = {}
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         repeat_password = request.POST.get('repeat_password')
#         age = int(request.POST.get('age'))
#
#     if password == repeat_password and int(age) >= 18 and username not in buyers:
#
# Buyer.object.create(name=username, balance=2000.0, age=age)
#     if password != repeat_password:
#         info['error'] = "Пароли не совпадают"
#         return HttpResponse('Пароли не совпадают')
#     elif age < 18:
#         info['error'] = "Вы должны быть старше 18"
#         return HttpResponse('Вы должны быть старше 18')
#     elif username in users:
#         info['error'] = "Пользователь уже существует"
#         return HttpResponse('Пользователь уже существует')
#     else:
#         info['welcome_message'] = f"Приветствуем, {username}!"
#         return HttpResponse(f'Приветствуем, {username}!')
#
#     return render(request, 'fifth_task/registration_page.html', context=info)
#
#
# def sign_up_by_html(request):
#     info = {}
#     if request.method == 'POST':
#         form = UserRegister(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             repeat_password = form.cleaned_data['repeat_password']
#             age = form.cleaned_data['age']
#
#             if password != repeat_password:
#                 info['error'] = "Пароли не совпадают"
#                 return HttpResponse('Пароли не совпадают')
#             elif age < 18:
#                 info['error'] = "Вы должны быть старше 18"
#                 return HttpResponse('Вы должны быть старше 18')
#             elif username in users:
#                 info['error'] = "Пользователь уже существует"
#                 return HttpResponse('Пользователь уже существует')
#             else:
#                 info['welcome_message'] = f"Приветствуем, {username}!"
#             return HttpResponse(f"Приветствуем, {username}!")
#     else:
#         form = UserRegister()
#         info['message'] = form
#
#     return render(request, 'fifth_task/registration_page.html', info)