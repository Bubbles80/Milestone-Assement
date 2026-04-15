from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World from Docker 🚀"

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        return f"Hello {name}, welcome to Docker!"
    
    return """
    <form method="POST">
        <input name="name" placeholder="Enter your name" />
        <button type="submit">Submit</button>
    </form>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
