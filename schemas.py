from marshmallow import Schema, fields, validate


class Data(Schema):
    data = fields.String(required=True)


class ErrorResponse(Schema):
    status = fields.String()
    message = fields.String()


class PostResponse(Schema):
    status = fields.String()
    message = fields.String()


class GetResponse(Schema):
    status = fields.String()
    message = fields.String()
