# Doctor Appointment Automation (WhatsApp → Notion) using Droidrun

## Overview
This project is a **real-world mobile automation** built using the **Droidrun Framework**.  
It automates doctor appointment scheduling by reading requests from **WhatsApp** and updating a **Notion-based appointment table** directly on an Android device.

The automation acts as a virtual appointment manager that collects missing information, avoids scheduling conflicts, and sends confirmations — without manual intervention.

---

## Problem Statement
Doctors and clinics often receive appointment requests via WhatsApp.  
Manually managing these requests leads to:
- Scheduling errors
- Missed messages
- Double bookings
- High administrative overhead

This project automates the entire workflow using mobile UI automation.

---

## What the Automation Does
1. Opens WhatsApp and reads the latest appointment request.
2. Extracts:
   - Patient name
   - Preferred date
   - Preferred time
3. Requests missing details and waits until all information is received.
4. Converts appointment time to **24-hour format**.
5. Opens Notion and navigates to the correct date page (`DD-MM-YYYY`).
6. Finds the appointment table with **Time** and **Name** columns.
7. Books the appointment if the slot is free.
8. Suggests an alternate time if the slot is occupied.
9. Sends confirmation back to the user via WhatsApp.

---

## Use Case Type
**B2B Automation**
- Clinics
- Hospitals
- Independent doctors
- Healthcare assistants

---

## Tech Stack
- **Droidrun Framework**
- **Android ADB**
- **WhatsApp (Mobile App)**
- **Notion (Mobile App)**
- **Python 3**



