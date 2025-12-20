from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = 'Home Page'
    return render_template('index.html', title=title)

@app.route('/about')
def about():
    title = 'About Page'
    name = 'Limilea'
    email = 'std.67122420216@ubru.ac.th'
    mobile = '0943466071'
    age = 20
    return render_template('about.html',
                            name=name,
                            email=email,
                            mobile=mobile,
                            age=age)

@app.route('/favorite/foods')
def favorite_foods():
    title = 'Favorite Foods'
    foods = ['ตำป่า', 'ข้าวมันไก่', 'ไก่ทอด', 'ข้าวผัด', 'ส้มตำไก่อย่าง']
    return render_template('favorite_foods.html',
                            foods=foods)

@app.route('/favorite/spots')
def favorite_spots():
    title = 'Favorite Spots'
    spots = ['ปิงปอง', 'ฟุตบอล', 'บาสเก็ตบอล']
    return render_template('favorite_spots.html',
                            spots=spots)

@app.route('/favorite/movies')
def favorite_movies():      
    title = 'Favorite Movies'
    movies = ['the witcher', 'fast and furious', 'transformers', 'john wick', 'spider-man']
    return render_template('favorite_movies.html',  
                            movies=movies)  

if __name__ == "__main__":
    app.run(debug=True)
