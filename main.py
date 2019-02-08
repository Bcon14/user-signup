from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


app = Flask(__name__)
app.config['DEBUG'] = True      


@app.route("/")
def index():
    template = jinja_env.get_template('user-form.html')
    return template.render()




@app.route("/welcome", methods=['POST'])
def welcome():
    template = jinja_env.get_template("welcome.html")
    return template.render()




def isSame(first, second):
    try:
        if str(first) == str(second):
            return True
    except ValueError:
        return False




@app.route('/', methods=['POST'])
def validate():
    user_name = request.form['username']
    password = request.form['password']
    v_password = request.form['verify']
    email = request.form['email']

    user_error = ''
    password_error =''
    vpassword_error =''
    email_error = ''

    if user_name == '':
        user_error = 'Not a valid username'
    if password =='':
        password_error = 'Not a valid password'
    if isSame(password,v_password) == False:
        vpassword_error = 'passwords do not match'
    if v_password == '':
        vpassword_error = 'passwords do not match'
    

    if email =='':
        email_error = ''
    else:
        for char in email:
            if char == '@':
                email_error ==''
            else:
                email_error = 'Email not vaild'


    
    if user_error == '' and password_error == '' and vpassword_error == '' and email_error == '':
        return render_template('/welcome.html', username=user_name)
    else:
        template = jinja_env.get_template('user-form.html')
        return template.render(user_error=user_error,
            password_error=password_error,
            vpassword_error=vpassword_error,
            email_error=email_error,
            username=user_name)
    
    

app.run()