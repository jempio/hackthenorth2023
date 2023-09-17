from taipy.gui import Gui
from taipy.gui import Html

recordPage = Html("""
    <div class="container">
        <div class="game"> Pronunciation Game </div>
        <div class="middleGroup">
            <div class="resultsFlex">
                <div class="resultsText">Your Results</div>
                <div class="scoreContainer">
                    <div class="score">95%</div>
                    <div class="score2">Accuracy</div>
                </div>
                <div class="listenContainer">
                    <taipy:button class="playButton" on_action="button_action_function_name">.</taipy:button>
                    <div class="AITidbit">Listen to AI say this sentence</div>
                </div>
                <div class="listenContainer">
                    <taipy:button class="playButton" on_action="button_action_function_name">.</taipy:button>
                    <div class="AITidbit">Listen to how you said this sentence</div>
                </div>
            </div>
            <div class="realSentence">The metal-carbon bond in organometallic compounds is generally highly covalent.</div>
        </div>
        <div class="options">
            <taipy:button class="bubbleRed" on_action="button_action_function_name">Retry Sentence</taipy:button>
            <taipy:button class="bubbleGreen" on_action="button_action_function_name">New Sentence</taipy:button>
        </div>
    </div>
"""
)
...
my_theme = {
  "palette": {
    "background": {"default": "#F9F5ED"},
    "primary": {"main": "#66283B"}
  }
}
...

Gui(recordPage).run(port=5003, use_reloader=True, theme=my_theme)
