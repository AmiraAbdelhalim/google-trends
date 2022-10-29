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
        return {}
    except Exception as e:
        print('Exception in pytrends connection=> ', e)
        return {}


def get_historical_interest_api(**kwargs):
    pytrend = connect_to_pytrends()
    if pytrend:
        try:
            kw = kwargs.get('kw_list')
            historical_interest = pytrend.get_historical_interest(kw,
                                                                  year_start=kwargs.get('year_start'),
                                                                  month_start=kwargs.get('month_start'),
                                                                  day_start=kwargs.get('day_start'),
                                                                  hour_start=kwargs.get('hour_start'),
                                                                  year_end=kwargs.get('year_end'),
                                                                  month_end=kwargs.get('month_end'),
                                                                  day_end=kwargs.get('day_end'),
                                                                  hour_end=kwargs.get('hour_end'))
            historical_interest = historical_interest.reset_index()
            historical_interest_json = pd.DataFrame.to_json(historical_interest, orient='columns')
            return historical_interest_json
        except requests.exceptions.ConnectionError:
            return {
                'error': True,
                'msg': 'connection error'
            }
        except requests.exceptions.ReadTimeout:
            return {
                'error': True,
                'msg': 'read timeout error'
            }
        except urllib3.exceptions.ReadTimeoutError:
            return {
                'error': True,
                'msg': 'read timeout error'
            }
        except socket.timeout:
            return {
                'error': True,
                'msg': 'socket time out error'
            }
        except Exception as e:
            return {
                'error': True,
                'msg': 'something went wrong'
            }


# send keyword and resolution type
def get_interests_by_region(keywords, resolution, largest_regions_len=10):
    pytrend = connect_to_pytrends()
    if pytrend:
        try:
            print('before => ', pytrend)
            pytrend.build_payload(keywords)
            interest_by_region = pytrend.interest_by_region(resolution=resolution)
            largest_region = interest_by_region.nlargest(largest_regions_len, keywords)
            print(largest_region)
            regions_json = pd.DataFrame.to_json(largest_region, orient='columns')
            print('j => ', regions_json)
            return regions_json

        except requests.exceptions.ConnectionError:
            print('ConnectionError')
            return {
                'error': True,
                'msg': 'AttributeError'
            }
        except requests.exceptions.ReadTimeout:
            print('ReadTimeout')
            return {
                'error': True,
                'msg': 'AttributeError'
            }
        except socket.timeout:
            print('timeout')
            return {
                'error': True,
                'msg': 'AttributeError'
            }
        except pytrends.exceptions.ResponseError:
            print('ResponseError')
            return {
                'error': True,
                'msg': 'AttributeError'
            }
        except AttributeError:
            print('AttributeError')
            return {
                'error': True,
                'msg': 'AttributeError'
            }
        except Exception as e:
            print('get_interests_by_region => ', e)
            return {
                'error': True,
                'msg': 'something went wrong'
            }