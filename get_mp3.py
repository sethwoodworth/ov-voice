from googlevoice import Voice

voice = Voice()
voice.login()

download_dir = "."

for message in voice.voicemail().messages:
    message.download.open(download_dir)
