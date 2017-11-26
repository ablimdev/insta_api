from flask import Flask, request, jsonify, make_response
import requests
import re
import json

class API():

    app = Flask('instagram_api')



    def __init__(self):
        pass

    @staticmethod
    @app.route('/', methods=['GET'])
    def landing():
        results = {
            'status':'here'
        }
        return jsonify(results)
        #flask version of json.loads

    @staticmethod
    @app.route('/user/<string:instagramuser>', methods=['GET'])
    def get_user(instagramuser):
        try:
            r = requests.get("https://instagram.com/" + instagramuser)
            #r = requests.get("https://instagram.com{}".format(instagramuser))
            html_page = r.text

            result = re.search('window._sharedData = (.*);</script>', html_page)


            insta_json = json.loads(result.group(1))

            insta_user  = insta_json['entry_data']['ProfilePage'][0]['user']

            api_results = {
                'biography': insta_user['biography'],
                'external_url':insta_user['external_url'],
                'followed_by':insta_user['followed_by']['count'],
                'follows':insta_user['follows']['count'],
                'full_name':insta_user['full_name'],
                'id':insta_user['id'],
                'profile_pic':insta_user['profile_pic_url'],
                'username':insta_user['username']
            }
            return jsonify(api_results)

        except:
            error_message = {
            'msg': 'user does not exist'
            }

            return jsonify(error_message)

    # @staticmethod
    # @app.route('/<string:myVar>', methods=['GET'])
    # def generic(myVar):
    #     results = {
    #         'status':myVar
    #     }
    #     return jsonify(results)

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
