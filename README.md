# **AI Webpage Generator Chatbot**  

  

## **📌 Description**  
The **AI Webpage Generator Chatbot** is a web application that allows users to describe a webpage in natural language, and the system generates the corresponding HTML/CSS code in real time. The chatbot provides an interactive preview and allows users to download the generated webpage.  

Powered by **Hugging Face's AI models**, this tool simplifies web development by converting plain-text descriptions into functional HTML/CSS layouts.  

---

## **✨ Features**  
✔ **AI-Powered HTML Generation** – Converts natural language into working HTML/CSS  
✔ **Live Preview** – Instantly renders the generated webpage  
✔ **Downloadable HTML** – Save the generated code as an `.html` file  
✔ **Responsive UI** – Clean and intuitive chat interface  
✔ **Error Handling** – Graceful fallbacks if AI fails  

---

## **🛠 Tech Stack**  
### **Frontend**  
- **HTML5, CSS3, JavaScript** – Core web technologies  
- **Django Templates** – Dynamic rendering  
- **Font Awesome** – Icons  

### **Backend**  
- **Django (Python)** – Web framework  
- **Hugging Face API** – AI model integration (`Salesforce/codegen2`)  

### **APIs & Services**  
- **Hugging Face Inference API** – For AI-based HTML generation  

### **Deployment (Optional)**  
- **Render / AWS / Heroku** – Cloud hosting  
- **PostgreSQL** – Database (if saving user history)  

---

## **🚀 How It Works**  
1. **User Input** – Describe the webpage you want (e.g., *"Create a blue webpage with a header"*)  
2. **AI Processing** – The backend sends the request to Hugging Face’s AI model  
3. **HTML Generation** – The AI returns clean HTML/CSS code  
4. **Live Preview** – The frontend renders the generated webpage instantly  
5. **Download** – Users can save the HTML file  

---

## **📂 Project Structure**  
```bash
ai-webpage-chatbot/
├── chat/                  # Django app
│   ├── static/            # JS/CSS files
│   ├── templates/         # HTML templates
│   ├── views.py           # AI generation logic
│   └── urls.py            # URL routing
├── chatbot_project/        # Django project config
├── .env                   # API keys & secrets
├── requirements.txt       # Python dependencies
└── README.md              # Documentation
```

---


