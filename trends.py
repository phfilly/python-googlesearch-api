from pytrends.request import TrendReq


def retrieveData(value):
    pytrend = TrendReq()
    kw_list = [value]
    pytrend.build_payload(kw_list, cat=0, geo='ZA', gprop='', timeframe='now 7-d')
    interest_over_time_df = pytrend.interest_over_time()
    interest_by_region_df = pytrend.interest_by_region()

    return [interest_over_time_df, interest_by_region_df]

