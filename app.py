from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html",
        title="EMROS | Smart Hotel Technology & Energy Management"
    )

@app.route("/privacy-service")
def privacy():
    return render_template("privacy.html",
        title="Privacy & Service Communication System | EMROS"
    )

@app.route("/guest-presence-system")
def presence():
    return render_template("presence.html",
        title="Guest Presence System for Hotels | EMROS"
    )

@app.route("/guest-room-management-system")
def grms():
    return render_template("grms.html",
        title="Guest Room Management System (GRMS) | EMROS"
    )

@app.route("/energy-management-system")
def energy():
    return render_template("energy.html",
        title="Hotel Energy Management System | EMROS"
    )

@app.route("/contact")
def contact():
    return render_template("contact.html",
        title="Contact EMROS | Smart Hotel Technology"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

#if __name__ == "__main__":
#    app.run(debug=True)
