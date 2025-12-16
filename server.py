from flask import Flask,render_template

app = Flask(__name__) 

@app.route('/')
def index():
    title = 'Home Page'
    return render_template('index.html', title=title)

@app.route('/about')
def about():
    title ='About Page'
    name = 'Limilea'
    email = 'std.67122420216@ubru.ac.th'
    mobile = '0943466071'
    age = 20
    return render_template('about.html',
                           title=title,
                            name=name,
                           email=email,
                           mobile=mobile, 
                           age=age)
@app.route('/favorite/foods')
def favorite_foods(): 
    title = 'Favorite Foods Page'
    foods = ['ข้าวมันไก่','ไก่ทอด' ,'หมูปิ้ง']
    return render_template('favorite_foods.html',
                    title=title,
                    foods=foods)


@app.route('/favorite/spots')
def favorite_spots():
    title = 'favorite Spots Page'
    spots = ['ฟุตบอล' ,'แบคมินตั้น' ,'ปิงปอง']
    return render_template('favorite_spots.html',
                           title=title,
                           spots=spots)
