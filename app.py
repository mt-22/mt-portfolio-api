from flask import Flask, request
from flask_mail import Mail, Message
from flask_cors import CORS
from flask.json import jsonify
from config import ApplicationConfig
from email_validator import validate_email, EmailNotValidError

app = Flask(__name__)
app.config.from_object(ApplicationConfig)
mail = Mail(app)
CORS(app, supports_credentials=True, resources={r"*": {"origins": "https://marshalltaylor.org"}})
# CORS(app, supports_credentials=True, resources={r"*": {"origins": "*"}})


@app.route('/contact', methods=['POST'])
def contact():
    print(request.environ)
    # if 'HTTP_ORIGIN' in request.environ and request.environ['HTTP_ORIGIN'] == "http://localhost:3000":
    if 'HTTP_ORIGIN' in request.environ and request.environ['HTTP_ORIGIN'] == "https://marshalltaylor.org":
        data = request.json
        name = data['name']
        email = data['email']
        body = data['body']
        try :
            emailInfo = validate_email(email, check_deliverability=False)
            email = emailInfo.normalized
            msg = Message(f"Message from {name}", sender='mdtaylor.portfolio@gmail.com', recipients = ['mdtaylor.portfolio@gmail.com'])
            msg.body = (
            f"""Name: {name}
    Email: {email}

    {body}""")
            mail.send(msg)
            return jsonify({
            "status": "OK"
        })
        except EmailNotValidError as e:
            return jsonify({
                "status": str(e)
            }), 401
    else:
        print('invalid origin')
        return "invalid origin"

### DEBUG
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)