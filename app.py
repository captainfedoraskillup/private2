from backend import app

if __name__ == '__main__':  # Script executed directly?
    print("pictures microservice. Uses S2I to build the application.")
    app.run(host="0.0.0.0", port=8080, debug=True,use_reloader=True)  # Launch built-in web server and run this Flask webapp
