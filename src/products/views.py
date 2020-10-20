# from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

def product_list_view(request):
    queryset = Product.objects.all()            # list of objects Product
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        print(request)
        obj.delete()
        return redirect("../../")
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)


# the name of the argument has to match with that in urls.py <>
def product_detail_view(request, id):
    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)

def product_update_view(request, id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()

    context = {
        "form": form
    }
    return render(request, "products/product_create.html", context)

def product_create_view(request):
    # obj = Product.objects.get(id=1)
    # form = ProductForm(request.POST or None, instance=obj)
    # ^ this is how you modify existing model form data
    form = ProductForm(request.POST or None)
    if (form.is_valid()):
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }

    return render(request, "products/product_create.html", context)

# Create your views here.
# def product_detail_view(request):
#     obj = Product.objects.get(id=1)
#     # context = {
#     #     "title": obj.title,
#     #     "description": obj.description
#     # }
#     context = {
#         'object': obj
#     }
#     return render(request, "products/product_detail.html", context)