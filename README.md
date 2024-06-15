# Generative AI Text-to-Text App

This repository contains a Generative AI application for text-to-text generation using the "google/flan-t5-small" model from Hugging Face. The project leverages Docker in Hugging Face Spaces and FastAPI for deployment, and Uvicorn for local runs, with a user-friendly web interface powered by ChatGPT.

## Features

- Text-to-text generation using state-of-the-art AI
- Dockerized setup for easy deployment
- FastAPI for efficient API handling
- Uvicorn for local development
- Interactive web app interface

## Installation

### Step 1: Create and Activate Conda Environment

```bash
conda create -p venv python==3.9 -y
conda activate D:\dockergenai\venv
```

### Step 2: Clone the Repository

```bash
git clone https://github.com/Rohitjakkam/Text2Text-Using-Hugging-Face.git
cd Text2Text-Using-Hugging-Face
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application Locally

```bash
uvicorn main:app --reload
```

### Step 5: Access the FastAPI Documentation

Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the API documentation.

## Usage

- Start the application and access the web interface.
- Use the provided endpoints to perform text-to-text generation tasks.
- Refer to the FastAPI documentation for detailed API usage.

## Acknowledgements

Special thanks to Kirsh Naik for his insightful video that guided this project. Check out his video [here](https://www.youtube.com/watch?v=aA76uj5kQac).

## Links

- [FastAPI Docs](https://rohitjakkam-text2text-using-docker.hf.space/docs#/default/generate_generate_get)
- [GitHub Repository](https://github.com/Rohitjakkam/Text2Text-Using-Hugging-Face)

## License

This project is licensed under the MIT License. See the LICENSE file for details.
