import profile
from unicodedata import category
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import User, Inventory
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.core.paginator import Paginator
from django.db.models import Q

# For login, authentication, authorization
# django part 5
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.

# For login, authentication, authorization
# django part 5
def loginView(request):
    return render(request, 'users/login.html')

def processLogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    useradmin = authenticate(username=username, password=password)
    if useradmin is not None:
        login(request, useradmin)
        return HttpResponseRedirect('/users/inventorySummary')
    else:
        return render(request, 'users/login.html', {'error_message': "Wrong Username or Password"})
    
def processLogout(request):
    logout(request)
    return HttpResponseRedirect('/users/')

# END OF LOGIN

# EMPLOYEE FUNCTIONS

def employeeList(request):
    # To display all customers
    # user_list = User.objects.order_by('id') 
    # context = {'user_list': user_list}
    # return render(request, 'users/employeeList.html', context)

    # FOR PAGINATION | part 4 django
    user_list = User.objects.all().order_by('id') #kapag may - yung order by magiging desc order
    paginator = Paginator(user_list, 10)
    page_number = request.GET.get('page')

    user_list = paginator.get_page(page_number)
    return render(request, 'users/employeeList.html', {'page_obj': user_list})
    
def addUser(request):
    return render(request, 'users/addUser.html')

def processAddUser(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    college = request.POST.get('college')
    year = request.POST.get('year')
    course = request.POST.get('course')
    address = request.POST.get('address')
    gender = request.POST.get('gender')
    contactnumber = request.POST.get('contactnumber')
    birthdate = request.POST.get('birthdate')

    if request.FILES.get('image'):
        image = request.FILES.get('image')
    else:
        image = 'profile_pic/image.jpg'
    try:
        n = User.objects.get(user_email = email)
        # number already exists
        return render(request, 'users/addUser.html',{
            'error_message' : "Duplicated Email: " + email
        })
    except ObjectDoesNotExist:
        user = User.objects.create(user_fname = fname, user_lname = lname, user_email=email, user_college = college, user_year = year, user_course = course, user_address = address, user_gender = gender, user_contactnumber = contactnumber, user_birthdate = birthdate, user_image = image)
        user.save()
        return HttpResponseRedirect('/users/employeeList')

@login_required(login_url='/users/')
def userDetails(request, profile_id):
    try:
        user = User.objects.get(pk=profile_id)
    except User.DoesNotExist:
        raise Http404("User does not exist.")
    return render(request, 'users/userDetails.html', {'user': user})

def deleteUser(request, profile_id):
    User.objects.filter(id=profile_id).delete()
    return HttpResponseRedirect('/users/employeeList')

@login_required(login_url='/users/login')
@permission_required('users.change_user', login_url='/users/login')
def editUser(request, profile_id):
    try:
        user = User.objects.get(pk=profile_id)
    except User.DoesNotExist:
        raise Http404("User does not exist.")
    return render(request, 'users/editUser.html', {'user': user})

def processEditUser(request, profile_id):
    user = get_object_or_404(User, pk=profile_id)
    profile_pic = request.FILES.get('image')
    try:
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        college = request.POST.get('college')
        year = request.POST.get('year')
        course = request.POST.get('course')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        contactnumber = request.POST.get('contactnumber')
    except (KeyError, User.DoesNotExist):
        return render(request, 'users/userDetails.html', { 
            'user': user,
            'error_message': 'Problem Updating Record'
        })
    else:
        user_profile = User.objects.get(id=profile_id)
        user_profile.user_fname = fname
        user_profile.user_lname = lname
        user_profile.user_email = email
        user_profile.user_college = college
        user_profile.user_year = year
        user_profile.user_course = course
        user_profile.user_address = address
        user_profile.user_gender = gender
        user_profile.user_contactnumber = contactnumber
        if profile_pic:
            user_profile.user_image = profile_pic
        user_profile.save()
        return HttpResponseRedirect(reverse('users:userDetails', args=(profile_id,)))
        # 37:30 | PART 3 | explanation of logic, and reverse()

    # 31:13 | PART 3 | get_object_or_404 = queries in database
    # it will search for primary key na ipapasa natin
    # pag walang ma-query magrereturn siya ng 404
    # checks if data exists in database

def searchForUser(request):
    term = request.GET.get('searchForUser', '')
    # dalawa yung parameter kasi hindi naman lagi nagse-search si user. kapag yung searchForUser lang, mag-eerror siya.
    user_list = User.objects.filter(Q(user_fname__icontains = term)  | Q(user_lname__icontains = term) |  Q(user_college__icontains = term) |  Q(user_course__icontains = term) |  Q(user_gender__icontains = term)).order_by('id')
    # double underscore for wildcard
    # read documentation for wildcard

    paginator = Paginator(user_list, 10)
    page_number = request.GET.get('page')

    user_list = paginator.get_page(page_number)
    return render(request, 'users/employeeList.html', {'page_obj': user_list})
    
# INVENTORY FUNCTIONS

def inventorySummary(request):
    # To display all customers
    # user_list = User.objects.order_by('id') 
    # context = {'user_list': user_list}
    # return render(request, 'users/employeeList.html', context)

    # FOR PAGINATION | part 4 django
    inventory_list = Inventory.objects.all().order_by('pro_category') #kapag may - yung order by magiging desc order
    paginator = Paginator(inventory_list, 10)
    page_number = request.GET.get('page')

    user_list = paginator.get_page(page_number)
    return render(request, 'inventorys/inventorySummary.html', {'page_obj': user_list})

def addProduct(request):
    return render(request, 'inventorys/addProduct.html')

def processAddProduct(request):
    procode = request.POST.get('procode')
    proname = request.POST.get('proname')
    procategory = request.POST.get('procategory')
    proprice = request.POST.get('proprice')
    proquantity = request.POST.get('proquantity')
    prosold = request.POST.get('prosold')
    prototalsales = request.POST.get('prototalsales')

    if request.FILES.get('proimage'):
        proimage = request.FILES.get('proimage')
    else:
        proimage = 'inventory/placeholder.jpg'
    try:
        n = Inventory.objects.get(pro_code = procode)
        # number already exists
        return render(request, 'inventorys/addProduct.html',{
            'error_message' : "Duplicated Product: " + procode
        })
    except ObjectDoesNotExist:
        inventory = Inventory.objects.create(pro_code = procode, pro_name = proname, pro_category = procategory, pro_price = proprice, pro_quantity = proquantity,  pro_sold = prosold,  pro_totalsales = prototalsales, pro_image = proimage)
        inventory.save()
        return HttpResponseRedirect('/users/inventorySummary')


def deleteProduct(request, product_id):
    Inventory.objects.filter(id=product_id).delete()
    return HttpResponseRedirect('/users/inventorySummary')


def searchForProduct(request):
    term = request.GET.get('searchForProduct', '')
    inventory_list = Inventory.objects.filter(Q(pro_code__icontains = term)  | Q(pro_category__icontains = term) |  Q(pro_name__icontains = term)).order_by('id')

    paginator = Paginator(inventory_list, 10)
    page_number = request.GET.get('page')

    user_list = paginator.get_page(page_number)
    return render(request, 'inventorys/inventorySummary.html', {'page_obj': user_list})


def productDetails(request, product_id):
    try:
        inventory = Inventory.objects.get(pk=product_id)
    except User.DoesNotExist:
        raise Http404("Product does not exist.")
    return render(request, 'inventorys/productDetails.html', {'inventory': inventory})

def editProduct(request, product_id):
    try:
        inventory = Inventory.objects.get(pk=product_id)
    except Inventory.DoesNotExist:
        raise Http404("Product does not exist.")
    return render(request, 'inventorys/editProduct.html', {'inventory': inventory})

def processEditProduct(request, product_id):
    inventory = get_object_or_404(Inventory, pk=product_id)
    proimage = request.FILES.get('proimage')
    try:
        procode = request.POST.get('procode')
        proname = request.POST.get('proname')
        procategory = request.POST.get('procategory')
        proprice = request.POST.get('proprice')
        proquantity = request.POST.get('proquantity')
        prosold = request.POST.get('prosold')
        prototalsold = request.POST.get('prototalsold')
        prototalsales = request.POST.get('prototalsales')
    except (KeyError, Inventory.DoesNotExist):
        return render(request, 'inventorys/productDetails.html', { 
            'inventory': inventory,
            'error_message': 'Problem Updating Info'
        })
    else:
        product_info = Inventory.objects.get(id=product_id)
        product_info.pro_code = procode
        product_info.pro_name = proname
        product_info.pro_category = procategory
        product_info.pro_price = proprice
        product_info.pro_quantity = proquantity
        product_info.pro_sold = prosold
        product_info.pro_totalsold = prototalsold
        product_info.pro_totalsales = prototalsales
        if proimage:
            product_info.pro_image = proimage
        product_info.save()
        return HttpResponseRedirect(reverse('users:productDetails', args=(product_id,)))

# FOR QUANTITY SOLD/ STOCKS LEFT
def processUpdateQuantityValues(request, product_id):
    quantisold = request.POST.get('prosold')
    


