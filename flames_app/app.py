from flask import Flask, render_template, request, jsonify, url_for
from flames_app.database import init_db, create_note, get_note, verify_password, cleanup_expired_notes

app = Flask(__name__)

# Initialize database on startup
init_db()
cleanup_expired_notes()  # Clean up old notes

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

@app.route('/secret-admirer')
def secret_admirer():
    """
    Learning: This route displays the form to create a secret note
    """
    return render_template('secret_admirer.html')

@app.route('/create-note', methods=['POST'])
def create_secret_note():
    """
    Learning: POST route that handles form submission
    - Gets data from request
    - Creates note in database
    - Returns JSON with the shareable link
    """
    data = request.get_json()
    message = data.get('message')
    password = data.get('password')
    sender_name = data.get('sender_name', 'Someone')
    
    if not message or not password:
        return jsonify({'error': 'Message and password are required'}), 400
    
    if len(message) > 500:
        return jsonify({'error': 'Message too long (max 500 characters)'}), 400
    
    # Create note and get unique ID
    note_id = create_note(message, password, sender_name)
    
    # Generate shareable link
    note_url = url_for('view_note', note_id=note_id, _external=True)
    
    return jsonify({
        'success': True,
        'note_id': note_id,
        'note_url': note_url
    })

@app.route('/note/<note_id>')
def view_note(note_id):
    """
    Learning: Dynamic route with <note_id> parameter
    URL like /note/xK7mP9qR will pass "xK7mP9qR" as note_id
    """
    note = get_note(note_id)
    
    if not note:
        return render_template('note_not_found.html'), 404
    
    return render_template('view_note.html', note_id=note_id)

@app.route('/unlock-note', methods=['POST'])
def unlock_note():
    """
    Learning: Verifies password and returns the secret message
    This is called via AJAX (no page reload)
    """
    data = request.get_json()
    note_id = data.get('note_id')
    password = data.get('password')
    
    if not note_id or not password:
        return jsonify({'error': 'Missing data'}), 400
    
    if verify_password(note_id, password):
        note = get_note(note_id)
        return jsonify({
            'success': True,
            'message': note['message'],
            'sender_name': note['sender_name'],
            'view_count': note['view_count']
        })
    else:
        return jsonify({'success': False, 'error': 'Incorrect password'}), 401

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
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
