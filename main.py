from definitions import html_header
import json
import flask


def test1():
    with open("./parameters.json", "r") as param:
        data = json.load(param)
        print(f"{data}")
        print(type(data))
        for key in data:
            print(key)
        return (data)


def main():
    print("running test1\n")
    test1()
    with open("./templates/index.html", "w") as index:
        index.write(html_header)
        with open("./parameters.json", "r") as param:
            data = json.load(param)
            for key in data:
                key_object = f'{key}'
                index.write(key_object)
#
#                @app.route(f'/{key}', method=['POST'])
#                def key_objectf():
#                    print(key)

    app.run(debug=True)


app = flask.Flask(__name__,
                  static_url_path='/templates',
                  static_folder='templates',
                  )


@app.route('/')
def index():
#    global serverSideTwigs
    return flask.render_template('index.html')

"""
@app.route('/button1/<twigs>', methods=['POST'])
def button1(twigs):
    print(f"twigs: {twigs}")
    # return str(int(twigs)+1)
    global serverSideTwigs
    serverSideTwigs = serverSideTwigs + 1
    return str(serverSideTwigs)



"""

if __name__ == "__main__":
    main()

