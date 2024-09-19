import logging
from datetime import datetime

from tgbot.misc.datetime_now import _get_now_datetime
import sqlite3


class DataBase:
    def __init__(self, path_to_db="finance_bot.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def cursor(self):
        return self.connection.cursor()

    def execute(
        self,
        sql: str,
        parameters: tuple = None,
        fetchone=False,
        fetchall=False,
        commit=False,
    ):
        if not parameters:
            parameters = tuple()
        try:
            with self.connection as connection:
                cursor = connection.cursor()
                cursor.execute(sql, parameters)
                data = None
                if commit:
                    connection.commit()
                if fetchone:
                    data = cursor.fetchone()
                elif fetchall:
                    data = cursor.fetchall()
            return data
        except sqlite3.Error as error:
            logging.error(f"Database error: {error}")

    def create_table_users(self):
        sql = """
                CREATE TABLE Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telegram_id INTEGER,
                name varchar(255) ,
                username varchar(255),
                phone integer,
                email varchar(255),
                date datetime
    );
            """
        return self.execute(sql=sql, commit=True)

    def add_user(
        self,
        telegram_id: int,
        name: str,
        phone: int = None,
        email: str = None,
        username: str = None,
        date: datetime = None,
    ):
        sql = "INSERT INTO Users(telegram_id, name, phone, email, username, date) VALUES (?,?,?,?,?,?)"
        parameters = (telegram_id, name, phone, email, username, date)
        return self.execute(sql, parameters=parameters, commit=True)

    def _init_db(self):
        """Инициализирует БД"""
        with open("infrastructure/database/create_db.sql", "r") as f:
            sql = f.read()
        self.cursor().executescript(sql)
        self.connection.commit()

    def check_db(self):
        if self.execute(
            "SELECT name FROM sqlite_master " "WHERE type='table' AND name='expense'",
            fetchall=True,
        ):
            return
        self._init_db()

    def select_all_categories(self):
        sql = """
                SELECT * FROM category
                """
        return self.execute(sql, fetchall=True)

    def add_user(self, user_id: int):
        sql = f"""
        INSERT INTO user(telegram_id) values ({user_id})     
        """
        return self.execute(sql, commit=True)

    def check_user(self, user_id: int):
        sql = f"""
       SELECT telegram_id FROM user WHERE telegram_id = {user_id}
        """
        return self.execute(sql, fetchone=True)

    def add_expense(
        self, owner: str, amount: int, created, category_codename: str, raw_text: str
    ):
        sql = """
        INSERT INTO expense(owner, amount, created, category_codename, raw_text ) VALUES (?, ?, ?, ?, ? )
        """
        parameters = (owner, amount, created, category_codename, raw_text)
        self.execute(sql, parameters=parameters, commit=True)

    def add_profit(self, owner: int, amount: int, created, row_text: str):
        sql = """
        INSERT INTO profit(owner,amount, created,row_text) VALUES (?,?,?,?)
        """
        parameters = (owner, amount, created, row_text)
        self.execute(sql, parameters=parameters, commit=True)

    def delete(self, table: str, row_id: int) -> None:
        row_id = int(row_id)
        sql = f"DELETE FROM {table} WHERE id={row_id}"
        return self.execute(sql, commit=True)

    def last_expenses(self, user_id: str):
        sql = f"""
        SELECT expense_id,owner, amount, category_codename FROM expense WHERE owner = {user_id} ORDER BY created DESC LIMIT 10
        """
        return self.execute(sql, fetchall=True)

    def get_month_statistic(self, user_id: str):
        now = _get_now_datetime()
        first_day_of_month = f"{now.year}-{now.month:02}-01"
        print(first_day_of_month)
        sql = f"""
        SELECT sum(amount) FROM expense where owner = {user_id} and date(created) >= date({first_day_of_month});
        """
        f""""""

        result = self.execute(sql, fetchone=True)
        if not result[0]:
            return "В цьому місяці не має витрат"
        all_month_expenses = result[0]
        return f"Витрати в цьому місяці - {all_month_expenses} грн"

    def get_today_statistic(self, user_id: str):
        sql = f"""
        SELECT SUM(amount) FROM expense WHERE owner = {user_id} and date(created)=date('now', 'localtime')
        """
        result = self.execute(sql, fetchone=True)
        if not result[0]:
            return "Сьогодні ще не має витрат"
        all_today_expenses = result[0]
        return f"Сьогодні ви витратили - {all_today_expenses} грн"

    def export_to_csv(self, user_id):
        import pandas as pd

        sql = f"""
        SELECT amount, created, category_codename, raw_text FROM expense WHERE owner = {user_id} 
        """
        df = pd.read_sql(sql, self.connection)
        path = f"csv_expenses/{user_id}_expenses.csv"
        df.to_csv(path, index=False)
        return path
