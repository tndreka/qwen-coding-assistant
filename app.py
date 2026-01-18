"""Main application - Qwen Coding Assistant."""
import chainlit as cl
import ollama
from core.config import Config
from core.prompts import SYSTEM_PROMPT, WELCOME_MESSAGE
from utils. logger import setup_logger

logger = setup_logger(__name__)

@cl.on_chat_start
async def start_chat():
    """Initialize chat session."""
    logger.info("New chat session started")
    
    cl.user_session.set(
        "conversation",
        [{"role": "system", "content":  SYSTEM_PROMPT}]
    )
    
    await cl.Message(content=WELCOME_MESSAGE).send()

@cl.step(type="tool")
async def generate_response(user_message: str):
    """Generate AI response."""
    try:
        conversation = cl.user_session.get("conversation")
        conversation.append({"role": "user", "content": user_message})
        
        logger.info(f"Generating response for: {user_message[: 50]}...")
        
        response = ollama.chat(
            model=Config.MODEL_NAME,
            messages=conversation
        )
        
        conversation.append({
            "role": "assistant",
            "content": response. message. content
        })
        
        return response
    except Exception as e:
        logger.error(f"Error: {e}")
        raise

@cl.on_message
async def main(message: cl.Message):
    """Handle incoming messages."""
    response_msg = cl.Message(content="")
    
    try:
        ai_response = await generate_response(message.content)
        
        for token in ai_response.message.content:
            await response_msg.stream_token(token)
        
        await response_msg.send()
    except Exception as e:
        logger.error(f"Error: {e}")
        await cl.Message(content="❌ Sorry, an error occurred. ").send()

if __name__ == "__main__":
    logger.info(f"Starting Qwen Coding Assistant with {Config.MODEL_NAME}")
    cl.run()