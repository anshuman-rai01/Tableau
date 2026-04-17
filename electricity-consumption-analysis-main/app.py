from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Yeh raha aapka modified Tableau URL
    tableau_url = "https://public.tableau.com/views/Tableau_SkillWallet/Dashboard1?:embed=yes&:showVizHome=no"
    
    return render_template('index.html', url=tableau_url)

if __name__ == '__main__':
    app.run(debug=True, port=5000)