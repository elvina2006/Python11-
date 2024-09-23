from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from .models import Product
from .forms import ProductFilter

class ProductListViets(ListView):
    queryset = Product.objects.all()
    template_name = 'product_list.html'
    context_object_name = "products"

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    template_name = 'product_create.html'
    form_class = ProductFilter
    success_url = reverse_lazy('product_list')



class ProductUpdteView(UpdateView):
    queryset = Product.objects.all()
    template_name = 'product_update.html'
    form_class = ProductFilter
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    queryset = Product.objects.all()
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
