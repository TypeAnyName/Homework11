import utils
from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates")


@app.route('/')
def candidate_list():
    candidate_full_list = utils.load_candidate_from_json()
    return render_template("list.html", candidate_full_list=candidate_full_list)


@app.route("/candidate/<int:uid>")
def page_profile(uid):
    candidate_by_id = utils.get_candidate(uid)
    return render_template("single.html", candidate_by_id=candidate_by_id)


@app.route("/search/<name>")
def show_names(name):
    candidate = utils.get_candidates_by_name(name)
    lenght = len(candidate)
    return render_template('search.html', candidate=candidate, lenght=lenght)


app.run()
