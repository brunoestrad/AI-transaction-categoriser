#   🏦 AI-transaction-categoriser

This script processes bank statements and categorises transactions using an **LLM-based approach** via the **Groq API** and displays an interactive dashboard that allows for category and month filtering as well as pie chart for visual representation. It automates financial transaction classification, making it easier to analyze personal finances.

## 🚀 Features
- Loads bank statements from CSV files.
- Uses **LLM (Llama 3.1-8B)** to categorise transactions.
- Saves the categorised transactions into a new CSV file (`finances.csv`).
- Supports multiple categories:  
  - Dining Out, Payment Received, Health, Groceries, Education, Transport, Investing, etc.

## 🛠 Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/brunoestrad/AI-transaction-categoriser.git
cd AI-transaction-categoriser
```
### 2️⃣ Install Dependecies
```sh
pip install -r requirements.txt
```
### 3️⃣ Set Up API kEY
```sh
Create a .env file in the project root and add:

GROQ_API_KEY=your_api_key_here

Replace your_api_key_here with your actual Groq API Key.
```
## 📂 Usage

### 1️⃣ Place Your Bank Statements in the `statements` Folder
- Ensure your bank statements are in CSV format with necessary fields

(`Transaction Description`, `Debit Amount`, `Transaction Date`, etc).

### 2️⃣ Run the Script
```sh
python llm_finance.py
```
### 3️⃣ Check the Categorised Transactions

After running the script, a new CSV file (`finances.csv`) will be created with an addtional **Category** column.

### 4️⃣ Run the Dashboard
```sh
streamlit run dash.py
```

## 🛠 Future Improvements
- Add support for more financial institutions and file formats.
- Improve transaction classification with custom rules and user feedback.
- Implement a local LLM model to remove dependency on external APIs.

## 

