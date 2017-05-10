from roomfinder import create_app


app = create_app()

@app.route('/home')
def home():
    return this is gome

app.run(host='localhost',port=8888, debug=True)


