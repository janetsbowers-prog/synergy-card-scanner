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
                            "text": "Please read the card number from this Synergy gift card image. Look for the long number sequence (usually 16 digits with spaces). Extract and return ONLY the card number digits, nothing else. Even if the image quality isn't perfect, do your best to read the numbers visible on the card."
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
