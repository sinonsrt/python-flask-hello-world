from flask import Flask # import

app = Flask(__name__) # instace - __name__ identify the actual module name

@app.route('/') # decorator route identifier
def hello_world(): # function
  return 'Hello, World!' # function return


if __name__ == '__main__': # compare if the file is directly exec and not instantiated
  app.run() # run the app