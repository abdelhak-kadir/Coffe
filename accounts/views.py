from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from .models import UserProfile
from products.models import Product
import re  # valide email

# Create your views here.


def signin(request):
    if request.method == 'POST' and 'btnsignin' in request.POST:
        username = request.POST['user']
        password = request.POST['pass']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if 'remembreme' not in request.POST:
                # the session will expire as soon as the user closes their browser.
                request.session.set_expiry(0)
            auth.login(request, user)
            # messages.success(request, 'You are now logged in')
        else:
            messages.error(request, 'Username or password invalid')
        return redirect('signin')
    else:
        return render(request, 'Accounts/signin.html')


def logout(request):
    if request.user.is_authenticated:  # determine if the user is authenticated or not
        auth.logout(request)
    return redirect('index')


def signup(request):
    if request.method == 'POST' and 'btnsignup' in request.POST:
        # variables for fields
        fname = None
        lname = None
        address = None
        address2 = None
        city = None
        state = None
        code = None
        email = None
        username = None
        password = None
        terms = None
        is_added = None
        # Get values from the form
        if 'fname' in request.POST:
            fname = request.POST['fname']
        else:
            messages.error(request, 'Error in first name')

        if 'lname' in request.POST:
            lname = request.POST['lname']
        else:
            messages.error(request, 'Error in last name')
        if 'address' in request.POST:
            address = request.POST['address']
        else:
            messages.error(request, 'Error in address ')
        if 'address2' in request.POST:
            address2 = request.POST['address2']
        else:
            messages.error(request, 'Error in address2 ')
        if 'city' in request.POST:
            city = request.POST['city']
        else:
            messages.error(request, 'Error in city ')
        if 'state' in request.POST:
            state = request.POST['state']
        else:
            messages.error(request, 'Error in state ')
        if 'code' in request.POST:
            code = request.POST['code']
        else:
            messages.error(request, 'Error in code ')
        if 'email' in request.POST:
            email = request.POST['email']
        else:
            messages.error(request, 'Error in email ')
        if 'user' in request.POST:
            username = request.POST['user']
        else:
            messages.error(request, 'Error in username ')
        if 'pass' in request.POST:
            password = request.POST['pass']
        else:
            messages.error(request, 'Error in password ')
        if 'terms' in request.POST:
            terms = request.POST['terms']
            # check the values
            if fname and lname and address and address2 and city and state and code and email and username and password:
                if terms == 'on':
                    # check if username is taken
                    if User.objects.filter(username=username).exists():
                        messages.error(request, 'This username is taken')
                    else:
                        # check if email is taken
                        if User.objects.filter(email=email).exists():
                            messages.error(request, 'This email is taken')
                        else:
                            # regexp for email validation
                            patt = "^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
                            if re.match(patt, email):
                                # add user
                                user = User.objects.create_user(
                                    first_name=fname,
                                    last_name=lname,
                                    username=username,
                                    email=email,
                                    password=password
                                )
                                user.save()
                                # add user profile
                                userprofile = UserProfile(
                                    user=user,
                                    address=address,
                                    address2=address2,
                                    city=city,
                                    state=state,
                                    code=code
                                )
                                userprofile.save()
                                # clear fields
                                fname = ''
                                lname = ''
                                address = ''
                                address2 = ''
                                city = ''
                                state = ''
                                email = ''
                                code = ''
                                username = ''
                                password = ''
                                terms = None
                                # success Message
                                messages.success(
                                    request, 'Your account is created')
                                is_added = True
                            else:
                                messages.error(request, 'Invalid email')
                else:
                    messages.error(request, 'You must agree to the terms')
            else:
                messages.error(request, 'check empty fields')
        return render(request, 'Accounts/signup.html', {
            'fname': fname,
            'lname': lname,
            'address': address,
            'address2': address2,
            'city': city,
            'state': state,
            'code': code,
            'email': email,
            'user': username,
            'pass': password,
            'is_added': is_added
        })
    else:
        return render(request, 'Accounts/signup.html')


def profile(request):
    if request.method == 'POST' and 'btnsave' in request.POST:
        if request.user is not None and request.user.id != None:
            userprofile = UserProfile.objects.get(user=request.user)
            if request.POST['fname'] and request.POST['lname'] and request.POST['address'] and request.POST['address2'] and request.POST['city'] and request.POST['state'] and request.POST['code'] and request.POST['email'] and request.POST['user'] and request.POST['pass']:
                request.user.first_name = request.POST['fname']
                request.user.last_name = request.POST['lname']
                userprofile.address = request.POST['address']
                userprofile.address2 = request.POST['address2']
                userprofile.city = request.POST['city']
                userprofile.code = request.POST['code']
                userprofile.state = request.POST['state']
                # request.user.email = request.POST['email']
                # request.user.username = request.POST['user']
                userprofile.save()
                # check if a string starts with the specified substring.
                if not request.POST['pass'].startswith('pbkdf2_sha256$'):
                    request.user.set_password(request.POST['pass'])
                request.user.save()

                auth.login(request, request.user)
                messages.success(request, 'Your data has been saved')
            else:
                messages.error(request, 'Check your values and elements')
        return redirect('profile')
    else:
        if request.user is not None:
            context = None
            if not request.user.is_anonymous:

                userprofile = UserProfile.objects.get(user=request.user)
                context = {
                    'fname': request.user.first_name,
                    'lname': request.user.last_name,
                    'address': userprofile.address,
                    'address2': userprofile.address2,
                    'city': userprofile.city,
                    'code': userprofile.code,
                    'state': userprofile.state,
                    'email': request.user.email,
                    'user': request.user.username,
                    'pass': request.user.password
                }

            return render(request, 'Accounts/profile.html', context)
        else:
            return redirect('profile')


def product_fav(request, pro_id):
    if request.user.is_authenticated and not request.user.is_anonymous:
        pro_fav = Product.objects.get(pk=pro_id)
        if UserProfile.objects.filter(user=request.user, product_fav=pro_fav).exists():
            messages.success(request, 'Already product in the favorite list')
        else:
            userprofile = UserProfile.objects.get(user=request.user)
            userprofile.product_fav.add(pro_fav)
            messages.success(request, 'Product has been favroted')
    else:
        messages.error(request, 'You must be logged in ')
    return redirect('/products/' + str(pro_id))


def show_product_fav(request):
    context = None
    if request.user.is_authenticated and not request.user.is_anonymous:
        userInfo = UserProfile.objects.get(user=request.user)
        pro = userInfo.product_fav.all()
        context = {'products': pro}
    return render(request, 'products/products.html', context)
