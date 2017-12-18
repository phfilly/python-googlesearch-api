from pytrends.request import TrendReq


def interestOverTime(value):
    pytrend = TrendReq()
    kw_list = [value]
    pytrend.build_payload(kw_list, cat=0, geo='ZA', gprop='', timeframe='now 7-d')
    interest_over_time_df = pytrend.interest_over_time()
    return interest_over_time_df


def interestByRegion(value):
    pytrend = TrendReq()
    kw_list = [value]
    pytrend.build_payload(kw_list, cat=0, geo='ZA', gprop='', timeframe='now 7-d')
    interest_by_region_df = pytrend.interest_by_region()
    return interest_by_region_df
