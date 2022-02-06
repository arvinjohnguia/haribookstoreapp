# DELETE
def processAddProduct(request):
    procode = request.POST.get('procode')
    proname = request.POST.get('proname')
    procategory = request.POST.get('procategory')
    proprice = request.POST.get('proprice')
    proquantity = request.POST.get('proquantity')
    prosold = request.POST.get('prosold')
    prototalsales = request.POST.get('prototalsales')

    if request.FILES.get('image'):
        proimage = request.FILES.get('proimage')
    else:
        proimage = 'inventory/placeholder.jpg'
    try:
        n = Inventory.objects.get(pro_code = procode)
        # number already exists
        return render(request, 'users/addUser.html',{
            'error_message' : "Duplicated Product Code: " + procode
        })
    except ObjectDoesNotExist:
        inventory = Inventory.objects.create(pro_code = procode, pro_name = proname, pro_category = procategory, pro_price = proprice, pro_quantity = proquantity,  pro_sold = prosold,  pro_totalsales = prototalsales, pro_image = proimage)
        inventory.save()
        return HttpResponseRedirect('/users/inventorySummary')

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