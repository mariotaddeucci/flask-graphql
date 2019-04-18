import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from graphene_mongo import MongoengineObjectType, MongoengineConnectionField
from .mongo.Model1 import Post, User
from .sql.Model1 import Department, Employee, Task


# Schema Objects
class PostObject(MongoengineObjectType):
    class Meta:
        model = Post
        interfaces = (graphene.relay.Node,)


class UserObject(MongoengineObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node,)


class DepartmentObject(SQLAlchemyObjectType):
    class Meta:
        model = Department
        interfaces = (graphene.relay.Node,)


class EmployeeObject(SQLAlchemyObjectType):
    class Meta:
        model = Employee
        interfaces = (graphene.relay.Node,)


class TaskObject(SQLAlchemyObjectType):
    class Meta:
        model = Task
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    posts = MongoengineConnectionField(PostObject)
    users = MongoengineConnectionField(UserObject)
    departments = SQLAlchemyConnectionField(DepartmentObject)
    employees = SQLAlchemyConnectionField(EmployeeObject)
    tasks = SQLAlchemyConnectionField(TaskObject)


schema = graphene.Schema(query=Query)
