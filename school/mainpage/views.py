from django.shortcuts import redirect, render


from django.views.decorators.http import require_http_methods


from mainpage.forms import ContactForm


# Create your views here.

# path('', views.index),
@require_http_methods(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainpage:index')

    form = ContactForm()
    context = {'form': form, 'title': 'Contact form'}
    return render(request, 'mainpage/index.html', context)
