from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required




def product_list(request):
    search_query = request.GET.get('search')
    products = Product.objects.all()
    if search_query:
        products = products.filter(Q(name__icontains=search_query))
    paginator = Paginator(products, 8)  # Show 8 products per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products/product_list.html', {'page_obj': page_obj,'products': products})


@login_required
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user.is_superuser:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                return redirect('product-list')
        else:
            form = ProductForm(instance=product)
        return render(request, 'products/update_product.html', {'form': form})
    else:
        return redirect('product_list')
    

@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user.is_superuser:
        if request.method == 'POST':
            product.delete()
            return redirect('product-list')
        return render(request, 'products/delete_product.html', {'product': product})
    else:
        return redirect('product-list')


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})


@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})


# products/views.py
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from account.models import CustomUser
import io
from datetime import datetime
from django.conf import settings

@login_required
def generate_invoice(request, pk):
    product = get_object_or_404(Product, pk=pk)
    user = request.user

    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Draw things on the PDF. Here's where the PDF generation happens.
    p.setFont("Helvetica-Bold", 20)
    p.drawString(100, height - 50, "Invoice")

    p.setFont("Helvetica", 12)
    p.drawString(100, height - 80, f"Date: {datetime.now().strftime('%Y-%m-%d')}")
    p.drawString(100, height - 120, f"Name: {user.fullname}")
    p.drawString(100, height - 140, f"Email: {user.email}")
    p.drawString(100, height - 160, f"Phone: {user.phone}")
    p.drawString(100, height - 180, f"Address: {user.address}")

    # Product details
    p.drawString(100, height - 220, "Product Details:")
    p.drawString(100, height - 240, f"Name: {product.name}")
    p.drawString(100, height - 260, f"Description: {product.description}")
    p.drawString(100, height - 280, f"Cost Price: ${product.cost_price}")
    p.drawString(100, height - 300, f"Sales Price: ${product.sales_price}")
    p.drawString(100, height - 320, f"Discount: {product.discount}%")

    # Draw the product image
    if product.image:
        image_path = f"{settings.MEDIA_ROOT}/{product.image.name}"
        p.drawImage(image_path, 100, height - 520, width=2*inch, height=2*inch)

    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')
