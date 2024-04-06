from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import SliderItem, Event, Category, Yorumlar
from .forms import SliderItemForm, EventForm, CategoryForm , YorumForm
from django.contrib import messages

def index(request):
    slider_items = SliderItem.objects.all()
    events = Event.objects.all()  # Tüm etkinlikleri al
    categories = Category.objects.all()  # Tüm kategorileri al
    return render(request, "index.html", {'slider_items': slider_items, 'events': events, 'categories': categories})

def event_detail(request, event_id):
    event = Event.objects.get(pk=event_id)
    yorumlar = Yorumlar.objects.filter(event=event)

    if request.method == 'POST':
        form = YorumForm(request.POST)
        if form.is_valid():
            yorum = form.save(commit=False)
            yorum.event = event
            yorum.save()
            return redirect('event_detail', event_id=event_id)
    else:
        form = YorumForm()

    return render(request, 'event_detail.html', {'event': event, 'yorumlar': yorumlar, 'form': form})

def category_events(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    events = Event.objects.filter(category=category)
    return render(request, 'category_events.html', {'category': category, 'events': events})


@login_required
def hesabim(request):
    return render(request, 'hesabim.html')



def slider_item_ekle(request):
    if request.method == 'POST':
        form = SliderItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Slider İtem başarıyla eklendi.')
            return redirect('hesabim')
    else:
        form = SliderItemForm()
    return render(request, 'slider_ekle.html', {'form': form})

def event_ekle(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Etkinlik başarıyla eklendi.')
            return redirect('hesabim')
    else:
        form = EventForm()
    return render(request, 'event_ekle.html', {'form': form})

def category_ekle(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kategori başarıyla eklendi.')
            return redirect('hesabim')
    else:
        form = CategoryForm()
    return render(request, 'kategori_ekle.html', {'form': form})
