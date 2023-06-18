from flask_restx import Namespace, Resource, fields, reqparse
from services import StudentService

student_ns = Namespace("students", description="Students operations")


student_model = student_ns.model(
    "Student",
    {
        "id": fields.String(readOnly=True, description="The student unique identifier"),
        "name": fields.String(required=True, description="The student name"),
        "surname": fields.String(required=True, description="The student surname"),
        "specialization": fields.String(
            required=True, description="The student specialization"
        ),
    },
)


def student_parser(required=False):
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=required)
    parser.add_argument("surname", type=str, required=required)
    parser.add_argument("specialization", type=str, required=required)
    return parser


@student_ns.route("/")
class StudentsList(Resource):
    @student_ns.doc("list_students")
    @student_ns.marshal_list_with(student_model)
    def get(self):
        query_params = student_parser(required=False).parse_args()
        return StudentService.get_all_students(**query_params)

    @student_ns.doc("create_student")
    @student_ns.expect(student_model)
    @student_ns.marshal_with(student_model, code=201)
    def post(self):
        student = student_parser(required=True).parse_args()
        return StudentService.create_student(student), 201


@student_ns.route("/<string:id>")
@student_ns.response(404, "Student not found")
@student_ns.param("id", "The student identifier")
class StudentItem(Resource):
    @student_ns.doc("get_student")
    @student_ns.marshal_with(student_model)
    def get(self, id):
        return StudentService.get_student_by_id(id)

    @student_ns.doc("update_student")
    @student_ns.expect(student_model)
    @student_ns.marshal_with(student_model)
    def put(self, id):
        student = student_parser(required=True).parse_args()
        return StudentService.update_student(id, student)

    @student_ns.doc("delete_student")
    @student_ns.response(204, "Student deleted")
    def delete(self, id):
        StudentService.delete_student(id)
        return "", 200
