from flask import Flask, render_template 
app = Flask(_name_) 
@app.route('/') 
def index(): 
    """ 
    Renders the main index.html template for the Smart Register application. 
    """ 
    return render_template('index.html') 
 
if _name_ == '_main_': 
    # Run the Flask application in debug mode for development 
    app.run(debug=True)
