from taipy.gui import Gui
from taipy.gui import Html

recordPage = Html("""
    <div class="container record">
        <h3 class="recordTitle"> Pronunciation Game </h3>
        <div class="subContainer2">
            <div class="recordContainer">
                  <div class="bubble">Easy Sentence</div>
                  <h2 class="greenText">Record Yourself Saying</h2>
            </div>
            <div class="sentence">The metal-carbon bond in organometallic compounds is generally highly covalent.</div>
        </div>
        <div class="audioButtonContainer">
            <h4 class="lightRedText">Record Audio</h4>
            <div class="redCircle"></div>
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

Gui(recordPage).run(port=5002, use_reloader=True, theme=my_theme)
