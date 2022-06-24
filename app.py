from flask import Flask, render_template, request,flash
import re
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bishop@2045'

#Inserting a list of models into a dictionary of car makers
carsAndModels = {'Toyota':['Avalon','Camry','Corolla','Prius','Yaris'],
                 'Mercedes Benz':['C300','C400','S65','S600','GLE450'],
                 'Ford':['Fiesta','Focus','Escort','Taurus','Mustang'],
                 'BMW':['X3','X4','X5','X6','M3'],
                 'Honda':['Civic','Accord','CR-V','Pilot','Passport'],
                 'Hyundai':['Accent','Tucson','Elantra','Creta','Palisade'],
                 'Nissan':['Maxima','Frontier','Murano','Armada','Altima'],
                 'Volkswagen':['Taos','Atlas','Tiguan','Jetta','Atlas Sport'],
                 'Chevrolet':['Corvette','Blazer','Colorado','Bolt EUV','Silverado'],
                 'Bentley':['Bentayga EWB Range','Bentayga Range','Flying Spur Range','Continental GT Range','Continental GTC Range']}

#list containing car issues
issues = ["Engine Issue",
          "Gearbox Issue",
          "Body Repairs",
          "Repainting",
          "Wiring Problems",
          "Oil Leakage",
          "Brake Issue"]

#Function to check if reference code matches pattern
def check_refCode(refCode):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6}$"
     # compiling regex
    pat = re.compile(reg)
     # searching regex                 
    mat = re.search(pat, refCode)
    # validating conditions
    if mat:
        flash("Reference code matches pattern.")
    else:
        flash("Reference code does not match pattern.")


SUBMITTED = {}

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template("index.html")
    
        
        
@app.route('/nextPage', methods=['GET', 'POST'])
def nextPage():
    if request.method == 'POST':
        fullname = request.form.get['fullname']
        refCode = request.form.get['refCode']
        email = request.form.get['email']
        maker = request.form.get['maker']
        model = request.form.get['model']
        issue = request.form.get['issue']
        
        check_refCode()
        
        #validating that all fields were filled/checked
        if not fullname:
            return render_template("error.html", message = "Full name field is empty")
        if not refCode:
           return render_template("error.html", message = "Reference code field is empty")
        if not email:
           return render_template("error.html", message = "Email field is empty") 
        if not maker:
           return render_template("error.html", message = "Automobile Maker field is not selected")
        if not model:
            return render_template("error.html", message = "Automobile model field is not selected") 
        if not issue:
            return render_template("error.html", message = "Automobile Issue field is not selected")
        
        SUBMITTED[fullname] = fullname
        SUBMITTED[refCode] = refCode
        SUBMITTED[email] = email
        SUBMITTED[maker] = maker
        SUBMITTED[model] = model
        SUBMITTED[issue] = issue
        
    return render_template("nextPage.html", submitted = SUBMITTED)

if __name__ == '__main__':
    app.run(debug=True)
    