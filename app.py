from flask import Flask, render_template_string, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        try:
            rendered_template = render_template_string(email)
         
            return render_template('thankyou.html',email=rendered_template)
        
        except Exception as e:
            return f"Erreur : {e}"
    return render_template('contact.html')
@app.route('/about')
def about():
     
        return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)