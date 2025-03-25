import pyautogui
import pyperclip
import time
from openai import OpenAI

client = OpenAI(
  api_key="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",
)
def is_last_message_from_sender(chat_log, sender_name="Rohan Das"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True 
    return False
    


# Step 1: Click at the icon at (1109, 874)
pyautogui.click(1109, 874)
time.sleep(1)  # Wait for 1 second to ensure the icon is clicked and the window is active


while True:
    time.sleep(5)

    # Step 2: Click and drag from (476, 200) to (1560, 774) to select text

    pyautogui.moveTo(220, 88)  # Move the mouse to the ending point with a 1-second duration
    pyautogui.dragto(1581,846, duration=2,button='left')  # Release the mouse button to finish the selection


    # Step 3: Press Ctrl+C to copy the selected text
    pyautogui.hotkey('ctrl', 'c')

    time.sleep(2)  # Wait for 1 second to allow the clipboard to update
    pyautogui.click(164,550)
    # Step 4: Retrieve the copied text from the clipboard
    chat_history = pyperclip.paste()

    # Print the copied text
    print(chat_history)

    if is_last_message_from_sender(chat_history):



        command='chat'
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named mayank who speaks hindi as well as english.you are from india and is a coder. You analyze chat history and respond like Naruto.Output should be the next response (text message only)  "},
            {"role": "user", "content":chat_history}
        ]
        )

        response = completion.choices[0].message.content

        pyperclip.copy(response)


        # Step 5: Click at (1328, 1808) to focus the target area
        pyautogui.click(1328, 1808)
        time.sleep(1)  # Wait for the click to be processed

        # Step 6: Paste the copied text (Ctrl+V)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for the paste action

        # Step 7: Press Enter
        pyautogui.press('enter')
