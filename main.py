import environment
import database
import trends
import datetime

from googleapiclient.discovery import build
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', data='please select a term in the address bar')


@app.route('/<term>')
def main(term):
    service = build(
        "customsearch",
        "v1",
        developerKey=environment.key)

    res = service.cse().list(
      q=term,
      cx=environment.cxId,
    ).execute()
    return render_template('index.html', data=res)


@app.route('/trends/<term>')
def trending(term):
    iotData = trends.retrieveData(term)
    values = []
    data = {}
    dates = []
    provinces = []
    province_value = []

    data = iotData[0].groupby(iotData[0].index.date).sum()
    for index, row in data.iterrows():
        dates.append(index.strftime("%Y-%m-%d"))
        values.append(row[0])

    regionData = iotData[1]
    for index, row in regionData.iterrows():
        provinces.append(index)
        province_value.append(row[0])

    return render_template('trends.html', values=values, dates=dates, data=data, term=term, provinces=provinces, province_value=province_value)


@app.route('/read')
def read():
    conn = database.connect()
    cur = conn.cursor()
    community = query(cur, 'Community', environment.community)
    topEngagers = query(cur, 'Top Engagers', environment.topEngagers)
    # topInfluencers = query(cur, 'Engagers', "select * from ")

    return render_template('read.html', data=[community, topEngagers])


def query(cur, name, query):
    start = datetime.datetime.now()
    cur.execute(query)
    rows = cur.fetchall()
    end = datetime.datetime.now()

    return [end-start, rows, name, len(rows)]

if __name__ == '__main__':
    main()
