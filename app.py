import pandas as pd
from flask import Flask, render_template
app = Flask(__name__)
df = pd.read_csv("profilo.csv")
user = df.iloc[0].to_dict()
print(user)
@app.route('/')
def home():
    return render_template("index.html", df = user)

@app.route('/modifica_profilo', methods=['GET','POST'])
def modifica_profilo():
    return render_template("modifica.html")

if __name__ == '__main__':
    app.run(debug=True, port=5001)