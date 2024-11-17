import pickle
import os
import google.generativeai as genai

google_api_key='AIzaSyBm1AppYECEOWE_vhMi7NrBl6Y3T718XLk'
genai.configure(api_key=google_api_key)


model=genai.GenerativeModel('gemini-pro')


response=model.generate_content("What is life span of person")
print(response.text)


