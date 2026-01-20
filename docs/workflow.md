# Workflow – Doctor Appointment Automation

## Input Source
- WhatsApp messages from patients requesting appointments.

---

## Processing Logic
1. Read latest WhatsApp message.
2. Extract patient name, date, and time.
3. Request missing information if needed.
4. Normalize time to 24-hour format.

---

## Data Store
- Notion pages organized by date (DD-MM-YYYY).
- Each page contains a table with:
  - Time
  - Name

---

## Decision Handling
- Empty slot → book immediately.
- Filled slot → suggest nearest available time.
- User confirmation required before alternate booking.

---

## Output
- Updated Notion appointment table.
- WhatsApp confirmation message sent to the user.

---

## Failure Handling
- Retry app open once.
- Adapt to UI changes visually.
- Ask user for clarification if uncertain.
