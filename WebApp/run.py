from plager import create_app

app = create_app() #Create an instance of the Flask app.

if __name__ == '__main__':
    app.run(host='localhost', port=4444, debug=True) #Run web server on localhost:8080.