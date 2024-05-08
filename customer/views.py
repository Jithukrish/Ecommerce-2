from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login as authlogin,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from  . models import Customer

def signout(request):
    logout(request)
    return redirect('index')

def account(request):
    context={}
    if request.method == 'POST' and "register" in request.POST:
        context['register']=True
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            email = request.POST.get("email")
            address = request.POST.get("address")
            phone = request.POST.get("phone")

            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )

            customer = Customer.objects.create(
                name=username,
                user=user,
                phone=phone,
                address=address,
            )
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('index')
        
        except IntegrityError:
            error_message = "Duplicate username not allowed"
            messages.error(request, error_message)
        # except Exception as e:
        #     error_message="duplicate username not allowed"
        #     messages.error(request,error_message)
        except ValueError as ve:
            messages.error(request, str(ve))

    if request.method == 'POST' and "login" in request.POST:
        context['register'] = False  

        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            print(username,password)

            user = authenticate(request, username=username, password=password)
            print(username,password)           
            if user:
                login(request, user)
                return redirect('index')  # Return the redirect response
            else:
                messages.error(request, 'Invalid username or password')
        except Exception as e:
            print(e)
            messages.error(request, 'An error occurred during login')
                     

    return render(request, "account.html",context)
