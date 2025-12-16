from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def calculate_flames(name1, name2):
    name1_list = list(name1.lower().replace(" ", ""))
    name2_list = list(name2.lower().replace(" ", ""))
    
    # Remove matching characters
    for char in name1_list[:]:
        if char in name2_list:
            name1_list.remove(char)
            name2_list.remove(char)
            
    count = len(name1_list) + len(name2_list)
    
    if count == 0:
        return "No Characters Left", "Try with different names!"
        
    result_list = ['Friendship', 'Love', 'Affection', 'Marriage', 'Enemy', 'Siblings']
    
    while len(result_list) > 1:
        split_index = (count % len(result_list)) - 1
        
        if split_index >= 0:
            right = result_list[split_index + 1:]
            left = result_list[:split_index]
            result_list = right + left
        else:
            result_list = result_list[:len(result_list) - 1]
            
    return result_list[0], f"Your relationship is {result_list[0]}!"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/flames')
def flames_calculator():
    return render_template('flames.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    name1 = data.get('name1')
    name2 = data.get('name2')
    
    if not name1 or not name2:
        return jsonify({'error': 'Both names are required'}), 400
        
    result, message = calculate_flames(name1, name2)
    return jsonify({'result': result, 'message': message})

if __name__ == '__main__':
    app.run(debug=True)
