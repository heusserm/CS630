#stand_up_api_word_count.py
# An Application that stands up a REST API library 
# For CS630, week 4, Assignment 2, SNHU
# By Matthew Heusser M.Heusser@snhu.edu Jun 2025
# 
# To use:
#  python3 stand_up_api_word_count.py
#
# The server will run on port 5042, mostly because it is assignment 4-2
#
# Sample browser URL to test:
#  http://localhost:5042/count?text=Hello%20world%20from%20browser
#
#  (You'll get a result of 4)
#
#  Sample curl command to test:
#   curl -G "http://localhost:5042/count" --data-urlencode "text=Hello world from curl"
#
#   
#----------------------------------------------------------#

from flask import Flask, request, jsonify
from word_count import count_words

app = Flask(__name__)

# Support GET and POST on both /count and /count/
@app.route('/count', methods=['GET', 'POST'], strict_slashes=False)
@app.route('/count/', methods=['GET', 'POST'], strict_slashes=False)
def count_endpoint():
    """
    GET  /count?text=your+string
    POST /count with JSON { "text": "your input string" }

    Response JSON: { "count": <number of words> }
    """
    # Handle GET
    if request.method == 'GET':
        text = request.args.get('text')
        if text is None:
            return jsonify(error="Missing 'text' query parameter"), 400
    # Handle POST
    else:
        data = request.get_json(force=True, silent=True)
        if not data or 'text' not in data:
            return jsonify(error="Missing 'text' parameter"), 400
        text = data['text']

    try:
        count = count_words(text)
    except Exception as e:
        return jsonify(error=str(e)), 500

    return jsonify(count=count)

if __name__ == '__main__':
    # macOS: disable reloader to avoid multiprocessing issues
    app.run(host='0.0.0.0', port=5042, debug=True, use_reloader=False)


