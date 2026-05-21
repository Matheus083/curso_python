import os
from google import genai

# Inicialize o cliente (ele buscará automaticamente a variável de ambiente GEMINI_API_KEY)
# Como alternativa, você pode passar a chave diretamente: client = genai.Client(api_key="SUA_CHAVE")
client = genai.Client(apy_key=)

# Gere conteúdo utilizando um modelo, como o 'gemini-2.5-flash'
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='Me fale sobre a linguagem de programação Python.',
)

print(response.text)
