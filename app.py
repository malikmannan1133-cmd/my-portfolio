from flask import Flask, render_template
import os

app = Flask(__name__)

projects_data = [
    {
        "title": "E-commerce Sales Analytics",
        "tech": "Python(NumPy,Pandas), MySQL, Power BI",
        "description": "Comprehensive analysis of $7.74M revenue data to identify growth drivers. Developed interactive dashboards to track monthly sales trends.",
        "image_file": "ecomerce.png"
    },
    {
        "title": "HR Employee Analytics",
        "tech": "Power BI,Python(NumPy,Pandas), MySql",
        "description": "Data-driven approach to workforce management. Analyzed employee performance and retention metrics to identify turnover risks.",
        "image_file": "hranalystics.png"
    },
    {
        "title": "Pizza Shop Sales Analysis",
        "tech": "MySQL, Power BI",
        "description": "End-to-end SQL project to track daily sales, customer preferences, and inventory turnover. Optimized order processing insights.",
        "image_file": "pizzasalesproject.png"
    },
    {
        "title": "Medical Whole Sale Analysis",
        "tech": "MySQL,Python(NumPy,Pandas),Power BI",
        "description": "Inventory and supply chain analysis for a medical wholesaler. Used SQL and Python to track stock levels and expiry dates.",
        "image_file": "medicalinventory.png"
    }
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects_data)

# Vercel ke liye ye line zaroori hai
app = app

if __name__ == '__main__':
    app.run(debug=True)