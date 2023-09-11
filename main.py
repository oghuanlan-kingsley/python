from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import pytz

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def get_info():
    # Get parameters from the query string
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get the current day of the week
    current_day = datetime.now().strftime('%A')

    # Get the current UTC time with validation of +/-2 hours
    utc_time = datetime.now(pytz.utc)
    utc_time_str = utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    # Get the GitHub URL of the file being run and the full source code URL
    github_file_url = 'https://github.com/username/repo/blob/main/app.py'
    github_repo_url = 'https://github.com/username/repo'

    # Create the response JSON
    response = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': utc_time_str,
        'track': track,
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
        'status_code': 200
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
