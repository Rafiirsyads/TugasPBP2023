from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Book',
        'amount': '5',
        'description': 'Encyclopedia'
    }

    return render(request, "main.html", context)