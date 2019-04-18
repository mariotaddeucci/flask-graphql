from flask import Flask
from flask_graphql import GraphQLView
from schema import schema
from schema.sql import db as sql_db
from schema.mongo import db as mongo_db
from os import getenv

app = Flask(__name__)

app.config.from_object('config')

mongo_db.init_app(app)
sql_db.init_app(app)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)


@app.route('/')
def home():
    return "A Simple Graphql endpoint"


if __name__ == "__main__":
    port = int(getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
