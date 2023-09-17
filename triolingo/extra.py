from taipy.gui import Gui
import speechToText

page = """
# Getting started aodin Taipy GUI

<|Error|button|class_name=error|on_action=recordAudio|>

<|Error|button|class_name=error|on_action=callAPI|>

"""

def recordAudio():
    speechToText.recordSpeech()

def callAPI():
    speechToText.recordSpeech()

Gui(page).run(port=5001, use_reloader=True)
