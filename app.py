import streamlit as st
import google.generativeai as genai


st.header("uygulama v1")


genai.configure(api_key="AIzaSyCEvvvZ-L8TPN-o1GPlMoREiFoQj5oKPYc")
safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_LOW_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
    ]
generation_config = {
        "temperature": 0.9,  #0'a yaklaştıkça hayal gücü artıyor 1'e yaklaştıkça gerçekliği artıyor
        "top_p": 0.90,  #halisünasyon geçirmesi azalıyor
        "top_k": 64,
        "max_output_tokens": 18192,  #bir milyon kadar token alabiliyor
        "response_mime_type": "text/plain",
    }
model = genai.GenerativeModel(

    safety_settings=safety_settings,
    generation_config=generation_config,
    model_name="gemini-1.5-flash-latest"

)
prompt="Sen bir kadın e-ticaret uzmanısın. Erkek iç çamaşırı firması için bir reklam kampanyası hazırlamanı istiyorum."
response= model.generate_content(prompt).text
st.markdown(response)

