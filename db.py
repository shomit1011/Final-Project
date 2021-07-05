import sqlite3
import random
import os


def get_inventory():

    conn = sqlite3.connect('inventory.db')
    cursor = conn.execute("SELECT * FROM inventory")
    table = cursor.fetchall()
    conn.close()
    print(table)
    return table


def add_item_sql(name, quantity):

    conn = sqlite3.connect('inventory.db')

    cursor = conn.execute("SELECT * FROM inventory")

    sr_no = cursor.fetchall()[-1][0] + 1

    cursor = conn.execute(
        f"INSERT INTO inventory values ({sr_no}, '{name}', {quantity}) ")
    # print(cursor.fetchall())
    conn.commit()
    conn.close()


def write_transcation(values):
    for row in values:
        conn = sqlite3.connect('inventory.db')

        cursor = conn.execute(
            f"UPDATE INVENTORY SET quantity = quantity - {row[1]} WHERE name='{row[0]}'")

        conn.commit()
        conn.close()

    t_id = 0

    while(True):
        t_id = random.randrange(1000, 9999)
        if not os.path.exists(f"transactions/{t_id}"):
            break

    with open(f"transactions/{t_id}", "w") as transaction:
        transaction.write(str(values))
    return t_id
