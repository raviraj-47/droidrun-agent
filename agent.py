import subprocess

GOAL = (
    "Open whatsapp, check for any new messages, "
    "if there is any new message which indicates any task to do, "
    "then open app drawer and search for 'Tasks' app and set a reminder "
    "be careful while choosing date and time"
    "so that I can't forget the task."
)

command = [
    "droidrun",
    "run",
    GOAL,
    "--config",
    r"C:\Users\HP\droidrun-whatsapp-agent\config.yaml"
]

subprocess.run(command)
