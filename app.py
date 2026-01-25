from flask import Flask, render_template
import os

app = Flask(__name__)

projects_data = [
    {
        "title": "E-commerce Sales Analytics",
        "tech": "Python, MySQL, Power BI",
        "description": "Comprehensive analysis of $7.74M revenue data to identify growth drivers.",
        "image_file": "ecomerce.png",
        "video_id": "1LmT_gCoQBTFN-xRmwUxZXSfwpeyCvn4l"
    },
    {
        "title": "HR Employee Analytics",
        "tech": "Power BI, Python, MySQL",
        "description": "Data-driven approach to workforce management and retention metrics.",
        "image_file": "hranalystics.png",
        "video_id": "1FhKsM2CmVlCaip3zKNYckQZmFTH-SRVi"
    },
    {
        "title": "Pizza Shop Sales Analysis",
        "tech": "MySQL, Power BI",
        "description": "End-to-end SQL project to track daily sales and customer preferences.",
        "image_file": "pizzasalesproject.png",
        "video_id": "1T_0HbsyBpqJfY3RtxL8q5VJFG4B6Jw0Z"
    },
    {
        "title": "Medical Whole Sale Analysis",
        "tech": "MySQL, Python, Power BI",
        "description": "Inventory and supply chain analysis for a medical wholesaler.",
        "image_file": "medicalinventory.png",
        "video_id": "1gk2OTEQxSiMaAqlaKjbG_fblvu8zbeTy"
    }
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects_data)

app = app

if __name__ == '__main__':
    app.run(debug=True)