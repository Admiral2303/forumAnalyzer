import operator

from flask import Flask, render_template, request
from grabber.database.messageDB import ForumDatabase

db = ForumDatabase()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('titles.html', titles=db.get_titles())


@app.route('/titles/<title_id>', methods=['GET'])
def title(title_id):
    author_mess_count = db.get_messages_count(title_id)
    max_mess_count = max(author_mess_count.items(), key=operator.itemgetter(1))[0]
    max_count = author_mess_count[max_mess_count]
    title_url = db.get_title_by_id(title_id)['url']
    title_name = db.get_title_by_id(title_id)['name']
    return render_template('title_statistic.html',
                           max_amount=max_count,
                           title_url=title_url,
                           title_name=title_name,
                           author_mess_count=author_mess_count, )


if __name__ == '__main__':
    app.run(port=3001)
