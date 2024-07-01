from ninja import NinjaAPI

api = NinjaAPI()
# class HelloSchema(Schema):
#     name: str = "world"


@api.get("/hello")
def hello(request, name="world"):
    return f"Hello {name}"

# @api.post("/hey")
# def hello(request, data: HelloSchema):
#     return f"Hello {data.name}"