import os
from dotenv import load_dotenv
import json
import chainlit as cl
from litellm import completion

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    print("\n❌ ERROR: GEMINI_API_KEY not set in environment variables.")
    exit()

@cl.on_chat_start
async def start():
    """Set up the chat session when a user connects."""
    cl.user_session.set("chat_history", [])
    await cl.Message(content="Welcome to the Gemini AI Assistant! How can I help you today?").send()

@cl.on_message
async def main(message: cl.Message):
    """Process incoming messages and generate responses."""
    msg = cl.Message(content="Thinking...")
    await msg.send()

    # get chat history
    history = cl.user_session.get("chat_history") or []

    # Append the user's message
    history.append({"role": "user", "content": message.content})

    try:
        # get completion from LiteLLM
        response = completion(
            model="gemini/gemini-2.0-flash",
            api_key=gemini_api_key,
            messages=history
        )

        response_content = response.choices[0].message.content

        # Send assistant's reply
        msg.content = response_content
        await msg.update()

        # Append assistant's reply to history
        history.append({"role": "assistant", "content": response_content})
        cl.user_session.set("chat_history", history)

        print(f"User: {message.content}")
        print(f"Assistant: {response_content}")

    except Exception as e:
        msg.content = f"Error: {str(e)}"
        await msg.update()
        print(f"Error: {str(e)}")

@cl.on_chat_end
async def on_chat_end():
    history = cl.user_session.get("chat_history") or []
    with open("chat_history.json", "w") as f:
        json.dump(history, f, indent=2)
    print("Chat history saved.")
