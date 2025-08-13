#  Bot & Spam Detection with DBSCAN & Flask

##  Overview

This project uses the **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)** algorithm for unsupervised outlier detection to classify chat messages as either **"Human"** or **"Bot/Spam."** DBSCAN is effective for this task because it identifies dense regions of data points (which would represent human-like behavior) and marks points that lie alone in low-density regions as noise or outliers (which can be interpreted as bot/spam activity). The model is deployed via a **Flask web application** with a simple HTML and CSS interface.

-----

##  Features

  - **DBSCAN Clustering** model for unsupervised outlier detection.
  - **Flask backend** for serving predictions.
  - **HTML/CSS frontend** for a clean user input form.
  - Classifies users as "Human" or "Bot/Spam."
  - **`StandardScaler`** for data normalization.

-----

##  Project Structure

```
bot_detection_dbscan/
│
├── app.py               # Flask app, includes model training & prediction logic
├── templates/
│   └── index.html       # Input form and result display
├── static/
│   └── style.css        # CSS styles for the frontend
├── dbscan.csv           # Dataset for training
└── README.md            # Project documentation
```

-----

##  Requirements

To install the necessary dependencies, use `pip`:

```bash
pip install Flask pandas numpy scikit-learn
```

-----

##  Dataset Description

The dataset (`dbscan.csv`) contains three key features representing chat message behavior. The DBSCAN algorithm will use these features to find dense regions and identify outliers.

**Columns:**

  - `messages_per_minute`: Number of messages sent per minute.
  - `avg_word_length`: The average length of words in a message.
  - `links_per_message`: The number of links included in each message.

-----

##  How It Works

### Web Application (`app.py`)

  - The Flask app loads the `dbscan.csv` dataset directly.
  - It normalizes the data using `StandardScaler`.
  - The `DBSCAN` model is then trained with `eps=1.0` and `min_samples=2`.
  - The root route (`/`) displays an input form (`index.html`) where a user can enter their messaging metrics.
  - Upon form submission, the app scales the new input data and uses the trained `DBSCAN` model to predict its cluster.
  - If the prediction is `-1`, the user is flagged as an outlier and the app returns **"Bot/Spam."** Otherwise, it returns **"Human."**

-----

##  Running the Project

1.  **Run the Flask App**
    ```bash
    python app.py
    ```
2.  **Open in Browser**
    Navigate to `http://127.0.0.1:5000/` to access the application.

-----

##  Screenshots

---
Home Page

<img width="500" height="332" alt="Screenshot 2025-08-13 113701" src="https://github.com/user-attachments/assets/3da8d22e-1e79-4ec2-8a73-7aad894346f9" />

---

Prediction Result

<img width="495" height="383" alt="Screenshot 2025-08-13 113719" src="https://github.com/user-attachments/assets/03a3d73e-ae58-486a-8adb-1ba1337b1a4d" />
