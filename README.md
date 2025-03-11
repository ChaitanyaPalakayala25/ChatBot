# Document Chatbot
## Prerequisites

- Python 3.8 or later
- A Hugging Face API key

## Installation

### Step 1: Install Python

1. **Download Python**:
   - Go to the official Python website: [python.org](https://www.python.org/).
   - Download the latest version of Python (3.8 or later).
   - During installation, make sure to check the box that says **"Add Python to PATH"**.

2. **Verify Installation**:
   - Open a terminal or command prompt and run:
     ```bash
     python --version
     ```
   - This should display the installed Python version (e.g., Python 3.10.12).

---

### Step 2: Set Up the Project Directory

1. **Create a Project Folder**:
   - Open a terminal or command prompt.
   - Create a new directory for your project:
     ```bash
     mkdir Document-Chatbot
     cd Document-Chatbot
     ```

2. **Create a Virtual Environment**:
   - Inside the project folder, create a virtual environment:
     ```bash
     python -m venv VirturalEnv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       VirturalEnv\Scripts\activate
       ```
     - On Mac/Linux:
       ```bash
       source VirturalEnv/bin/activate
       ```
   - Your terminal prompt should now show `(VirturalEnv)`, indicating the virtual environment is active.

---

### Step 3: Install Dependencies

1. **Upgrade pip**:
   - Ensure pip is up to date:
     ```bash
     pip install --upgrade pip
     ```

2. **Install Required Libraries**:
   - Install the necessary Python libraries:
     ```bash
     pip install streamlit python-dotenv PyPDF2 langchain sentence-transformers faiss-cpu transformers torch
     ```

---

### Step 4: Set Up Hugging Face API Key

1. **Get a Hugging Face API Key**:
   - Go to [Hugging Face](https://huggingface.co/).
   - Sign up or log in to your account.
   - Click on your profile picture → **Settings** → **Access Tokens**.
   - Create a new token with **Read** permissions.
   - Copy the token.

2. **Create a `.env` File**:
   - Inside your project folder, create a file named `.env`.
   - Add the following line to the file:
     ```
     HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_key_here
     ```
   - Replace `your_huggingface_api_key_here` with the token you copied.

---

### Step 5: Create the `app.py` File

1. **Create the File**:
   - Inside your project folder, create a file named `app.py`.
   - Open the file in a text editor or IDE (e.g., VS Code).

2. **Add the Code**:
   - Copy and paste the app.py code from this repo into `app.py`.
   - Copy and paste the htmlTemplates.py code from this repo into `htmlTemplates.py`.
---

## Running the Application

**Run the Streamlit App**:
   - In the terminal, run:
     ```bash
     streamlit run app.py
     ```
   - The application will open in your default web browser.

---

## Usage

1. **Upload PDFs**:
   - Use the sidebar to upload one or more PDF documents.
2. **Ask Questions**:
   - Enter your question in the text input box and press Enter.
3. **View Responses**:
   - The chatbot will display responses based on the content of the uploaded PDFs.

---
