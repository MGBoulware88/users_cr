from flask import Flask, render_template, request, redirect, session
from user import User
app = Flask(__name__)
secret_key = "CHANGEME"

@app.route("/")
def index():
    # call the get_all_users(cls, data) classmethod to populate the HTML
    users = User.get_all_users()
    print(users)
    for user in users:
        print(user.first_name, user.last_name)
    return render_template("index.html", users = users)


@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/users/create", methods=['POST'])
def create_user():
    User.create(request.form)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)