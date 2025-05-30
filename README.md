# LMArena Minimal Demo

This project is a minimal Streamlit web app for comparing responses from different Large Language Models (LLMs) side by side. Users can select two LLMs, enter a prompt, and vote for the better response. The app is designed for easy extension and secure API key management using Streamlit's secrets.

## What is a Benchmark?

A benchmark is a standardized method or set of tests used to evaluate and compare the performance, quality, or capabilities of different systems, models, or algorithms. In the context of Large Language Models (LLMs), a benchmark typically involves presenting the models with the same set of prompts or tasks and measuring their responses according to specific criteria, such as accuracy, relevance, fluency, or user preference.

This app serves as a benchmarking tool by allowing users to compare responses from different LLMs side by side using the same prompt. Users can then vote for the better response, providing a simple and interactive way to assess and compare the strengths and weaknesses of various LLMs.

## How to Design a Benchmark?

Designing a benchmark involves several key steps to ensure **fair, meaningful, and reproducible** evaluation of models or systems. Here are some general guidelines, especially relevant for benchmarking Large Language Models (LLMs):

1. **What is the Objective:**
   - Clearly state what you want to measure (e.g., accuracy, helpfulness, creativity, safety).

2. **What are the Tasks:**
   - Choose a diverse and representative set of tasks that reflect real-world use cases or specific evaluation goals.
   - Ensure the tasks are unbiased and cover different difficulty levels.

3. **How to Standardize the Evaluation Process:**
   - Present the same tasks to all models under the same conditions.
   - Control for variables such as prompt wording, context, and temperature settings.

4. **What are the Evaluation Metrics:**
   - Decide how you will measure performance (e.g., human preference, accuracy, BLEU score, response time).
   - For subjective tasks, consider using human raters or crowd-sourced voting.

5. **How to Collect and Analyze Results:**
   - Gather responses and scores for each model.
   - Use statistical analysis to compare models and identify significant differences.

6. **Document and Share:**
   - Clearly document your benchmark design, tasks, and evaluation criteria so others can reproduce or build upon your work.

## Obtain API Keys for Supported LLMs

### 1. Google Gemini
- Go to https://aistudio.google.com/app/apikey
- Log in with your Google account.
- Click "Create API key" and copy the generated key to `.streamlit/secrets.toml`.

### 2. Nvidia NIM
- Go to https://build.nvidia.com
- Register an account and log in. You need to verify your account with phone number (US) to use the free API.
- Click on your profile icon (top right) and navigate to `API keys` tab
- Generate an API key and copy it to `.streamlit/secrets.toml`.
- Select a model that you are interested in, e.g., DeepSeek-R1, and use `view code` button to view the sample code on using API key to access model 

## Adding API Keys and Model Names to the App
1. Open or create the file `.streamlit/secrets.toml` in your project directory.
2. Add your API keys and model names under the appropriate LLM section, for example:

```toml

[llms.llm1]
name = "Google Gemini"
api_key = "your-gemini-api-key"
model = "google/gemini-pro"
```

**Note: Never share or commit your API keys to public repositories.**


# Deployment of Web App

## Deploy to Streamlit Community Cloud

1. **Push your code to a GitHub repository**
   
   Do **not** include your `.streamlit/secrets.toml` in the repository. Instead, add it to your `.gitignore`.

2. **Go to [Streamlit Community Cloud](https://share.streamlit.io)**
   
   - Click "Deploy an app" and connect your GitHub repo.
   - Set the main file path to `arena_demo.py`.

3. **Add your secrets**
   
   - In the app settings on Streamlit Cloud, find the "Secrets" section.
   - Copy the contents of your local `.streamlit/secrets.toml` and paste them into the secrets editor.

4. **Deploy**
   
   - Click "Deploy". Your app will build and launch online.

## Deploy using Render

1. Push the project to a GitHub repo.
2. Go to render.com and connect it with your GitHub account
3. Deploy the web using Render's dashboard
   1. In the build command: add `pip install -r requirements.txt`
   2. In the start command: add `gunicorn app:app`

## Deploy using Vercel
1. Push the project to a GitHub repo.
2. Go to vercel.com and connect it with your GitHub account
3. Deploy the web using the dashboard
   1. Note: You need vercel.json file to configure the deployment. An example is given below:
   ```json
   {
   "builds": [
    { "src": "app.py", "use": "@vercel/python" }
   ],
   "routes": [
    { "src": "/(.*)", "dest": "app.py" }
   ]
   } 
   ```