import socket

import pytrends
import requests
import urllib3
from pytrends.request import TrendReq
import pandas as pd
import pprint


def connect_to_pytrends():
    try:
        pytrend = TrendReq(hl='en-US', tz=360)
        # pytrend.build_payload(kw_list, cat=cat, timeframe=timeframe, geo=geo, gprop=gprop)
        return pytrend
    except AttributeError:
        print('pytrend id none')
        return None
    except Exception as e:
        print('Exception in pytrends connection=> ', e)
        return None


def get_historical_interest_amira(**kwargs):
    pytrend = connect_to_pytrends(kw_list=kwargs.get('kw_list'), geo=kwargs.get('geo'), cat=kwargs.get('cat'),
                                  timeframe=kwargs.get('timeframe'))
    if pytrend:
        try:
            # pytrend = TrendReq()
            historical_interest = pytrend.get_historical_interest(kwargs.get('kw_list'),
                                                                  year_start=kwargs.get('year_start'),
                                                                  month_start=kwargs.get('month_start'),
                                                                  day_start=kwargs.get('day_start'),
                                                                  hour_start=kwargs.get('hour_start'),
                                                                  year_end=kwargs.get('year_end'),
                                                                  month_end=kwargs.get('month_end'),
                                                                  day_end=kwargs.get('day_end'),
                                                                  hour_end=kwargs.get('hour_end'))
            # save datetime and trends number
            historical_interest_json = pd.DataFrame.to_json(historical_interest, orient='columns')
            return historical_interest_json
        except requests.exceptions.ConnectionError:
            print('ConnectionError')
            return {}
        except requests.exceptions.ReadTimeout:
            print('ReadTimeout')
            return {}
        except urllib3.exceptions.ReadTimeoutError:
            print('ReadTimeoutError')
            return {}
        except socket.timeout:
            print('timeout')
            return {}


# x = get_historical_interest_amira(kw_list=['wild cat'], year_start=2021, month_start=2, day_start=6, hour_start=0,
#                                   year_end=2021, month_end=2, day_end=10, hour_end=0, cat=0, timeframe='today 5-y',
#                                   geo='',
#                                   gprop='')
# print('x => ', x)
print('------------------------------------------------------------------------')

try:
    pytrend = connect_to_pytrends()
    if pytrend:
        pytrend.build_payload(['wild cats'], cat=0, timeframe='today 5-y', geo='', gprop='')
        interest_by_region=pytrend.interest_by_region(resolution='REGION', inc_low_vol=True, inc_geo_code=True)
        ibr_ten_largest=interest_by_region.nlargest(10,'wild cats')
        print(ibr_ten_largest)
except requests.exceptions.ConnectionError:
    print('ConnectionError')
except requests.exceptions.ReadTimeout:
    print('ReadTimeout')

except socket.timeout:
    print('timeout')
except pytrends.exceptions.ResponseError:
    print('ResponseError')



