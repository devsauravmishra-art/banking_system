from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample endpoint for account creation
@app.route('/create_account', methods=['POST'])
def create_account():
    data = request.json
    return jsonify({"message": "Account created", "account": data}), 201

# Sample endpoint for checking balance
@app.route('/check_balance/<account_id>', methods=['GET'])
def check_balance(account_id):
    # Sample balance data
    balance = 1000.00  # This would normally come from a database
    return jsonify({"account_id": account_id, "balance": balance})

# Sample endpoint for making a deposit
@app.route('/deposit/<account_id>', methods=['POST'])
def deposit(account_id):
    data = request.json
    return jsonify({"message": "Deposit successful", "account_id": account_id, "amount": data['amount']}), 200

if __name__ == '__main__':
    app.run(debug=True)