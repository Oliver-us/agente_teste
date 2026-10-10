from groq import Groq
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

st.title('AGENTE DE ATENDIMENTO')


client = Groq(api_key=os.getent.get('API_KEY_GROQ'))


pergunta = st.text_input('Digite uma pergunta: ')



SYSTEM_PROMPT  = 'Você é um atendente mano da quebrada que fala varias girias e usa sarcásmo no atendimento'


chat_completion = client.chat.completions.create(

    messages=[


        {"role": "system", 'content': SYSTEM_PROMPT }, 

        {"role": "user", "content": pergunta}

    ],

  model="openai/gpt-oss-120b",

  temperature = 0.7


)



st.write(chat_completion.choices[0].message.content)