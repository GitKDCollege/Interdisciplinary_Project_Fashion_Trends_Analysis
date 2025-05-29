from dotenv import load_dotenv
import streamlit as st
import os
import requests
import sqlite3 as lite
import json

load_dotenv()
API_KEY = os.getenv('GROQ_API_KEY')

# Prompt
prompt = [
    """
    You are a chatbot for our fashion trend analysis website. You need to convert English queries into SQL commands.
    The SQL database contains a table called Data with the following columns:
    Brand, Selling_Price, MRP, Category_By_Gender, Category_By_Attire, Discount_Percentage, Category_By_Cloth.
    Do not include ``` or the word "sql" in your output. Your job is to return only the valid SQL query in plain text.

    If the query is not regarding the Data, then reply with "Sorry, this is out of the Context of this Application"

    If the query is about data but something that cannot be done by SQL queries (eg comparing two things, visualize, etc), reply with "Sorry, This is out of my current capabilities, Please try another prompt"

    Example 1 – What is the total number of fashion items available?
    SELECT COUNT(*) FROM Data;

    Example 2 – Show all items with more than 30% discount.
    SELECT * FROM Data WHERE Discount_Percentage > 30;

    Example 3 – List all men’s footwear from the database.
    SELECT * FROM Data WHERE Category_By_Gender = 'Men' AND Category_By_Attire = 'Footwear';

    Example 4 – Find the average selling price of clothing for women.
    SELECT AVG(Selling_Price) FROM Data WHERE Category_By_Gender = 'Women';

    Example 5 – Get all items where the selling price is less than 1000.
    SELECT * FROM Data WHERE Selling_Price < 1000;

    Example 6 – What are the different clothing categories available?
    SELECT DISTINCT Category_By_Cloth FROM Data;

    Example 7 – Show all items where the brand is ‘Nike’.
    SELECT * FROM Data WHERE Brand = 'Nike';
    """
]

def get_groq_response(question, prompt):
    url = 'https://api.groq.com/openai/v1/chat/completions'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{
            "role": "user",
            "content": f"{prompt[0]} {question}"
        }]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_data = response.json()
        return response_data['choices'][0]['message']['content'].strip()
    else:
        return f"Error: {response.status_code} - {response.text}"

def read_sql_query(sql, db):
    try:
        conn = lite.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
    except Exception as e:
        return [("Error", str(e))]
    finally:
        conn.commit()
        conn.close()

# Streamlit UI
st.set_page_config(page_title="Chatbot")
st.title("Interact with Data !!")

question = st.text_input("Ask your queries:", key="input")
submit = st.button("Ask the question")

if submit:
    # SQL response:
    sql_response = get_groq_response(question, prompt)
    st.subheader("Response:")
    print(sql_response)

    if(sql_response.startswith("Sorry")):
        st.markdown(sql_response)
    else:
        rows = read_sql_query(sql_response, "data.sqlite")

        for row in rows:
            if len(row) == 1:
                st.markdown(f"<p style='font-size:20px;'>{row[0]}</p>", unsafe_allow_html=True)
            else:
                formatted = " | ".join(str(col) for col in row)
                st.markdown(f"<p style='font-size:20px;'>{formatted}</p>", unsafe_allow_html=True)

    # st.subheader("The Corresponding SQL Query is:")
    # st.code(sql_response, language='sql')