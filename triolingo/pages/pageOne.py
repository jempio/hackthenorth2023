from taipy.gui import Html

pageOne = Html("""
    <div class="container">
        <h1> Pronunciation Game </h1>
        <div class="subContainer">
            <h2> How to Play: </h2>
            <ol>
                <li>Click generate sentence and you will be given a sentence to say </li>
                <li>Record yourself saying the sentence</li>
                <li>You will be scored on how correct your pronunciation is</li>
            </ol>
        </div>
            <h2>Choose Your Difficulty</h2>
        <div class="buttonContainer">
            <taipy:button class="button green" on_action="easy_callback">Easy</taipy:button>
            <taipy:button class="button yellow" on_action="medium_callback">Medium</taipy:button>
            <taipy:button class="button red" on_action="hard_callback">Hard</taipy:button>
        </div>
    </div>
            

"""
)