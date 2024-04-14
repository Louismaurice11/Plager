from plager import create_app

app = create_app() #Create an instance of the Flask app.

if __name__ == '__main__':
    app.run() #Run web server.
