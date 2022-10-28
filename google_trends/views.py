import json

from django.shortcuts import render
from .google_pytrends import get_historical_interest_api
import datetime
from .models import HistoricalInterestKeyWord, HistoricalInterest


# Create your views here.
def search_trends(request):
    today = datetime.datetime.now()
    if request.method == "POST":
        date_start = get_date_values(request.POST.get('start_date'), 'start') if request.POST.get('start_date') else ''
        date_end = get_date_values(request.POST.get('end_date'), 'end') if request.POST.get('end_date') else ''
        hour_start = get_hour_value(request.POST.get('start_time'), 'start') if request.POST.get('start_time') else ''
        hour_end = get_hour_value(request.POST.get('end_time'), 'end') if request.POST.get('end_time') else ''

        kw_list = [request.POST.get('kw_list')]
        year_start = date_start.get('year_start') if date_start else today.year
        month_start = date_start.get('month_start') if date_start else today.month
        day_start = date_start.get('day_start') if date_start else today.day

        hour_start = hour_start.get('hour_start') if hour_start else 0

        year_end = date_end.get('year_end') if date_end else today.year
        month_end = date_end.get('month_end') if date_end else today.month
        day_end = date_end.get('day_end') if date_end else today.day

        hour_end = hour_end.get('hour_end') if hour_end else 0

        historical_data = get_historical_interest_api(kw_list=kw_list, year_start=year_start, month_start=month_start,
                                                      day_start=day_start, hour_start=hour_start, year_end=year_end,
                                                      month_end=month_end, day_end=day_end, hour_end=hour_end)

        if historical_data:
            print('historical_data => ', historical_data)
            kw = HistoricalInterestKeyWord.objects.create(search_keyword=kw_list[0])
            kw.save()
            historical_data = json.loads(historical_data)
            list_of_dates = []
            list_of_trends = []
            list_of_partials = []
            historical_data_dic = {}
            for record in historical_data:
                if record == 'date':
                    print(historical_data[record])
                    list_of_dates = list(historical_data[record].values())
                if record == 'isPartial':
                    list_of_partials = list(historical_data[record].values())
                if record == kw_list[0]:
                    list_of_trends = list(historical_data[record].values())

            for index in range(len(list_of_dates)):
                historical_data_dic['date_time'] = datetime.datetime.fromtimestamp(list_of_dates[index] / 1e3)
                historical_data_dic['trends'] = list_of_trends[index]
                historical_data_dic['is_partial'] = list_of_partials[index]
                if kw:
                    interests = HistoricalInterest.objects.create(search_key=kw, **historical_data_dic)
                    interests.save()
    return render(request, 'google_trends/trends.html', {})


def get_date_values(date, key):
    date_dict = dict()
    split_dates = date.split('-')
    if key == 'start':
        date_dict['year_start'] = int(split_dates[0])
        date_dict['month_start'] = int(split_dates[1])
        date_dict['day_start'] = int(split_dates[2])
        return date_dict
    elif key == 'end':
        date_dict['year_end'] = int(split_dates[0])
        date_dict['month_end'] = int(split_dates[1])
        date_dict['day_end'] = int(split_dates[2])
        return date_dict


def get_hour_value(time, key):
    split_time = time.split(':')
    time_dict = dict()
    if key == 'start':
        time_dict['hour_start'] = int(split_time[0])
        return time_dict
    elif key == 'end':
        time_dict['hour_end'] = int(split_time[0])
        return time_dict
