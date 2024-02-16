TASK 1-DISPLAY POLYGON ON A MAP

OVERVIEW

This application displays a polygon on a map using the OpenLaysers library, with polygon coordinates fetched from a 'polygon.json' file. It's built with Flask, a Python web framework, and designed to be simple yet functional, showcasing how to work with geographic data in web app.

ASSUMPTIONS

'polygon.json' is in the project root and correctly formatted.
HTML template named 'index.html' in the 'templates' directory, following Flask conventions.

RUNNING APPLICATION

Navigate to your project directory and run flask run or python -m flask run.
If your Flask file has a different name, set FLASK_APP to your file's name before running. Use export FLASK_APP=yourfilename.py on Unix/macOS or set FLASK_APP=yourfilename.py on Windows.
Access the Application: Open http://127.0.0.1:5000/ in a web browser to view the map with the polygon.

APPROACH

The backend servers an HTML page that includes OpenLayers via CDN for map rendering. The polygon data, loaded from 'polygon.json', is passed to the front end where OpenLayers displays the polygon on the map.

FEATURES 

Polygon display based on JSON coordinates
Map centers and zooms to fit the polygon
Responsive map with zoom and pan capabilities

TASK 2-DETECTING UNAUTHORIZED SALES

OVERVIEW

The Unauthorized Sales Detection API is a Flask-based application that identifies unauthorized sales transactions from provided datasets of product listings and sales records. It compares each sales transaction against authorized product listings to flag any sales made by unauthorized sellers.

APPROACH

The solution involves parsing two lists from a POST request: productListings and salesTransactions. productListings contains products along with their authorized seller IDs, while salesTransactions lists actual sales, including seller IDs. The API then cross-references these to identify any sales transactions conducted by sellers not authorized for the given product.

ASSUMPTIONS

The input JSON payload is correctly formatted, with productListings and salesTransactions both present.
Seller IDs in the salesTransactions list are unique per product.
There is a direct one-to-one mapping between a product and its authorized seller.

ERROR HANDLING

The API ensures error handling, returning a 400 Bad Request status code for invalid inputs such as:
 Missing either productListings or salesTransactions in the request body,
 Empty lists for productListings or salesTransactions,
 Mismatched product IDs or seller IDs not found in the listings,

RUNNING THE CODE

After ensuring Flask is installed and your script is ready in the project directory, run the application with flask run. Use a tool like Postman or a curl command in the terminal to send POST requests to the API at http://127.0.0.1:5000/detect-unauthorized-sales.

TASK 3-OPTIMAL JOB INTERVIEW SCHEDULING

OVERVIEW

This API endpoint, '/max-interviews', is designed to help users calculate the maximum number of non-overlapping job interviews they can attend based on the provided start and end times. 

APPROACH

The algorithm implemented to solve this scheduling problem follows a greedy approach. It first sorts the interviews by their end times to always choose the interview that finishes the earliest, allowing for the maximum available time to attend subsequent interviews. This method assumes that moving from one interview to another is instantaneous, provided the next interview starts at the same time or after the previous one ends.

ASSUMPTIONS

The start_times and end_times lists are correctly formatted and of equal length.

Transitioning from one interview to the next requires no time, assuming the next interview starts exactly at or after the previous one ends.

Interviews can be attended back-to-back without any breaks.

ERROR HANDLING

The API ensures error handling, returning a 400 Bad Request status code for invalid inputs such as: 
Missing start_times or end_times in the request body,
Mismatched lengths of start_times and end_times.

RUNNING THE CODE

After ensuring Flask is installed and your script is ready in the project directory, run the application with flask run. Use a tool like Postman or a curl command in the terminal to send POST requests to the API athttp://127.0.0.1:5000/max-interviews
