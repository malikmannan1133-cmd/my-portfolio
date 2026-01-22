from flask import Flask, render_template

app = Flask(__name__)

# Step 1: Data Setup
# We are creating a list of dictionaries to store your project details.
projects_data = [
    {
        "title": "E-commerce Sales Analytics",
        "tech": "Python(NumPy,Pandas), MySQL, Power BI",
        "description": "Comprehensive analysis of $7.74M revenue data to identify growth drivers. Developed interactive dashboards to track monthly sales trends, category performance, and customer acquisition costs using Python and Power BI.",
        "image_file": "ecomerce.png"
    },
    {
        "title": "HR Employee Analytics",
        "tech": "Power BI,Python(NumPy,Pandas), MySql",
        "description": "Data-driven approach to workforce management. Analyzed employee performance and retention metrics to identify turnover risks, resulting in actionable recommendations for organizational efficiency",
        "image_file": "hranalystics.png"
    },
    {
        "title": "Pizza Shop Sales Analysis",
        "tech": "MySQL, Power BI",
        "description": "End-to-end SQL project to track daily sales, customer preferences, and inventory turnover. Optimized order processing insights by identifying peak hours and best-selling product combinations.",
        "image_file": "pizza sales project.png"
    },
    {
        "title":"Medical Whole Sale Analysis",
        "tech": "MySQL,Python(NumPy,Pandas),Power BI",
        "description":"Inventory and supply chain analysis for a medical wholesaler. Used SQL and Python to track stock levels, expiry dates, and supplier performance to minimize waste and ensure product availability",
        "image_file":"medicalinventory.png"
    }
]

# Step 2: Route Definition
# This function tells Flask to show 'index.html' when someone visits your home page.
@app.route('/')
def home():
    return render_template('index.html', projects=projects_data)
import os

if __name__ == '__main__':
    # Render ya dusri hosting ke liye port dynamic hona chahiye
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)