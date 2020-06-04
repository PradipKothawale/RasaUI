from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/docs")
def hello_docs():
    return render_template('index_doc.html')

@app.route("/send_receive")
def send_receive():
    return render_template('send_and_receive_message.html')

@app.route("/send_receive_examples")
def send_receive_examples():
    return render_template('send_and_receive_message_examples.html')

@app.route("/health")
def health():
    return render_template('check_health_of_bot.html')

@app.route("/insurance_ref")
def insurance_ref():
    return render_template('parse_insurance_document_and_get_reference.html')

@app.route("/insurance_data")
def insurance_data():
    return render_template('get_result_of_parsed_insurance_document.html')

@app.route("/insurance_data_error")
def insurance_data_error():
    return render_template('get_error_result_of_parsed_insurance_document.html')

@app.route("/auth_token")
def auth_token():
    return render_template('get_auth_token.html')

@app.route("/auth_token_error")
def auth_token_error():
    return render_template('get_error_result_of_auth_token.html')

@app.route("/auth_token_error_missing")
def auth_token_error_missing():
    return render_template('get_error_missing_token.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)