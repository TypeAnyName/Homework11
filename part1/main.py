from flask import Flask, render_template

app = Flask(__name__,template_folder="../templates")


@app.route('/', )
def page_index():
    name = "Ivan"
    number = "132134"
    return render_template("profile.html", name=name, number=number)


app.run()
