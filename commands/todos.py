import typer
import db

app = typer.Typer()

con = db.con


@app.command()
def create(name: str):
    con.execute("insert into todos (name, completed) values (?, ?)", (name, False))
    con.commit()


@app.command()
def read():
    cur = con.cursor()
    res = cur.execute("select * from todos")
    rows = res.fetchall()
    for row in rows:
        print(row)


@app.command()
def update_name(id: int, name: str):
    con.execute("update todos set name = ? where id = ?", (name, id))
    con.commit()


@app.command()
def toggle(id: int):
    cur = con.cursor()
    res = cur.execute("select * from todos where id = ?", (id,))
    row = res.fetchone()
    completed = row[2]
    toggled = 0 if completed == 1 else 1
    cur.execute("update todos set completed = ? where id = ?", (toggled, id))
    con.commit()


@app.command()
def delete(id: int):
    con.execute("delete from todos where id = ?", (id,))
    con.commit()
