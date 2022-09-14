import logging


def should_abort_request(req):

    if req.resource_type == "image":
        logging.log(logging.INFO, f"Ignoring Image {req.url}")
        return True
    if req.method.lower() == 'post':
        logging.log(logging.INFO, f"Ignoring {req.method} {req.url} ")
        return True

    return False

