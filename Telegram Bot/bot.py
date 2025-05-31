import telebot
from langchain_groq import ChatGroq
import re
import streamlit as st

st.title('🤖 Telegram Bot')

st.divider()
st.info('LLM Generative AI using API of Deepseek integrated with Telegram chat')
st.write("Check out the [Telegram Bot](https://t.me/imagepower_bot) for more details.")

#Initialize the LLM model
llm = ChatGroq(
    temperature=0,
    groq_api_key="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",
    model_name="deepseek-r1-distill-llama-70b"
)

# Initialize the bot
bot = telebot.TeleBot('7774959017:AAEQZJGWOM-iLZzKg6Gs3JB8jgm4lWVkpF8')

# Command to start the bot
@bot.message_handler(commands=['start','hi','hello'])
def start(message):
    bot.send_message(message.chat.id, "Hi! I am Rupesh's personal assistant. How can i help you?", parse_mode='html')

# Handler for incoming text messages
@bot.message_handler(content_types='text')

def echo(message):
    # Get the response from the LLM based on user input
    response = llm.invoke(message.text)  # Send message.text to LLM and get response
    
    # Sanitize the response by removing unsupported HTML tags
    sanitized_response = re.sub(r'</?[^>]+>', '', response.content)  # Remove all HTML tags
    
    # Print the sanitized response (for debugging purposes)
    #print(message.text)
    #print(sanitized_response)
    
    # Send the sanitized response back to the user as the bot's reply
    bot.send_message(message.chat.id, sanitized_response, parse_mode='html')

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    # Your bot's response logic here
    bot.send_message(message.chat.id, "I received your message!")

# Run the bot
bot.infinity_polling()
