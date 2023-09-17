from taipy.gui import Gui
from taipy.gui import Html

page = Html("""
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
            <taipy:button class="button green" on_action="button_action_function_name">Easy</taipy:button>
            <taipy:button class="button yellow" on_action="button_action_function_name">Medium</taipy:button>
            <taipy:button class="button red" on_action="button_action_function_name">Hard</taipy:button>
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

Gui(page).run(port=5001, use_reloader=True, theme=my_theme)
