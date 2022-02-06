<a href ="{% url 'users:editProduct' user.id %}" class="btn btn-primary mb-2">Update Product</a>

def editProduct(request, profile_id):
    try:
        inventory = Inventory.objects.get(pk=profile_id)
    except Inventory.DoesNotExist:
        raise Http404("Product does not exist.")
    return render(request, 'users/editProduct.html', {'inventory': inventory})

def processEditProduct(request, profile_id):
    inventory = get_object_or_404(Inventory, pk=profile_id)
    profile_pic = request.FILES.get('image')
    try:
        procode = request.POST.get('procode')
        proname = request.POST.get('proname')
        procategory = request.POST.get('procategory')
        proprice = request.POST.get('proprice')
        proquantity = request.POST.get('proquantity')
        prosold = request.POST.get('prosold')
        prototalsales = request.POST.get('prototalsales')
    except (KeyError, Inventory.DoesNotExist):
        return render(request, 'users/userDetails.html', { 
            'inventory': inventory,
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