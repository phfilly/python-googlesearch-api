import pprint
import environment
import database
import trends
import datetime

from googleapiclient.discovery import build
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def main():
    service = build(
        "customsearch",
        "v1",
        developerKey=environment.key)

    res = service.cse().list(
      q='mercedes',
      cx=environment.cxId,
    ).execute()
    return render_template('index.html', data=res)


@app.route('/trends')
def trending():
    iotData = trends.interestOverTime("Russian Bear Vodka")
    values = []
    data = {}
    dates = []
    provinces = []
    province_value = []

    data = iotData.groupby(iotData.index.date).sum()
    for index, row in data.iterrows():
        dates.append(index.strftime("%Y-%m-%d"))
        values.append(row[0])

    regionData = trends.interestByRegion("Russian Bear Vodka")
    for index, row in regionData.iterrows():
        provinces.append(index)
        province_value.append(row[0])

    return render_template('trends.html', values=values, dates=dates, data=data, term="Russian Bear Vodka", provinces=provinces, province_value=province_value)


@app.route('/read')
def read():
    conn = database.connect()
    cur = conn.cursor()
    before = datetime.datetime.now()
    cur.execute("SELECT * FROM public.community where brand = 'REMY_MARTIN'")
    rows = cur.fetchall()
    after = datetime.datetime.now()
    return render_template('read.html', data=rows, length=len(rows), before=before, after=after)


if __name__ == '__main__':
    main()
