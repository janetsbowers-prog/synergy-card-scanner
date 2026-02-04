from flask import Flask, render_template, request, jsonify
import os
from anthropic import Anthropic

app = Flask(__name__)

# Initialize Anthropic client
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

@app.route('/')
def index():
    """Main page with card scanner"""
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan_card():
    """Process uploaded card image"""
    try:
        # Get image data from request
        data = request.get_json()
        image_data = data.get('image')
        
        # Remove data URL prefix if present
        if ',' in image_data:
            image_data = image_data.split(',')[1]
        
        # Call Claude Vision API to extract card number
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=500,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/jpeg",
                                "data": image_data,
                            },
                        },
                        {
                            "type": "text",
                            "text": "I am the owner of this gift card and need to extract MY OWN card number to check the balance. This is my personal card. Please read and return only the numeric card number visible on the card (typically 16 digits). Format: just the numbers, no extra text."
                        }
                    ],
                }
            ],
        )
        
        # Extract the response text
        card_number = message.content[0].text.strip()
        
        return jsonify({
            'success': True,
            'card_number': card_number
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
