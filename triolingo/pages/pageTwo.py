from taipy.gui import Html
from reader import readQuote
from reader import readDiff

pageTwo = Html(f"""
    <div class="container record">
        <div class="game"> Pronunciation Game </div>
        <div class="subContainer2">
            <h2 class="greenText">Record Yourself Saying</h2>
                <div class="recordContainer">
                    <div class="bubble">{readDiff()} Sentence</div>
                    <div class="sentence"> {readQuote()} </div>
                </div>
        </div>
        <div class="audioButtonContainer">
            <h4 class="lightRedText">Record Audio</h4>
            <taipy:button class="redCircle" on_action="record_callback"> . </taipy:button>
        </div>
    </div>
"""
)
