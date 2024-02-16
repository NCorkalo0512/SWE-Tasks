from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/max-interviews', methods=['POST'])
def max_interviews():
    data = request.json
    start_times = data.get('start_times')
    end_times = data.get('end_times')
    
    if not start_times or not end_times or len(start_times) != len(end_times):
        return jsonify({"error": "Invalid input"}), 400
    
    max_interviews = calculate_max_interviews(start_times, end_times)
    
    return jsonify({"max_interviews": max_interviews}), 200

def calculate_max_interviews(start_times, end_times):
    interviews = sorted(zip(start_times, end_times), key=lambda x: x[1])
    count = 0
    last_end_time = 0
    
    for start, end in interviews:
        if start >= last_end_time:
            count += 1
            last_end_time = end
    
    return count

if __name__ == '__main__':
    app.run(debug=True)