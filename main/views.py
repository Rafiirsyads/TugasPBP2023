from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Rafi Irsyad Saharso',
        'npm': '2206082221',
        'class': 'A'
    }

    return render(request, "main.html", context)