from flask import Flask, request, abort
import sqlite3


def get_db_connection():
    return sqlite3.connect("./db.sqlite")


def bootstrap_db():
    connection = get_db_connection()
    schema_file = open("./schema.sql")
    connection.executescript(schema_file.read())
    connection.commit()
    connection.close()


def get_operands_key(operands):
    return ",".join(map(str, sorted(operands)))


def normalize_operand_array(array):
    if type(array) == str:
        array = array.split(",")
    return [float(x) for x in array]


bootstrap_db()
app = Flask(__name__)


@app.route("/")
def info():
    return """
        <h1>Sum</h1>
        <form action="/create_sum" method="post">
            <input name="operands" type="text" placeholder="e.g. 1,2,3"/>
            <button type="submit">Create Sum</button>
        </form>
        <form action="/retrieve_sum" method="get">
            <input name="operands" type="text" placeholder="e.g. 1,2,3"/>
            <button type="submit">Retrieve Sum</button>
        </form>
    """


@app.route("/create_sum", methods=["POST"])
def create_sum():
    connection = get_db_connection()

    operands = normalize_operand_array(
        request.form["operands"] or request.json["operands"]
    )
    operands_sum = sum(operands)
    operands_key = get_operands_key(operands)

    connection.execute(
        "REPLACE INTO sum (operands_key,operands_sum) VALUES (?,?)",
        (operands_key, operands_sum),
    )

    connection.commit()
    connection.close()

    return {"sum": operands_sum}


@app.route("/retrieve_sum", methods=["GET"])
def retrieve_sum():
    connection = get_db_connection()

    operands = normalize_operand_array(request.args.get("operands"))
    operands_key = get_operands_key(operands)

    rows = connection.execute(
        "SELECT operands_sum FROM sum WHERE operands_key = ?", (operands_key,)
    ).fetchone()

    connection.commit()
    connection.close()

    if rows == None:
        abort(404, f"No sum has been created {operands_key} for yet.")

    operands_sum = rows[0]

    return {"sum": operands_sum}
