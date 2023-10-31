import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.llms import OpenAI
import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
chat = ChatOpenAI(temperature=.7, openai_api_key=openai_api_key)
# Sidebar contents
with st.sidebar:
    st.title('💬 HR.ai')
    st.markdown('''
    ## About
    This app lets you prepare for the interview:
    - [Email us]- abraar237@gmail.com
    ''')
    



llm = OpenAI(model_name="text-davinci-003", openai_api_key=openai_api_key)
    
def main():
    st.header("Chat with HR 💬")
 
 
    # upload a PDF file
    pdf = st.file_uploader("Upload your Resume", type='pdf')
 
    # st.write(pdf)
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()


    user_input = st.text_input("Enter your Profession")
    
    if user_input:

        new=chat(
        [
            SystemMessage(content=f"""
    I want you to behave like an HR im recruiting for job as {user_input}.
    i want you to ask me 5 specific  {user_input }related 
    questions regarding my resume resume details i submitted 
    the questions that you ask should not be too long  after each qestions
    start your response by saying WELCOME to HR.ai
    """),
            HumanMessage(content=f"my resume:{text}")
        ]
    )
        new=str(new)
        content = new.split("=")[1].split('\'')[1]
        st.write(content)


if __name__ == '__main__':
    main()