from flask import Flask, jsonify, request
import utils

app = Flask(__name__)

@app.route('/catalogs/', methods=['GET'])
def get_catalogs():
    rows = utils.get_all('SELECT * FROM catalogs')
    data = []
    for r in rows:
        data.append({
            'id': r[0],
            'name': r[1],
            'url': r[2]
        })

    return jsonify({'catalogs': data})

@app.route('/news', methods=['GET'])
def get_news():
    rows = utils.get_all('SELECT * FROM news')
    data = []
    for r in rows:
        data.append({
            'id': r[0],
            'subject': r[1],
            'description': r[2],
            'image': r[3],
            'ori_url': r[4],
            'catalogy_id': r[5]
        })

    return jsonify({'news': data})

@app.route('/news/<int:new_id>', methods=['GET'])
def get_news_by_id(new_id):
    r = (utils.get_news_by_id(new_id))[0]
    data = {
        'subject': r[0],
        'description': r[1],
        'image': r[2],
        'ori_url': r[3]
    }
    return jsonify({'product': data})

@app.route('/news/<int:news_id>', methods=['POST'])
def insert_comment(news_id):
    if request.form.get('content'):
        utils.add_comment(news_id, request.form['content'])
        return jsonify({'Status': 1, 'Message': 'Success'})

    return jsonify({'Error code': 1, 'message': 'Fail'})

@app.route('/news/add', methods=["POST"])  # Add action ofter is post methods
def insert_news():
    pass

if __name__ == '__main__':
    app.run(debug=True)