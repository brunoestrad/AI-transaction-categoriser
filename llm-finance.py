import csv
import pandas as pd
from datetime import datetime
import os

# LLM Imports:
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.prompts import  PromptTemplate
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
# from huggingface_hub import InferenceApi


def load_CSV(): 

    transactions_data = []
    for statement in os.listdir("statements"):
        
        try:
            with open (f'statements/{statement}') as file:
                # Read CSV as dictionary
                reader = csv.DictReader(file)
                for row in reader:
                    transactions_data.append(row)
            
        except FileNotFoundError:
            print("File not found!")
    
    print(f"\nSuccessfully loaded {len(transactions_data)} rows")
    return transactions_data


def llm_categorisation(df):
    _ = load_dotenv(find_dotenv())

    template = """
    You are a data analyst with over 2 decades of experience working in a project of
    data cleaning. Your job is to choose an adequate category for each transaction
    that will be sent to you.

    They're all transactions from a person's bank statement.

    Choose between the following categories:
    - Dining out
    - Income: Please note this includes only negative inputs
    - Health
    - Groceries
    - Education
    - Transport
    - Investment
    - Phone
    - Shopping
    - Charity

    Pick a category for this item: {text}

    Reply only with one category, don't use any special characters, only the category as a response
    """

    prompt = PromptTemplate.from_template(template=template)
    #chat = ChatGroq(model="llama-3.3-70b-versatile")
    chat = ChatGroq(model="llama-3.1-8b-instant")

    # Groq's library/SDK automatically finds GROQ_API_KEY, however this can be
    # done if a custom key is available
    # api_key = os.getenv("GROQ_API_KEY")
    # chat = ChatGroq(model="llama-3.3-70b-versatile", api_key=api_key)

    chain = prompt | chat

    category = []
    for transaction in list(df["Description"].values):
        category += [chain.invoke(transaction).content]

    df["Category"] = category
    df.to_csv("finances.csv")

if __name__ == "__main__":

    transactions_data = load_CSV()

    df = pd.DataFrame(transactions_data)
    df["Amount"] = df["Amount"].astype(float)
    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")
    del df["Postcode"], df["Address"], df["Town/City"], df["Country"]

    llm_categorisation(df)
