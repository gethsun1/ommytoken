from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('invoice_form.html')

@app.route('/generate_invoice', methods=['POST'])
def generate_invoice():
    # Retrieve form data using request.form
    # Perform calculations and generate the invoice

    # Example calculation
    item_price = 10
    quantity = 5
    total = item_price * quantity

    # Return a rendered template with the calculated total
    return render_template('invoice.html', total=total)

if __name__ == '__main__':
    app.run(debug=True)
