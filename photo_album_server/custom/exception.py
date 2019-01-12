# -*- coding: utf-8 -*-
"""
这个脚本是用来处理自定义异常
"""
import rest_framework
from rest_framework.response import Response
from rest_framework.exceptions import APIException


class CustomException:
    """ 这个类的作用是用来区分错误是哪个类
    """

    exception_code_dict = {
        1062: "数据已经存在"
    }

    exception_cls_dict = {}

    def __error_type(self, exc):
        """ 这个类的作用是判断错误情况
        :param exc:
        :return:
        """
        back_error = None
        error_value = exc.args[0]
        if isinstance(error_value, (int,)):
            back_error = self.exception_code_dict.get(exc.args[0])
        elif isinstance(error_value, (str,)):
            back_error = self.exception_cls_dict.get(exc.args[0])

        if not back_error:
            back_error = "操作错误"
        return back_error

    def handel(self, exc, context):
        """ 这个类的作用是用来判断错误类型

        :param exc:
        :param context:
        :return:
        """
        error_zh = self.__error_type(exc=exc)

        detailed_error = {}
        if isinstance(exc, (rest_framework.exceptions.ValidationError,)):
            if isinstance(exc.detail, (dict,)):
                # err_fields = ["string", "code"]
                for k, v in exc.detail.items():
                    detailed_error[k] = v[0]

        return Response(
            data={"message": error_zh, "detailed": detailed_error}
            , status=exc.status_code
        )


ce = CustomException()


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.

    # response = exception_handler(exc, context)
    # # Now add the HTTP status code to the response.
    # print(response)
    # if response is not None:
    #     response.data['message'] = response.data['detail']
    #     del response.data['detail']
    #     return response

    return ce.handel(exc, context)


class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = "服务暂时不可用"


class PageNoFund(APIException):
    status_code = 404
    default_detail = "页面不存在"
