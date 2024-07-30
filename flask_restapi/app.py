from flask import Flask

server = Flask(__name__)


class APIConfig:
    API_TITLE = "TODO API"
    API_VERSION = "V1"
    OPENAPI_VERSION = "3.0.3"
    OPENAPU_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/docs"
    OPENAPI_SWAGGER_UI_URL = ""
    OPENAPI_REDOC_PATH = "/redoc"
    OPENAPI_REDOC_UI_URL = ""


server.config.from_object(APIConfig)


api = Api(server)

todo = Blueprint()

todo = Blueprint("todo", "todo", url_prfix = "/todo", description= "TODO API")

task = [
    {
        "id":uuid.UUID(""),
        "created": datetime.now(timezone.utc),
        "compleated": False,
        "task": "Create Flask Api."     
    }
]

class CreateTask(Schema):
    task = field.List(fields.Nested(Tasks))


class UpdateTask(CreateTask):
    compleated = field.Bool()

class Task(UpdateTask):
    id = fields.UUID()
    created = fields.dateTime()

class SortByEnum(enum.Enum):
    task =task
    created = created

class SortDirectionEnum(enum.Enum):
    asc = "asc"
    desc = "desc"


class ListTaskParameters(schema):
    order_by = fields.Enum()
    order = fields.Enum(SortDirectionEnum, load_default=SortDirectionEnum)





@todo.route("/tasks")

 class TodoCollection(MethodView):

    @todo.arguments(ListTaskParameters, location="querry")
    @todo.response(status_code = 200, schema = Task)
    def get(self, parameters):
        return {
            "tasks": sorted(
                tasks,
                key = lambda task: task[parameters["order_by"].value]
                reverse = parameters["order"] == SortDirectionEnum.desc

            )
        }

    @todo.arguments(CreateTask)
    @todo.response(status_code = 201, schema = Task)
    def post(self, task):
        task["id"] = uuid.uuid4()
        task["created"] = datetime.now(timezone.utc)
        task["compleated"] = False

    

    
@api.route("/tasks/<uuid:task_id>")
class TodoTask(MethodView):
    @todo.response(status_code=200, schema=Task)
    def get(self, task_id):
        for task in tasks:
            if task["id"] == task_id:
                return task
        abort(404, f"Task {task_id} not found")")
    
    @todo.arguments(UpdateTask)
    @Todo.response(status_code=200, schema = Task)
    def put(self, task_id):
        for task in tasks:
            if task["id"] == task_id:
               if task["id"] == task_id:
                    task["compleate"] = payload["completed"]
                    task["task"] = payload["task"]
                return task
        abort(404, f"Task {task_id} not found)


    
    @todo.response(status_code=204)
    def delete(self, task_id):
        for index, task in enumerate(tasks):
            if task["id"] == task_id:
                task.pop(index)
                return
        abort(404, f"Task with task id {task_id} not found")
        



api.register_blueprint(todo)


