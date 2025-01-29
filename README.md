# Contributor
| Name  | Job Description |
| ------------- | ------------- |
| Brillyando Magathan Achmad  | Data preparation, data cleaning, and preprocessing data. Create, build, and develope RAG system, prompt engineering, implement virtual try on and integrate to streamlit, integrate to google cloud storage and deploy to cloud run  |
| Putra Al Farizi  | Data Preparation, Data Preprocessing, Analyze Retention Rate, Average Order Value and Conversion Rate, and Develop Chatbot Application with RAG|
| Khalid Destiawan  | Data Preparation, Analyze Retention Rate, Average Order Value and Conversion Rate. Dashboard development |

# Overview
This is the CI/CD phase of our capstone project, product recommendation chatbot and dashboard analysis using Google Cloud Run, from IYKRA AI Engineering Fellowship batch 1.
**Note: this is not the newest version due to free trial credit deadline**

# Explanation
- Before deploying to Google Cloud Run, I added the dataset and images file to Google Cloud Storage. This is the directories inside bucket.
 ![image](https://github.com/user-attachments/assets/bca423b2-4ff1-4422-bdc7-74d8bf520f3a)
  Dataset folder to store the datasets, while image and Final Product(s) to store fashion images, lastly faiss_index is the embedding of our product catalog.
- Created trigger to build a docker image using Google Container Registry, push, and deploy the image to Cloud Run.
  ![image](https://github.com/user-attachments/assets/3993439f-8b2e-4ea9-ba53-9e40b07060d3)
  Whenever I make changes to the code and push it to this repository, it will trigger to build an image and deploy the image immediately to Cloud Run.
- After the app is deployed to Cloud Run, I added secret key, which is Openai API key and Replicate API token.
- The URL will be shown and app can completely be used by anyone who has the URL.

# Demo
[![YouTube](http://i.ytimg.com/vi/yzXIu8Tc0r4/hqdefault.jpg)](https://www.youtube.com/watch?v=yzXIu8Tc0r4)


# Business Understanding

## Problem Description
An e-commerce platform faces challenges in delivering a personalized shopping experience. The lack of tailored product recommendations leads to reduced customer engagement, lower conversion rates, and a suboptimal average order value. Customers expect intuitive and customized support when navigating extensive product catalogs, but the platform currently lacks the capability to provide this level of personalization.

## Goals
Develop a chatbot that leverages customer data to provide personalized product recommendations, enhancing customer engagement, satisfaction, and trust.

## Project Objectives
1. Build an AI-powered chatbot capable of analyzing customer behavior and customer preference to deliver personalized product recommendations in real-time.
2. Create a dashboard for tracking chatbot performance and customer behavior insights, aiding in data-driven decision-making.

# Tool
- Deployment: Streamlit
- Vector database: FAISS
- LLM (Large Language Model): GPT 4o
- Data Visualization: Looker

# Project instruction

## Installation

Follow these steps to install the project from GitHub:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/PutraAlFarizi15/capstone-project-personalized-shopping-copilot.git
2. **Navigate to the project directory**
    ```bash
    cd capstone-project-personalized-shopping-copilot
3. **Create a virtual environment (optional but recommended)**
    ```bash
    python -m venv venv
4. **Activate the virtual environment**
    ```bash
    # Windows
    venv\Scripts\activate
    # MacOS/Linux
    source venv/bin/activate
5. **Install the project dependencies**
    ```bash
    pip install -r requirements.txt
6. **Add your OpenAI API key to the app.py file**: Find the following line in the app.py file and replace it with your API key
    ```bash
    openai_api_key = 'your openai api key'
7. **Run the application using Streamlit**
    ```bash
    streamlit run main.py
    ```

## How to use Application
Once the application is running, you will see the following message:
```bash
💬 Product Recommendation Chatbot
Welcome! Please provide your Customer ID to start.
```
**Steps:**

1. **Enter the Customer ID:**
   - Customer IDs are obtained from the customer interaction dataset.
   - As an example, you can use `CUST1001`.\
   after entering the Customer ID, the chatbot will respond:
   ```bash
   Thank you! Customer ID 'CUST1001' has been verified. How can I assist you?
    ```

2. **Request Product Recommendations**
    - Example prompt: white shirt with friend
    - The chatbot will recommend up to 3 products along with Buy and Virtual Try On buttons.
    after entering the Query, expectation that the chatbot response will be:
        ```bash
        based on the analysis of your purchase history and the product catalog, I recommend the following blue shirts for your vacation:

        1.Product ID: PROD4632

        Rating: 3.66\
        Size: L\
        Color: Blue\
        Price: 2,207,297.76\
        Weather: Sunny\
        Event Type: Vacation\
        Reason: This shirt is specifically designed for sunny weather, making it ideal for vacation. Its blue color aligns with your preference, and it falls within a similar price range to your previous purchases, indicating a potential fit for your budget.
        ```
        ![Struktur Database](image/PROD1457.jpg)\
        ```bash
        Virtual Try On
        ```

3. Virtual Try-On  
    - Click the **Virtual Try On** button to try the product virtually.  
    - You will then be prompted to upload a picture of a model or a person.  
    - The uploaded image will be processed, and the result will display the person wearing the selected clothing item. \

## NOTES (IMPORTANT!)
This app is the deployed phase, where the secret keys are stored in Google Cloud Run. The link cannot be accessed after Jan, 29th 2025.
The uploaded image and result from virtual try on will be saved on Google Cloud Storage, and will be deleted immediately after the session is finished.



