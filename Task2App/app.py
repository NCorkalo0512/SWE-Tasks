from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/detect-unauthorized-sales', methods=['POST'])
def detect_unauthorized_sales():
    data = request.get_json()

    # Provjera valjanosti ulaznih podataka
    if not data or 'productListings' not in data or 'salesTransactions' not in data:
        return jsonify({'error': 'Bad Request', 'message': 'Invalid data'}), 400
    
    product_listings = data['productListings']
    sales_transactions = data['salesTransactions']

    # Kreiran direktorij za autorizirane prodavace za svaki proizvod
    authorized_sellers = {listing['productID']: listing['authorizedSellerID'] for listing in product_listings}

    # Inicijalizacija strukture za praćenje neovlaštenih prodaja
    unauthorized_sales_dict = {}

    # Pregledati svaku transakciju je li autorizirana odnosno neautorizirana
    for transaction in sales_transactions:
        product_id = transaction['productID']
        seller_id = transaction['sellerID']
        
        # Ukoliko prodavac nije autorizirani prodavac, onda je neautorizirana prodaja
        if authorized_sellers.get(product_id) != seller_id:
            if product_id not in unauthorized_sales_dict:
                unauthorized_sales_dict[product_id] = {'productID': product_id, 'unauthorizedSellerIDs': [seller_id]}
            elif seller_id not in unauthorized_sales_dict[product_id]['unauthorizedSellerIDs']:
                unauthorized_sales_dict[product_id]['unauthorizedSellerIDs'].append(seller_id)

  
    unauthorized_sales = list(unauthorized_sales_dict.values())

    return jsonify({'unauthorizedSales': unauthorized_sales}), 200

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal Server Error', 'message': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)