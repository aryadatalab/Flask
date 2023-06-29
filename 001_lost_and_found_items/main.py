from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# Define a list to store found items
found_items = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        # Retrieve data from the form
        item_name = request.form['item_name']
        item_description = request.form['item_description']
        contact_info = request.form['contact_info']

        # Create a dictionary to store the item details
        item = {
            'name': item_name,
            'description': item_description,
            'contact': contact_info
        }

        # Add the item to the found_items list
        found_items.append(item)

        # Write the item details to a text file
        with open('items.txt', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([item_name, item_description, contact_info])

        return render_template('success.html', item_name=item_name)
    else:
        return render_template('report.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        # Retrieve the search query from the form
        search_query = request.form['search_query']

        # Filter the found_items list based on the search query
        results = []
        for item in found_items:
            if search_query.lower() in item['name'].lower():
                results.append(item)

        return render_template('search_results.html', results=results)
    else:
        return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)
