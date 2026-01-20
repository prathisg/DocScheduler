import subprocess

"""
Doctor Appointment Automation using Droidrun (WhatsApp → Notion)

This script triggers a Droidrun agent that:
1. Reads appointment requests from WhatsApp
2. Collects missing details
3. Updates the Notion schedule
4. Handles slot conflicts
5. Sends confirmations
"""

TASK_PROMPT = """
Open WhatsApp directly and find the latest message about a doctor appointment.

Extract 'patient_name', 'pref_date', and 'pref_time'.

If any detail is missing:
- Reply to the user asking ONLY for the missing detail.
- Wait until all three details are provided.

Convert the time to 24-hour format.

Then open Notion.
Do NOT use the AI chat or 'Ask, chat, find with AI' box.

Look for the date in DD-MM-YYYY format (for example: 25-01-2026):
- Check recents first.
- If not found, click the search icon at the bottom and search using the keyboard.

Once the date page is open:
- Look for a table with 'Time' and 'Name' columns.
- Scroll to find the row for the requested time.

If the 'Name' cell is empty:
- Enter the patient's name and save.
- Return to WhatsApp and send:
  "Your appointment is confirmed for [Date] at [Time]."

If the slot is already filled:
- Find the next closest available time.
- Return to WhatsApp and send:
  "That slot is full, can we do [alt_time] instead?"

If the user confirms:
- Return to Notion.
- Update the new time slot with the patient's name.
- Send final confirmation:
  "Your appointment is confirmed for [Date] at [Time]."
"""

def run():
    subprocess.run(
        ["droidrun", "run", TASK_PROMPT],
        check=True
    )

if __name__ == "__main__":
    run()
