from flask import Flask, render_template, request , jsonify

import google.generativeai as genai


app = Flask(__name__)
app.secret_key = 'your_secret_key'


API_KEY = 'AIzaSyCnHiPnc81WluNjSklL6lLR5FO_NbHRCfM'
#'AIzaSyCCrYnLhDIgToWeG4u_nPpQcB9uNJMze0U'
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

medical_keywords = [
    "Customer Satisfaction","Order Management","Product Inquiries","Return Process",
    "Shipping Information","Live Chat Support","Help Desk","Ticketing System","Feedback Management",
    "Issue Resolution","Customer Retention","Response Time","Customer Experience",
    "Support Tickets","Service Quality",
    "CRM Integration","Automated Responses",
    "Personalized Support","Resolution Tracking",
    "Customer Escalations","Knowledge Base",
    "Customer Engagement","Proactive Support",
    "Service Level Agreements","Complaint Handling",
    "Support Analytics","Customer Loyalty",
    "Cross-Selling","Upselling","Service Recovery",
    "Technical Support","Account Management",
    "Self-Service Portal","Order Tracking",
    "Customer Journey","Client Relations",
    "Support Workflow","Interaction History","Support Metrics"
]




@app.route('/ask', methods=['POST'])
def ask():
    user_message = str(request.form['messageText'])
    
    if not is_medical_query(user_message):
        bot_response_text = "I'm sorry, I can only answer medical-related questions. Please ask a question related to medical topics."
    else:
        bot_response = chat.send_message(user_message)
        bot_response_text = bot_response.text
    
    return jsonify({'status': 'OK', 'answer': bot_response_text})

def is_medical_query(query):
    return any(keyword in query.lower() for keyword in medical_keywords)


