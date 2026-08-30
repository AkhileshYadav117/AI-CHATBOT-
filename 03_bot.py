import os
import pyautogui
import pyperclip
import time
from dotenv import load_dotenv

load_dotenv()
# from groq import Groq # Switched online architecture import

# Initializing Groq Client with your active key layout parameters
from groq import Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Split the chat log into individual messages
def is_last_message_from_sender(chat_log, sender_name="Mummy"):
    messages = chat_log.strip().split("/2026]")[-1]
    if sender_name in messages:
        return True 
    return False 

# Move to taskbar and click Chrome initially to bring it to focus
pyautogui.moveTo(1375, 1071, duration=0.5) 
pyautogui.click()
time.sleep(1.5)  # Wait for Chrome to smoothly pop up on top of VS Code

while True:
    # --- STEP 1: AUTOMATICALLY CLICK CHROME ON TASKBAR ---
    # ( Handled initially outside the loop, or coordinates can be re-called here if needed )

    # --- STEP 2: DRAG AND SELECT TEXT IN CHROME ---
    pyautogui.moveTo(679, 197) 
    time.sleep(0.3)
    pyautogui.mouseDown(button='left')
    time.sleep(0.3)
    pyautogui.moveTo(1843, 972, duration=1.5)
    time.sleep(0.3)
    # pyautogui.click(1603,840)
    pyautogui.mouseUp(button='left')
    time.sleep(0.5)

    # --- STEP 3: COPY SELECTED CHAT ---
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(1843, 972)
    time.sleep(0.5)
    
    # Store clipboard text in a variable
    chatHistory = pyperclip.paste()

    print("Copied Text : ")
    print(chatHistory)
    
    # --- STEP 4: CONDITIONAL GENERATION & SENDING ---
    if is_last_message_from_sender(chatHistory):
        
        # REMOVE TIMESTAMP AND DATE: Clean each line directly inside this block
        cleaned_chat = "\n".join([line.split(":", 2)[-1].strip() if "]" in line and ":" in line else line for line in chatHistory.strip().split("\n")])
        
        print("Cleaned Text Sent to AI: ")
        print(cleaned_chat)

        # Requesting online response from Groq infrastructure
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",  
            messages=[
                {
                  "role": "system",
                    "content": """
                    You are a regular Indian guy named Akhilesh who is a coder. 
                    CRITICAL RULES FOR CHAT:
                    1. Respond in casual, natural Hinglish (mix of Hindi and English) just like a normal person.
                    2. Your response MUST be ultra-short (Maximum 1 small sentence or 5-8 words).
                    3. Do NOT write paragraphs, do NOT give long explanations, and do NOT talk about your projects, mummy, or village unless the other person explicitly asks you about it.
                    4. Never sound like an AI assistant. Keep it pure, raw text messaging style.
                    5.Write as the receiver can understand your sent  messages .
                    """
                },
                {
                    "role": "user",
                    "content": f"Here is the recent chat history:\n{cleaned_chat}\n\nReply as Akhilesh to the very last message:" 
                }
            ]
        )
        
        # Extracting target reply text string payload
        human_reply = response.choices[0].message.content.strip()
        
        pyperclip.copy(human_reply)
        time.sleep(0.3)
        print(response)  # Matches your original print object visualization format
        pyperclip.copy(human_reply)

        # Click message box inside Chrome
        pyautogui.click(787, 973)
        time.sleep(0.5)

        # Paste copied text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)

        # Press Enter to send
        pyautogui.press('enter')
        
    else:
        print("Last message is not from Mummy. Skipping reply generation.")

    # Loop cooling delay to prevent hitting regional token velocity walls
    print("Waiting 10 seconds before running next cycle...")
    time.sleep(10)