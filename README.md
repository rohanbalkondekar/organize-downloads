# Organize Downloads

Python script to sort files in the Downloads folder by extension.


## Quick Start
1. Requires Python 3.x
2. Run `python organize_downloads.py` in the terminal.

## Details
- Creates necessary subfolders.
- Renames duplicates to prevent overwrites.
- Affects files only, not subdirectories.


## Completely Written by GPT-4-Turbo in 3 Shots

Initial Set of Prompts that I used

```python
system_prompt = """You are an Excellent Software Engineer. You specilize in python. You write highly performant Python code to organize files i.e. moving different types of files into designated folders
"""
```

```python
user_prompt = """ 
Write Python Code to Move/Organize Different Types of Files into Designated Folders. 
For Documents, Images, Music, Executables, Zip, etc.

**IMPORTANT**
- Support Wide variety of file types and their respective folders
- The Script should be able to run on any OS
- Only Move Files and NOT folders
- Implement Proper Error Handling
- Avoid Overwriting Files

Take a DEEP BREATH and Think Step By Step
Plan, Explain and Solve
"""
```

later based on the output that it generated, subsequent prompting is done 
e.g. 
- `Add more file types and folders` 
- `move rest of the files in 'others' folder including the files without extension`
-  `dynamically get the 'downloads' folder path`, etc

I use GPT-4 via OpenAI Python API in a Jupiter Notebook
Below is the code that I use:

```python
import sys
import openai

client = openai.OpenAI(api_key='sk-')

# Prompts
system_prompt = """You are an ...
"""

user_prompt = """Write Python ...
"""

messages=[
  {"role": "system", "content": system_prompt},
  {"role": "user", "content": user_prompt},
]

stream_response = True # Streaming is enabled by default

completion = client.chat.completions.create(
    model='gpt-4-1106-preview',
    messages=messages,
    temperature=0.5,
    stream=stream_response  
)

gpt_response = ""

if stream_response:
    for chunk in completion:
        content = chunk.choices[0].delta.content
        if content is not None:
            sys.stdout.write(content)
            sys.stdout.flush()
            gpt_response = gpt_response + content
else:
    print(completion.choices[0].message.content)
```

Responses are streamed by default, trun that off by setting `stream_response = False` if you face any issues with streaming

To continue the conversation, I use the following code in the next cell:

```python
user_reply = r'''Cool! Now do this ...
'''

messages.append({"role": "assistant", "content": gpt_response})
messages.append({"role": "user", "content": user_reply})

completion = client.chat.completions.create(
  model="gpt-4-1106-preview",
  messages=messages,
  stream=True,
)

gpt_response = ""

for chunk in completion:
    content = chunk.choices[0].delta.content
    if content is not None:
        sys.stdout.write(content)
        sys.stdout.flush()
        gpt_response = gpt_response + content
```

This approach is lousy as you need to copy this entire code every time you want to continue. You can convert this into a function or class, which is left as an exercise for the reader.

