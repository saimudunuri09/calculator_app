from flask import Flask, request, render_template_string
from calculator import add_numbers

app = Flask(__name__)

html_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Simple Addition App</title>
</head>
<body>
    <h2>Add Two Numbers</h2>
    <form method="POST">
        <label>Enter number A:</label>
        <input type="number" name="a" required><br><br>

        <label>Enter number B:</label>
        <input type="number" name="b" required><br><br>

        <button type="submit">Calculate</button>
    </form>

    {% if result is not none %}
        <h3>Result = {{ result }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        a = float(request.form.get("a"))
        b = float(request.form.get("b"))
        result = add_numbers(a, b)

    return render_template_string(html_page, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
