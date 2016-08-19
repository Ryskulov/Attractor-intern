import cgi


class HTTP_METHODS:
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"


def method_post(request):
    ctype, pdict = cgi.parse_header(request.headers['content-type'])
    if ctype == 'multipart/form-data':
        postvars = {}
        pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
        postvars = cgi.parse_multipart(request.rfile, pdict)
        user_attribute = dict()
        if len(postvars):
            for key in postvars:
                if key != "picture":
                    user_attribute[key] = postvars[key][0].decode("utf-8")
                else:
                    user_attribute[key] = postvars[key][0]
        return user_attribute
    elif ctype == 'application/x-www-form-urlencoded':
        length = int(request.headers['content-length'])
        postvars = cgi.parse_qs(request.rfile.read(length), keep_blank_values=1)
        user_attribute = dict()
        if len(postvars):
            for key, value in postvars.items():
                user_attribute[key.decode("utf-8")] = value[0].decode("utf-8")
        return user_attribute
    else:
        postvars = {}
