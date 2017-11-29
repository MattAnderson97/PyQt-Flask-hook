from flask import Flask, render_template

# instantiate Flask
app = Flask(__name__)
# add support for .pug templates
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')


# @ denotes a decorator, extends functionality of a given function or method
# while keeping code inside the function/method simple
# @app.route() provided by flask
# "/" tells flask this is the default route that should be loaded if no page is provided (http(s)://<domain>/)
# can put specific locations such as "/img" to catch http(s)://<domain>/img
@app.route("/")
def index():
    # render index.html template from templates folder and return it
    return render_template("index.html")


# check to see if this is the main program
if __name__ == "__main__":
    # run flask (port 5000)
    app.run()