import pprint
import environment

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


if __name__ == '__main__':
    main()
