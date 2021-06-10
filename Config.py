from flask import Blueprint, render_template

second = Blueprint("second", __name__, static_folder="static", template_folder="template")

@second.route("/route")
@second.route("/")
def route():
    # Render the about page
    titleMsg = "Route page"
    return render_template("about.html", title=titleMsg)


