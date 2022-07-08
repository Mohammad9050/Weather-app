import requests
from django.http import HttpResponseRedirect
from Home.forms import get_city
from django.shortcuts import render
from django.urls import reverse
from Home.models import WeatherList


def weather_show(request):
    context = {}
    wea_count = WeatherList.objects.all().count()

    if request.method == 'POST':
        form = get_city(request.POST)
        if form.is_valid():
            city = form.cleaned_data.get('city')
            city = city.capitalize()
            try:
                url = "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=80a27ba62e0bd286009a18502a117273" \
                      "&units=metric" % city
                j_data = requests.get(url).json()
                code = j_data['cod']
                assert code == 200, 'city not found !'
                assert wea_count <= 5, 'cities are full !'
                assert not WeatherList.objects.filter(city=city), '%s is available' % city
                temp_min = int(j_data['main']['temp_min'])
                temp_max = int(j_data['main']['temp_max'])
                type_weather = j_data['weather'][0]['main']
                temp_main = int(j_data['main']['temp'])
                icon = j_data['weather'][0]['icon']
                WeatherList.objects.create(temp_min=temp_min, temp_max=temp_max, type_weather=type_weather,
                                           temp_main=temp_main, icon=icon, city=city)
            except Exception as e:
                error = str(e)
                context['error'] = error
    else:
        form = get_city()
    weathers = WeatherList.objects.all().order_by('time')
    context['wea_list'] = weathers
    context['form'] = form
    return render(request, 'Weather/home.html', context)


def update_obj(request, num):
    my_list = []
    obj = WeatherList.objects.filter(pk=num)
    for i in obj:
        my_list.append(i.city)
    url = "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=80a27ba62e0bd286009a18502a117273" \
          "&units=metric" % my_list[0]
    j_data = requests.get(url).json()
    temp_min = int(j_data['main']['temp_min'])
    temp_max = int(j_data['main']['temp_max'])
    type_weather = j_data['weather'][0]['main']
    temp_main = int(j_data['main']['temp'])
    icon = j_data['weather'][0]['icon']
    obj.update(temp_min=temp_min, temp_max=temp_max, temp_main=temp_main, type_weather=type_weather, icon=icon)

    return HttpResponseRedirect(reverse("Home:home"))


def delete_obj(request, num):
    WeatherList.objects.filter(pk=num).delete()
    return HttpResponseRedirect(reverse("Home:home"))
