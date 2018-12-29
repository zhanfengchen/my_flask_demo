#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time    : 12/29/18 11:43 AM
# @Author  : zhanfengchen
# @Site    : 
# @File    : main.py
# @Software: PyCharm
from flask import Flask, request
import logging.config
import traceback
from flask_cors import CORS
from flask_restplus import Api, Resource
from src.respone_helper import time_dector, msg_dector
from src.conf import logging_filename
from src.swagger_model import SwaggerModel


logging.config.fileConfig(logging_filename)
loggerFile = logging.getLogger("out2file")


app = Flask(__name__)
CORS(app)
api = Api(app, doc='/doc/')


swagger_model = SwaggerModel()
swagger_model.set_api(api)

position_batch_input = swagger_model.get_model("")
position_batch_output = swagger_model.get_model("")

position_input = swagger_model.get_model("")
position_output = swagger_model.get_model("")

@api.route('/position/batch_action')
class PositionBatchAction(Resource):
    def _get_data(self):
        # para in json
        data = request.get_json()
        # para in data
        data = request.get_data()
        return data

    @time_dector.new_add_time
    @msg_dector.add_new_message
    def __clean(self):
        success_flag, out_data = True, []
        try:
            position_data = self._get_data()
            result_dicts =
        except Exception as e:
            success_flag = False
            loggerFile.error('-------------------ERROR----------------------\n' +
                             traceback.format_exc())

        return {'data': out_data,
                'success': success_flag}

    @api.expect(position_batch_input)
    @api.marshal_with(position_batch_output)
    def post(self):
        result = self.__clean()
        return result


@api.route('/position/action')
class PositionAction(Resource):
    def _get_data(self):
        # para in json
        data = request.get_json()
        # para in data
        data = request.get_data()
        return data

    @time_dector.new_add_time
    @msg_dector.add_new_message
    def __process(self):
        success_flag, out_data = True, []
        try:
            position_data = self._get_data()
            result_dicts =
        except Exception as e:
            success_flag = False
            loggerFile.error('-------------------ERROR----------------------\n' +
                             traceback.format_exc())

        return {'data': out_data,
                'success': success_flag}

    @api.expect(position_input)
    @api.marshal_with(position_output)
    def post(self):
        result = self.__process()
        return result



if __name__ == '__main__':
    loggerFile.info('Start!')
    # fill your port
    app.run(debug=False, host='0.0.0.0', port=)
