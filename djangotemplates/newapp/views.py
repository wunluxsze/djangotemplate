from django.shortcuts import render

# Create your views here.
def index(request):
    data = {"header": "Алабуга политех, 215-8-2, Программирование JavaScript", "message": "Хочу стать уборщиком туалетов" }
    return render(request, "index.html", context= data)


def about(request):
    data = {"name": "Зубенко Михаил Петрович", "about": "Рост: 310см (в ширину), Вес: 120кг, 22 года"}
    return render(request, "about.html", context= data)

def contact(request):
    data = {"number": "+79373970772", "telegram": "t.me/alwraiz"}
    return render(request, "contact.html", context={"data": data})

def form(request):
    return render(request, "form.html",)
