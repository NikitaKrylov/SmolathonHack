from datetime import date, datetime, timedelta
from typing import Callable
from posts.models import EventPost
from account.models import TravelRoute, TravelRouteDay

from django.contrib.auth.models import User


def generate_travel_route(user: User, from_date: date, to_date: date, gen_func: Callable = None) -> TravelRoute:
    hotel = EventPost.objects.filter(category='Гостинницы').order_by('?').first()
    route = TravelRoute(user=user, from_date=from_date, to_date=to_date)
    route.save()

    bars = set(EventPost.objects.filter(category='Питание', subcategory='Бары').order_by('?'))
    restaurants = set(EventPost.objects.filter(category='Питание', subcategory='Рестораны').order_by('?'))
    other_events = set(EventPost.objects.filter(category='Досуг').order_by('?'))

    first_day = TravelRouteDay(
        route=route,
        day_num=1,
        day_type=TravelRouteDay.DayType.START,
        date=from_date
    )
    first_day.save()
    first_day.events.add(hotel, bars.pop(), other_events.pop())

    for day in range(2, (to_date - from_date).days):
        route_day = TravelRouteDay(
            day_num=day,
            day_type=TravelRouteDay.DayType.MIDDLE,
            route=route,
            date=from_date + timedelta(days=day - 1)
        )
        route_day.save()
        route_day.events.add(restaurants.pop(), other_events.pop(), other_events.pop(), bars.pop())

    last_day = TravelRouteDay(
        route=route,
        day_num=(to_date - from_date).days + 1,
        day_type=TravelRouteDay.DayType.END,
        date=to_date
    )
    last_day.save()
    last_day.events.add(other_events.pop(), bars.pop(), other_events.pop())

    return route
