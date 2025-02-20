from flask import Flask, render_template, request
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify

# Configure Gemini AI
genai.configure(api_key='AIzaSyBfLgClw1r2Qd3Ps1GhOThHn_P0eOeo-tw')


app = Flask(__name__)

# Function to calculate match percentage based on vowels



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/aimatch')
def ai_match():
    return render_template('aimatch.html')

@app.route('/loveletter')
def loveletter():
    return render_template('loveletter.html')

@app.route('/pickup')
def pickup():
    return render_template('pickup.html')

@app.route('/poem')
def poem():
    return render_template('poem.html')

@app.route('/respond')
def respond():
    return render_template('respond.html')

@app.route('/bot')
def bot():
    return render_template('bot.html')

@app.route('/match')
def match():
    return render_template('match.html')



@app.route('/generate_poem', methods=['POST'])
def generate_poem():
    try:
        data = request.json
        crush_name = data.get("crushName")
        traits = data.get("traits")

        if not crush_name or not traits:
            return jsonify({"error": "Missing required fields"}), 400

        # Generate a romantic poem using Gemini AI
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Write a short romantic poem about someone named {crush_name}. They are {traits}. Make it heartwarming and poetic and rhyming and cute."
        
        response = model.generate_content(prompt)

        return jsonify({"poem": response.text.strip()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/generate_letter', methods=['POST'])
def generate_letter():
    try:
        data = request.json
        your_name = data.get("yourName")
        crush_name = data.get("crushName")
        traits = data.get("traits")

        if not your_name or not crush_name or not traits:
            return jsonify({"error": "Missing required fields"}), 400

        # Generate a romantic love letter using Gemini AI
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"""
        Write a heartfelt love letter from {your_name} to {crush_name}.
        {crush_name} is described as {traits}.
        Make it emotional, sweet, poetic, and passionate. It must be a proposal like asking to be my valentine.It must be of 3 paragraph.Reduce the no.of sentences in each paragraph. Make the letter short and cute . Only cheesy lines.
        End the letter with: 'With all my love, {your_name}'.
        """

        response = model.generate_content(prompt)

        # Ensure response is valid
        if not response or not hasattr(response, "text") or not response.text:
            return jsonify({"error": "Failed to generate letter"}), 500

        return jsonify({"letter": response.text.strip()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


PICKUP_LINES = [
    "Are you a magician? Because whenever I look at you, everyone else disappears. ✨",
    "Are you a WiFi signal? Because I'm feeling a strong connection! 📶",
    "Are you an exam? Because I’ve been studying you all night. 📚❤️",
    "Do you have a Band-Aid? Because I just scraped my knee falling for you. 😍",
    "Are you made of copper and tellurium? Because you're Cu-Te. 🔬",
    "Are you a keyboard? Because you're just my type. ⌨️💕",
    "I must be a snowflake because I've fallen for you. ❄️💘",
    "Can you lend me a map? I keep getting lost in your eyes. 🗺️👀",
    "Are you a light bulb? Because you brighten up my day. 💡😊",
]

@app.route('/generate_pickup', methods=['GET'])
def generate_pickup():
    return jsonify({"line": random.choice(PICKUP_LINES)})
    
@app.route('/chat_partner_bot', methods=['POST'])
def chat_partner_bot():
    try:
        data = request.json
        user_message = data.get("message")
        partner = data.get("partner")

        if not user_message or not partner:
            return jsonify({"error": "Missing required fields"}), 400

        # Define different personalities
        if partner == "male":
            persona = "You are a cheesy and playful boyfriend who loves teasing and using pickup lines.Give Short one sentenece replies."
        else:
            persona = "You are a cheesy girlfriend who loves romantic conversations and compliments.Give Short one sentenece replies."

        # Generate AI response
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"{persona} The user says: {user_message}. Respond in a cute and romantic way."

        response = model.generate_content(prompt)

        if not response or not hasattr(response, "text") or not response.text:
            return jsonify({"error": "Failed to generate response"}), 500

        return jsonify({"response": response.text.strip()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/generate_response', methods=['POST'])
def generate_response():
    try:
        data = request.json
        crush_message = data.get("crushMessage")

        if not crush_message:
            return jsonify({"error": "Missing required field"}), 400

        # AI Model Prompt
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Your crush just texted: '{crush_message}'. Generate a flirty yet natural response to keep the conversation fun and engaging. Avoid being too over-the-top, but keep it romantic and playful."

        response = model.generate_content(prompt)

        if not response or not hasattr(response, "text") or not response.text:
            return jsonify({"error": "Failed to generate response"}), 500

        return jsonify({"response": response.text.strip()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    app.run(debug=True)
