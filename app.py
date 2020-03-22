"""
Date:	20/03/2020
Author:	Gerrit Lang

Main App with all Endpoints
"""


from flask import Flask, request, flash, redirect, jsonify, render_template
import src.core as Core
from src.forms.offer import OfferForm

# pylint: disable=invalid-name
app = Flask(__name__)
app.config["SECRET_KEY"] = "gdxgdgfdfgdfggfdgfgfdgfjgjgj"


@app.route("/")
def index():
    """
    index page of our service

    Returns:
        template: html index
    """
    return render_template("index.html")


@app.route("/offers", methods=["GET", "POST"])
@app.route("/offers/<offer_id>", methods=["GET"])
def offers(offer_id=None):
    """
    endpoint for offers

    Args:
        offer_id (str, optional): id of the offer. Defaults to None.

    Returns:
        list or dict: requested offers
    """
    form = OfferForm()
    if form.validate_on_submit():
        flash("Offer created: {}".format(form.title.data))
        Core.create_offer(form.title.data)
        return redirect("/offers")
    if request.method == "GET":
        if offer_id:
            return jsonify(Core.get_matches(offer_id))
        else:
            return render_template("offer.html", offer_table=Core.get_matches('1'), form=form)
    return "Not implemented"


@app.route("/employees", methods=["GET", "POST"])
@app.route("/employees/<employee_id>", methods=["GET"])
def employees(employee_id=None):
    """
    endpoint for employees

    Args:
        employee_id (str, optional): id of the employee. Defaults to None.

    Returns:
        list or dict: requested employees
    """
    if request.method == "GET":
        if employee_id:
            return jsonify(Core.get_employees(employee_id))
        return render_template("employee.html")


@app.route("/employers", methods=["GET", "POST"])
@app.route("/employers/<employer_id>", methods=["GET"])
def employers(employer_id=None):
    """
    endpoint for employer

    Args:
        employer_id (str, optional): id of the employer. Defaults to None.

    Returns:
        list or dict: requested employers
    """
    if request.method == "GET":
        if employer_id:
            return jsonify(Core.get_employers(employer_id))
        return render_template("employer.html")


if __name__ == "__main__":
    app.run()
