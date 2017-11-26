from flask import Flask, request, jsonify, make_response


class API():

    app = Flask('instagram_api')



    def __init__(self):
        pass


    # error handling
    @staticmethod
    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

    # Running the flask server
    def run(self,debug=True,port=5000):
        self.app.run(host="0.0.0.0",port=port, debug=debug,threaded=True)


ab = API()

ab.run(True)
