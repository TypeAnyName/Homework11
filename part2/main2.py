import utils
from flask import Flask, render_template

app = Flask(__name__,template_folder="../templates")


@app.route('/', )
def candidate_list():
    candidate_full_list = utils.load_candidate_from_json()
    return render_template("list.html", candidate_full_list=candidate_full_list)


app.run()
