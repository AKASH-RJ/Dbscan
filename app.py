from flask import Flask, render_template, request
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load and prepare dataset
df = pd.read_csv("dbscan.csv")
X = df.values
X_scaled = StandardScaler().fit_transform(X)

# Train DBSCAN model
model = DBSCAN(eps=1.0, min_samples=2)
model.fit(X_scaled)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            mpm = float(request.form["messages_per_minute"])
            awl = float(request.form["avg_word_length"])
            lpm = float(request.form["links_per_message"])
            user_data = [[mpm, awl, lpm]]
            user_scaled = StandardScaler().fit(X).transform(user_data)
            cluster = model.fit_predict(user_scaled)[0]
            prediction = "Bot/Spam" if cluster == -1 else "Human"
        except:
            prediction = "Invalid input!"
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
