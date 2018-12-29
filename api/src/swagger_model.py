#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time    : 12/29/18 2:43 PM
# @Author  : zhanfengchen
# @Site    : 
# @File    : swagger_model.py
# @Software: PyCharm
from flask_restplus import fields, Model

__all__ = ['SwaggerModel']


class SwaggerModel(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SwaggerModel, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self._api = None

        self._common_output_dic = {
            "start_time": fields.String(),
            "cost_time": fields.Float(),
            "message": fields.String(),
            "success": fields.Boolean()
        }

        default_value =

        self._title_id_pair_model = self._assemble_and_regist_model("title_id_pair",
                                                                    [{"text": fields.String(default=default_value),
                                                                      "id": fields.Integer()}])
        self._title_input_dic = {"text": fields.String(default=default_value), }

        self._control_args = {
            "strategy": fields.String(default='short'),
            "skill_number": fields.String(default='10000')
        }

        self._output_data_dic = {""}

        self._models = {}
        self._build_models()

    def _assemble_and_regist_model(self, model_name, dic_lis):
        _new_dic = {}
        for dic in dic_lis:
            _new_dic.update(dic)
        model = Model(model_name, _new_dic)
        self._models[model_name] = model
        return model

    def _build_models(self):
        # titles_input
        _batch_input_data_dic = {"data": fields.List(fields.Nested(self._title_id_pair_model))}
        _ = self._assemble_and_regist_model("titles_input", [_batch_input_data_dic, self._control_args])

        # titles_output
        _output_data_model = self._assemble_and_regist_model("output_data_model",
                                                             [{"output": self._output_data_dic, "id": fields.Integer}])
        _output_lis_dic = {"data": fields.List(fields.Nested(_output_data_model))}
        _ = self._assemble_and_regist_model("titles_output", [_output_lis_dic, self._common_output_dic])

        # title input
        _ = self._assemble_and_regist_model("title_input", [self._title_input_dic, self._control_args])

        # title output
        _ = self._assemble_and_regist_model("title_output", [self._output_data_dic, self._common_output_dic])

    def _regist(self):
        for key, model in self._models.iteritems():
            self._api.models[key] = model

    def set_api(self, api):
        self._api = api
        self._regist()

    def get_model(self, model_name):
        return self._models.get(model_name, None)
