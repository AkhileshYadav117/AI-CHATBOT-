import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Initializing Groq Client with your active key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

system_prompt = """
You are a person named Akhilesh who speaks Hindi and English.
He is from India and is a coder.
Analyze the chat history and reply exactly like Akhilesh would.
Keep responses short and natural.
"""

# Cleaned up chat history layout string
command = """
[8:02 pm, 10/05/2026] Akhilesh Yadav: Sachhi n
Haa bhai
[8:02 pm, 10/05/2026] Sahil 11th Science: Confirm hai n
[8:02 pm, 10/05/2026] Sahil 11th Science: Haa thik hai
[8:02 pm, 10/05/2026] Akhilesh Yadav: Tumhara centre aaya h kya
[8:02 pm, 10/05/2026] Sahil 11th Science: Tumhara centre aaya h kya
Ha
[8:03 pm, 10/05/2026] Akhilesh Yadav: Kb h paper
[8:03 pm, 10/05/2026] Sahil 11th Science: 12 ko 1st shift
[8:03 pm, 10/05/2026] Akhilesh Yadav: Acha
[8:03 pm, 10/05/2026] Akhilesh Yadav: All the best
[8:03 pm, 10/05/2026] Sahil 11th Science: Thanks
[7:42 pm, 13/05/2026] Sahil 11th Science: +91 93700 37835
"""

# FIXED: Switched to the correct structural messages list format for Groq execution
response = client.chat.completions.create(
    model="openai/gpt-oss-20b",  
    messages=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": f"Chat History:\n{"\n".join([line.split(":", 2)[-1].strip() if "]" in line and ":" in line else line for line in command.strip().split("\n")])}\n\nReply:"
        }
    ]
) 

# FIXED: Correct target extraction parameter formatting
print(response.choices[0].message.content.strip())