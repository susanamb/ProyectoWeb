from flask import Flask, redirect, url_for

app = Flask(__name__)

# default route
@app.route("/")
def home():
    return "Hello! this is a FLASK server! <h1>HOLAMUNDO</h1>"

#route that sends a parameter on the url
@app.route("/<name>")
def user(name): #recieve the parameter
    return f"Helloo {name}, your name is a parameter"
    
@app.route("/admin")
def admin():
    return redirect(url_for("home"))

    #run the server
if __name__ == "__main__":
    print("running....")
    app.run()