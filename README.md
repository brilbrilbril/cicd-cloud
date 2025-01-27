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


