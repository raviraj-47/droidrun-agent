# Agent Workflow

1. Agent starts on Android home screen
2. Opens WhatsApp
3. Reads unread messages on screen
4. Uses reasoning to detect task-related intent
5. If task is detected:
   - Opens app drawer
   - Opens Tasks app
   - Creates a reminder
6. If no task is detected:
   - Stops execution

The agent makes decisions dynamically based on screen content,
without using hardcoded UI automation.
