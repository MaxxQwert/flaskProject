from flask import Blueprint, render_template
from werkzeug.exceptions import BadRequest

service_app = Blueprint("service_app", __name__)

SERVICES = {
    1: 'Repair',
    2: 'Firmware',
    3: 'Cleaning',
}


@service_app.route("/", methods=["GET", "POST"])
def services_list():
    return render_template("services/services_list.html", services=SERVICES)


@service_app.route("/<int:service_id>/")
def services_detail(service_id: int):
    try:
        service_name = SERVICES[service_id]
    except KeyError:
        raise BadRequest(f"Invalid product id #{service_id}")

    return render_template(
        "services/detail.html",
        service_id=service_id,
        service_name=service_name,
    )
