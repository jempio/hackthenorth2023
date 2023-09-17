from taipy.gui import Html
from reader import readQuote
from reader import readScore

pageThree = Html(f"""
    <div class="container">
        <div class="game"> Pronunciation Game </div>
        <div class="middleGroup">
            <div class="resultsFlex">
                <div class="resultsText">Your Results</div>
                    <div class="scoreContainer">
                    <div class="score">{readScore()}</div>
                    <div class="score2">Accuracy</div>
                </div>
                <div class="listenContainer">
                    <taipy:button class="playButton" on_action="listen_to_ai">.</taipy:button>
                    <div class="AITidbit">Listen to AI say this sentence</div>
                </div>
                <div class="listenContainer">
                    <taipy:button class="playButton" on_action="listen_to_sentence">.</taipy:button>
                    <div class="AITidbit">Listen to how you said this sentence</div>
                </div>
            </div>
            <div class="realSentence">{readQuote()}</div>
        </div>
        <div class="options">
            <taipy:button class="bubbleRed" on_action="retry_sentence">Retry Sentence</taipy:button>
            <taipy:button class="bubbleGreen" on_action="get_new_sentence">New Sentence</taipy:button>
        </div>
    </div>
"""
)