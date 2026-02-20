from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime
import sqlite3
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)

# Database setup
conn = sqlite3.connect('health_data.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users 
             (id TEXT PRIMARY KEY, history TEXT, wellness TEXT, timestamp TEXT)''')
conn.commit()

HEALTH_RULES = {
    'high_bp': ['🥄 Reduce salt intake significantly', '🏃‍♂️ Exercise 30min daily (walking/brisk)', '📊 Monitor BP weekly at home', '🍎 Focus on potassium-rich foods (bananas, spinach)'],
    'low_activity': ['🚶 Walk 10k steps daily (track with phone)', '🧘‍♀️ Yoga/stretching 3x/week (15min sessions)', '💧 Hydrate 3L water/day', '⏰ Take 5min walk every hour at work'],
    'poor_sleep': ['😴 Aim 7-9 hours/night consistently', '📱 No screens 1hr before bed', '🛌 Same bedtime every night', '☕ No caffeine after 2pm']
}

def compress_data(history, wellness):
    """Compress using ScaleDown package with better error handling."""
    full_text = f"Medical history: {history}\nWellness data: {wellness}"
    
    # Simple length-based compression as fallback
    if len(full_text) < 50:
        return full_text, {'savings_percent': 0, 'status': 'too_short'}
    
    try:
        # Try multiple import methods
        try:
            from scaledown.optimizer import HasteOptimizer
            optimizer = HasteOptimizer(top_k=3, bfs_depth=1)
            result = optimizer.optimize(context=full_text, query="wellness recommendations")
            compressed = result.content
        except:
            try:
                from scaledown import optimize
                compressed = optimize(full_text)
            except:
                from scaledown.tools import tools
                optimizer = tools(llm='gpt-4o-mini', optimiser='cot')['optimizer']
                compressed = optimizer(full_text)
        
        original_len = len(full_text)
        compressed_len = len(compressed)
        savings_percent = max(0, int((1 - compressed_len/original_len) * 100))
        
        print(f"✅ ScaleDown SUCCESS: {savings_percent}% ({original_len}→{compressed_len} chars)")
        return compressed, {'savings_percent': savings_percent, 'status': 'success'}
        
    except Exception as e:
        print(f"⚠️ ScaleDown failed ({str(e)[:50]}...) - using smart truncation")
        
        # SMART FALLBACK: Keep key medical terms, truncate rest
        words = full_text.split()
        key_terms = ['hypertension', 'diabetes', 'sleep', 'sedentary', 'bp', 'insomnia']
        important_words = [w for w in words if any(kt in w.lower() for kt in key_terms)]
        truncated = ' '.join(words[:30] + important_words[:5])
        
        savings_percent = max(0, int((1 - len(truncated)/len(full_text)) * 100))
        print(f"✅ Smart Truncation: {savings_percent}% ({len(full_text)}→{len(truncated)})")
        
        return truncated, {'savings_percent': savings_percent, 'status': 'smart_truncation'}

def generate_recommendations(compressed_data, user_id):
    """Smart symptom detection + recommendations."""
    data_lower = compressed_data.lower()
    symptoms = []
    
    # Hypertension detection
    if any(word in data_lower for word in ['hypertension', 'high blood pressure', 'bp 140', 'bp 150', 'blood pressure high']):
        symptoms.append('high_bp')
    
    # Low activity detection
    if any(word in data_lower for word in ['sedentary', 'no exercise', 'desk job', 'sitting 8', 'sitting 10', 'inactive']):
        symptoms.append('low_activity')
    
    # Poor sleep detection
    if any(word in data_lower for word in ['insomnia', 'poor sleep', 'sleep 5', 'sleep 4', 'sleepless', 'fatigue']):
        symptoms.append('poor_sleep')
    
    recs = []
    for sym in symptoms:
        recs.extend(HEALTH_RULES.get(sym, ['👩‍⚕️ Consult healthcare professional']))
    
    if not recs:
        recs = ['🥗 Maintain balanced diet rich in vegetables/fruits', '🏃‍♂️ Regular moderate exercise (30min/day)', '😴 Prioritize 7-9 hours quality sleep', '👩‍⚕️ Schedule regular health checkups']
    
    return recs[:5]  # Limit to top 5

@app.route('/add_data', methods=['POST'])
def add_data():
    try:
        data = request.json
        user_id = data.get('user_id')
        history = data.get('history', '')
        wellness = data.get('wellness', '')
        timestamp = datetime.now().isoformat()
        
        if not user_id:
            return jsonify({'error': 'User ID required'}), 400
            
        c.execute("INSERT OR REPLACE INTO users VALUES (?, ?, ?, ?)", 
                 (user_id, history, wellness, timestamp))
        conn.commit()
        return jsonify({'status': 'Data stored successfully', 'user_id': user_id})
    except Exception as e:
        return jsonify({'error': f'Storage error: {str(e)}'}), 500

@app.route('/get_recommendations/<user_id>', methods=['GET'])
def get_recs(user_id):
    try:
        c.execute("SELECT history, wellness FROM users WHERE id=?", (user_id,))
        row = c.fetchone()
        if not row:
            return jsonify({'error': 'No data found for this user. Add data first.'}), 404
        
        history, wellness = row
        compressed, metrics = compress_data(history, wellness)
        recs = generate_recommendations(compressed, user_id)
        
        print(f"🎯 Recommendations for {user_id}: {len(recs)} items, Savings: {metrics.get('savings_percent',0)}%")
        
        return jsonify({
            'recommendations': recs,
            'compressed_data': compressed,
            'metrics': metrics,
            'savings_percent': metrics.get('savings_percent', 0),
            'compression_status': metrics.get('status', 'unknown')
        })
    except Exception as e:
        print(f"❌ Backend error: {str(e)}")
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Test endpoint - shows API status."""
    try:
        import scaledown
        package_status = f"✅ v{scaledown.__version__}"
    except ImportError:
        package_status = "❌ NOT INSTALLED"
    
    return jsonify({
        'backend_status': 'running',
        'port': 5000,
        'scaledown_package': package_status,
        'database': 'connected'
    })

if __name__ == '__main__':
    print("🚀 Health Agent Backend Starting...")
    try:
        import scaledown
        print("✅ ScaleDown PACKAGE: INSTALLED ✓")
    except ImportError:
        print("⚠️ ScaleDown PACKAGE: MISSING - install with 'pip install scaledown'")
    print("🌐 APIs ready: http://localhost:5000/health")
    app.run(debug=True, port=5000)
