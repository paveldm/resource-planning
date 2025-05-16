from PySide6.QtSql import QSqlDatabase, QSqlQuery
from datetime import datetime, timedelta

class DatabaseManager:
    def __init__(self, db_name='pnr_planner.db'):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(db_name)
        if not self.db.open():
            print("Ошибка подключения к БД")
            return
        self.create_tables()

    def create_tables(self):
        query = QSqlQuery()
        with open('database/create_tables.sql', 'r', encoding='utf-8') as f:
            sql_script = f.read()
            for statement in sql_script.split(';'):
                if statement.strip():
                    if not query.exec_(statement):
                        print(f"Ошибка при выполнении запроса: {query.lastError().text()}")

    def add_employee(self, name, direction):
        query = QSqlQuery()
        query.prepare("""
        INSERT INTO employees (name, direction) 
        VALUES (?, ?)
        """)
        query.addBindValue(name)
        query.addBindValue(direction)
        query.exec()

    def delete_employee(self, employee_id):
        query = QSqlQuery()
        query.prepare("DELETE FROM tasks WHERE assigned_employee_id = ?")
        query.addBindValue(employee_id)
        if not query.exec():
            raise Exception(f"Ошибка при удалении задач сотрудника: {query.lastError().text()}")
        query.prepare("DELETE FROM employees WHERE id = ?")
        query.addBindValue(employee_id)
        if not query.exec():
            raise Exception(f"Ошибка при удалении сотрудника: {query.lastError().text()}")

    def delete_task(self, task_id):
        try:
            self.db.transaction()
            query = QSqlQuery()
            query.prepare("DELETE FROM tasks WHERE id = ?")
            query.addBindValue(task_id)
            if not query.exec():
                raise Exception(f"Ошибка при удалении задачи из таблицы tasks: {query.lastError().text()}")

            query.prepare("DELETE FROM task_visualization_dates WHERE task_id = ?")
            query.addBindValue(task_id)
            if not query.exec():
                raise Exception(
                    f"Ошибка при удалении задачи из таблицы task_visualization_dates: {query.lastError().text()}")

            self.db.commit()

        except Exception as e:
            self.db.rollback()
            print(f"Ошибка при удалении задачи: {e}")
            raise e

    def get_all_employees(self):
        query = QSqlQuery("SELECT id, name, direction FROM employees")
        employees = []
        while query.next():
            employees.append((query.value(0), query.value(1), query.value(2)))
        return employees

    def get_all_tasks(self):
        query = """
            SELECT 
                id, name, description, direction, duration, dependencies,
                planned_start, planned_end, actual_start, actual_end, actual_duration, assigned_employee_id
            FROM tasks
            ORDER BY planned_start ASC
        """
        return self.execute_query(query)

    def execute_query(self, query, params=None):
        result = []
        sql_query = QSqlQuery(self.db)
        try:
            if params:
                sql_query.prepare(query)
                for param in params:
                    sql_query.addBindValue(param)
                if not sql_query.exec():
                    print(f"Ошибка при выполнении параметризованного запроса: {sql_query.lastError().text()}")
                    return result
            else:
                if not sql_query.exec(query):
                    print(f"Ошибка при выполнении запроса: {sql_query.lastError().text()}")
                    return result

            if query.strip().upper().startswith("SELECT"):
                while sql_query.next():
                    row = [sql_query.value(i) for i in range(sql_query.record().count())]
                    result.append(tuple(row))

        except Exception as e:
            print(f"Ошибка при выполнении запроса: {e}")
            return result
        return result

    def get_tasks_for_list(self):
        query = "SELECT id, name FROM tasks ORDER BY planned_start ASC"
        return self.execute_query(query)

    def get_task_by_id(self, task_id):
        query = QSqlQuery()
        query.prepare("""
            SELECT 
                id, name, description, direction, duration, dependencies,
                planned_start, planned_end, actual_start, actual_end, assigned_employee_id
            FROM tasks
            WHERE id = ?
        """)
        query.addBindValue(task_id)
        if not query.exec_():
            raise Exception(f"Ошибка при загрузке задачи: {query.lastError().text()}")

        if query.next():
            return tuple(query.value(i) for i in range(11))
        return None

    def update_task_actual_dates(self, task_id, actual_start, actual_end):
        query = QSqlQuery()
        query.prepare("""
            UPDATE tasks
            SET actual_start = ?, actual_end = ?
            WHERE id = ?
        """)
        query.addBindValue(actual_start)
        query.addBindValue(actual_end)
        query.addBindValue(task_id)
        if not query.exec():
            raise Exception(f"Ошибка при обновлении фактических дат: {query.lastError().text()}")

    def get_employees_by_direction(self, direction):
        query = QSqlQuery()
        query.prepare("SELECT id, name FROM employees WHERE direction = ?")
        query.addBindValue(direction)
        if not query.exec():
            raise Exception(f"Ошибка при получении сотрудников: {query.lastError().text()}")
        employees = []
        while query.next():
            employees.append((query.value(0), query.value(1)))  # (id, name)
        return employees

    def get_employee_name(self, employee_id):
        query = QSqlQuery()
        query.prepare("SELECT name FROM employees WHERE id = ?")
        query.addBindValue(employee_id)
        if not query.exec():
            raise Exception(f"Ошибка при получении имени сотрудника: {query.lastError().text()}")
        if query.next():
            return query.value(0)
        return "Не назначен"

    def save_project_start_date(self, start_date):
        query = QSqlQuery()
        query.prepare("SELECT COUNT(*) FROM project_settings")
        if not query.exec():
            raise Exception(f"Ошибка при проверке даты начала проекта: {query.lastError().text()}")
        query.next()
        record_count = query.value(0)
        if record_count == 0:
            query.prepare("INSERT INTO project_settings (start_date) VALUES (?)")
        else:
            query.prepare("UPDATE project_settings SET start_date = ? WHERE id = 1")
        query.addBindValue(start_date)
        if not query.exec():
            raise Exception(f"Ошибка при сохранении даты начала проекта: {query.lastError().text()}")

    def get_project_start_date(self):
        query = QSqlQuery("SELECT start_date FROM project_settings WHERE id = 1")
        if query.exec() and query.next():
            return query.value(0)
        return None

    def add_task_with_calculated_dates(self, name, description, direction, duration, dependencies_str, assigned_employee_id):
        project_start_date = self.get_project_start_date()
        if not project_start_date:
            raise Exception("Дата начала проекта не задана!")

        project_start_dt = datetime.strptime(project_start_date, "%Y-%m-%d")
        tasks = self.get_all_tasks()
        task_map = {task[0]: {"planned_end": task[7]} for task in tasks}
        planned_start_dt = project_start_dt

        if dependencies_str:
            dependency_ids = [int(dep.strip()) for dep in dependencies_str.split(",") if dep.strip()]
            for dep_id in dependency_ids:
                if dep_id not in task_map:
                    raise Exception(f"Задача с ID {dep_id} не найдена!")

            latest_dependency_end = project_start_dt
            for dep_id in dependency_ids:
                dep_end = datetime.strptime(task_map[dep_id]["planned_end"], "%Y-%m-%d")
                if dep_end > latest_dependency_end:
                    latest_dependency_end = dep_end

            planned_start_dt = latest_dependency_end + timedelta(days=1)

        planned_end_dt = planned_start_dt + timedelta(days=duration - 1)
        planned_end_dt_for_gantt = planned_start_dt + timedelta(days=duration)
        planned_start = planned_start_dt.strftime("%Y-%m-%d")
        planned_end = planned_end_dt.strftime("%Y-%m-%d")
        planned_end_for_gantt = planned_end_dt_for_gantt.strftime("%Y-%m-%d")

        query = QSqlQuery()
        query.prepare("""
            INSERT INTO tasks (
                name, description, direction, duration, dependencies, planned_start, planned_end, assigned_employee_id
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """)
        query.addBindValue(name)
        query.addBindValue(description)
        query.addBindValue(direction)
        query.addBindValue(duration)
        query.addBindValue(dependencies_str or "")
        query.addBindValue(planned_start)
        query.addBindValue(planned_end)
        query.addBindValue(assigned_employee_id)

        if not query.exec():
            raise Exception(f"Ошибка при добавлении задачи: {query.lastError().text()}")

        task_id = query.lastInsertId()
        query.prepare("""
            INSERT INTO task_visualization_dates (
                task_id, planned_start, planned_end, actual_start, actual_end
            ) VALUES (?, ?, ?, ?, ?)
        """)
        query.addBindValue(task_id)
        query.addBindValue(planned_start)
        query.addBindValue(planned_end_for_gantt)
        query.addBindValue(None)
        query.addBindValue(None)

        if not query.exec():
            raise Exception(f"Ошибка при добавлении дат задачи: {query.lastError().text()}")

    def calculate_planned_dates(self, duration, dependencies, project_start_date):
        tasks = self.get_all_tasks()
        task_map = {task[0]: {"planned_end": task[4]} for task in tasks}
        latest_dependency_end = project_start_date

        if dependencies:
            for dep_id in dependencies.split(","):
                dep_id = int(dep_id.strip())
                if dep_id in task_map:
                    dep_end = datetime.strptime(task_map[dep_id]["planned_end"], "%Y-%m-%d")
                    if dep_end > latest_dependency_end:
                        latest_dependency_end = dep_end
        planned_start = latest_dependency_end
        planned_end = planned_start + timedelta(days=duration - 1)
        return planned_start, planned_end

    def get_tasks_for_deletion(self):
        query = """
            SELECT 
                id, name, planned_start, planned_end, assigned_employee_id, actual_start, actual_end
            FROM tasks
            ORDER BY planned_start ASC
        """
        return self.execute_query(query)

    def update_task_actual_duration(self, task_id, actual_duration):
        query = QSqlQuery()
        query.prepare("""
            UPDATE tasks
            SET actual_duration = ?
            WHERE id = ?
        """)
        query.addBindValue(actual_duration)
        query.addBindValue(task_id)

        if not query.exec():
            raise Exception(f"Ошибка при обновлении фактической длительности: {query.lastError().text()}")

    def update_task_visualization_dates(self, task_id, actual_start, actual_end):
        query = QSqlQuery()

        actual_end_dt = datetime.strptime(actual_end, "%Y-%m-%d")
        actual_end_dt += timedelta(days=1)
        actual_end_adjusted = actual_end_dt.strftime("%Y-%m-%d")
        query.prepare("""
            SELECT id FROM task_visualization_dates WHERE task_id = ?
        """)
        query.addBindValue(task_id)

        if not query.exec():
            raise Exception(f"Ошибка при проверке существования записи: {query.lastError().text()}")

        if query.next():
            query.prepare("""
                UPDATE task_visualization_dates
                SET actual_start = ?, actual_end = ?
                WHERE task_id = ?
            """)
            query.addBindValue(actual_start)
            query.addBindValue(actual_end_adjusted)
            query.addBindValue(task_id)
        else:
            query.prepare("""
                INSERT INTO task_visualization_dates (task_id, planned_start, planned_end, actual_start, actual_end)
                SELECT id, planned_start, planned_end, ?, ?
                FROM tasks
                WHERE id = ?
            """)
            query.addBindValue(actual_start)
            query.addBindValue(actual_end_adjusted)
            query.addBindValue(task_id)
        if not query.exec():
            raise Exception(f"Ошибка при обновлении/добавлении записи: {query.lastError().text()}")
