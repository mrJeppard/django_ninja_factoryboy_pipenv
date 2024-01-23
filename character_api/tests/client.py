from django.test.client import MULTIPART_CONTENT, Client

class APIClient(Client):
    _post = Client.post
    _put = Client.put
    _patch = Client.patch
    _delete = Client.delete

    def __convert_format_arg(self, format, content_type) -> str:
        if format == "json" and content_type is None:
            content_type = "application/json"
        elif format == "multipart" and content_type is None:
            content_type = MULTIPART_CONTENT
        elif content_type is not None:
            pass
        else:
            content_type = MULTIPART_CONTENT
        return content_type

    def post(self, path, data=None, format=None, content_type=None, **extra):
        content_type = self.__convert_format_arg(format, content_type)
        return self._post(path, data, content_type, **extra)

    def put(self, path, data=None, format=None, content_type=None, **extra):
        content_type = self.__convert_format_arg(format, content_type)
        return self._put(path, data, content_type, **extra)

    def patch(self, path, data=None, format=None, content_type=None, **extra):
        content_type = self.__convert_format_arg(format, content_type)
        return self._patch(path, data, content_type, **extra)

    def delete(self, path, data=None, format=None, content_type=None, **extra):
        content_type = self.__convert_format_arg(format, content_type)
        return self._delete(path, data, content_type, **extra)
