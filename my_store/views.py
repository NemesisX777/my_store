from django.shortcuts import redirect


def redirect_root(request):
    return redirect('all_products_url')
