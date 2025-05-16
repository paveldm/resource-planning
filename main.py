import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QDate
from database.db_manager import DatabaseManager
from gui.main_window import Ui_MainWindow
from datetime import datetime
import pandas as pd
import plotly.express as px
from PySide6.QtWidgets import QListWidgetItem
from PySide6.QtCore import Qt
from datetime import timedelta
from PySide6.QtGui import QIcon

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, db_manager):
        super().__init__()
        self.setupUi(self)
        self.db_manager = db_manager
        self.setWindowTitle("Ресурсное планирование при ПНР")
        self.setWindowIcon(QIcon("logo.png"))

        self.stackedWidget.setCurrentIndex(0)
        self.pushButtonEmployee.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButtonTasks.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButtonGantt.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.pushButtonActualDates.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.pushButtonAnalysis.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.pushButtonGantt.clicked.connect(self.build_gantt_chart)
        self.pushButtonGantt.clicked.connect(self.build_gantt_chart_tasks)
        self.pushButtonAdd.clicked.connect(self.add_employee)
        self.chooseDirection_2.currentTextChanged.connect(self.update_employee_list)
        self.load_employees()
        self.load_tasks()
        self.load_tasks_to_list()
        self.listWidgetTasks.itemClicked.connect(self.on_task_selected)
        self.pushButtonDeleteEmployee.clicked.connect(self.delete_employee)
        self.pushButtonDeleteTask.clicked.connect(self.delete_task)
        self.load_employees_to_delete()
        self.load_tasks_to_delete()
        self.load_tasks_to_table()
        self.setup_read_only_table()
        self.pushButtonAddDateProject.clicked.connect(self.save_project_start_date)
        self.load_project_start_date()
        self.pushButtonAddTask.clicked.connect(self.add_task_to_db)
        self.pushButtonSaveActualDuration.clicked.connect(self.save_actual_duration)
        self.update_analysis_tab()
        self.stackedWidgetDiagrams.setCurrentIndex(0)
        self.pushButtonDiagram1.clicked.connect(self.switch_to_previous_diagram)
        self.pushButtonDiagram2.clicked.connect(self.switch_to_next_diagram)
        self.pushButtonBarChart1.clicked.connect(lambda: self.switch_bar_chart_page(0))
        self.pushButtonBarChart2.clicked.connect(lambda: self.switch_bar_chart_page(1))
        self.stackedWidgetPieCharts.setCurrentIndex(0)
        self.pushButtonPieChart1.clicked.connect(lambda: self.switch_pie_chart_page(0))
        self.pushButtonPieChart2.clicked.connect(lambda: self.switch_pie_chart_page(1))

    def switch_to_previous_diagram(self):
        current_index = self.stackedWidgetDiagrams.currentIndex()
        total_pages = self.stackedWidgetDiagrams.count()
        new_index = (current_index - 1) % total_pages
        self.stackedWidgetDiagrams.setCurrentIndex(new_index)

    def switch_to_next_diagram(self):
        current_index = self.stackedWidgetDiagrams.currentIndex()
        total_pages = self.stackedWidgetDiagrams.count()
        new_index = (current_index + 1) % total_pages
        self.stackedWidgetDiagrams.setCurrentIndex(new_index)

    def switch_bar_chart_page(self, index):
        self.stackedWidgetBarCharts.setCurrentIndex(index)

    def switch_pie_chart_page(self, index):
        self.stackedWidgetPieCharts.setCurrentIndex(index)

    def load_employees_to_delete(self):
        employees = self.db_manager.get_all_employees()
        self.deleteEmployee.clear()
        for employee in employees:
            employee_id, name, direction = employee
            self.deleteEmployee.addItem(f"{name} ({direction})", userData=employee_id)

    def load_tasks_to_delete(self):
        try:
            tasks = self.db_manager.get_tasks_for_deletion()
            self.deleteTask.clear()
            for task in tasks:
                (
                    task_id,
                    name,
                    planned_start,
                    planned_end,
                    assigned_employee_id,
                    actual_start,
                    actual_end,
                ) = task
                self.deleteTask.addItem(f"{name}", userData=task_id)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить задачи: {e}")

    def delete_employee(self):
        employee_id = self.deleteEmployee.currentData()
        self.db_manager.delete_employee(employee_id)
        self.load_employees_to_delete()
        self.load_employees()
        self.update_analysis_tab()


    def delete_task(self):
        task_id = self.deleteTask.currentData()
        try:
            self.db_manager.delete_task(task_id)
            self.load_tasks_to_delete()
            self.load_tasks()
            self.load_tasks_to_table()
            self.update_analysis_tab()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось удалить задачу: {e}")

    def load_tasks(self):
        try:
            tasks = self.db_manager.get_all_tasks()
            self.tableWidgetTasks.setRowCount(0)
            for row_number, task in enumerate(tasks):
                (
                    id,
                    name,
                    description,
                    direction,
                    duration,
                    dependencies,
                    planned_start,
                    planned_end,
                    actual_start,
                    actual_end,
                    actual_duration,
                    assigned_employee_id,
                ) = task
                self.tableWidgetTasks.insertRow(row_number)
                self.tableWidgetTasks.setItem(row_number, 0, QTableWidgetItem(str(id)))
                self.tableWidgetTasks.setItem(row_number, 1, QTableWidgetItem(name))
                self.tableWidgetTasks.setItem(row_number, 2, QTableWidgetItem(direction))
                self.tableWidgetTasks.setItem(row_number, 3, QTableWidgetItem(planned_start))
                self.tableWidgetTasks.setItem(row_number, 4, QTableWidgetItem(planned_end))
                self.tableWidgetTasks.setItem(row_number, 5, QTableWidgetItem(str(duration)))
                self.tableWidgetTasks.setItem(row_number, 6, QTableWidgetItem(dependencies))

            centered_columns = [0, 2, 3, 4, 5, 6]
            for row in range(self.tableWidgetTasks.rowCount()):
                for col in centered_columns:
                    item = self.tableWidgetTasks.item(row, col)
                    if item:
                        item.setTextAlignment(Qt.AlignCenter)
            self.tableWidgetTasks.setColumnWidth(0, 30)
            self.tableWidgetTasks.setColumnWidth(1, 350)
            self.tableWidgetTasks.setColumnWidth(2, 100)
            self.tableWidgetTasks.setColumnWidth(3, 100)
            self.tableWidgetTasks.setColumnWidth(4, 110)
            self.tableWidgetTasks.setColumnWidth(5, 110)
            self.tableWidgetTasks.setColumnWidth(6, 30)

            self.load_tasks_to_delete()
            self.load_tasks_to_list()

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить задачи: {e}")

    def load_employees(self):
        employees = self.db_manager.get_all_employees()
        self.tableWidget.setRowCount(0)
        for row_number, employee in enumerate(employees):
            self.tableWidget.insertRow(row_number)
            self.tableWidget.setItem(row_number, 0, QTableWidgetItem(employee[1]))
            self.tableWidget.setItem(row_number, 1, QTableWidgetItem(employee[2]))
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 50)
        centered_columns = [0, 1]
        for row in range(self.tableWidget.rowCount()):
            for col in centered_columns:
                item = self.tableWidget.item(row, col)
                item.setTextAlignment(Qt.AlignCenter)

    def update_employee_list(self):
        direction = self.chooseDirection_2.currentText()
        if not direction:
            return
        employees = self.db_manager.get_employees_by_direction(direction)
        self.chooseEmployee.clear()
        for employee in employees:
            self.chooseEmployee.addItem(employee[1], userData=employee[0])

    def add_employee(self):
        name = self.addEmployee.text().strip()
        direction = self.chooseDirection.currentText()

        if not name:
            QMessageBox.warning(self, "Ошибка", "Введите имя сотрудника!")
            return
        if not direction or direction == "":
            QMessageBox.warning(self, "Ошибка", "Выберите специализацию!")
            return
        try:
            self.db_manager.add_employee(name, direction)
            self.addEmployee.clear()
            self.load_employees()
            self.load_employees_to_delete()
            self.update_analysis_tab()

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось добавить сотрудника: {e}")

    def load_tasks_to_list(self):
        tasks = self.db_manager.get_tasks_for_list()
        self.listWidgetTasks.clear()
        for task in tasks:
            task_id, name = task
            item = QListWidgetItem(f"{task_id}: {name}")
            self.listWidgetTasks.addItem(item)

    def on_task_selected(self, current_item):
        try:
            if not current_item:
                QMessageBox.warning(self, "Ошибка", "Выберите задачу!")
                return

            item_text = current_item.text()
            task_id = int(item_text.split(":")[0])
            task = self.db_manager.get_task_by_id(task_id)
            if not task:
                QMessageBox.warning(self, "Ошибка", "Задача не найдена!")
                return

            self.actualDurationInput.setValue(1)

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные задачи: {e}")

    def load_tasks_to_table(self):
        try:
            self.tableWidgetActualDates.clearContents()
            self.tableWidgetActualDates.setRowCount(0)

            tasks = self.db_manager.get_all_tasks()

            self.tableWidgetActualDates.setRowCount(len(tasks))

            for row, task in enumerate(tasks):
                (
                    task_id,
                    name,
                    description,
                    direction,
                    duration,
                    dependencies,
                    planned_start,
                    planned_end,
                    actual_start,
                    actual_end,
                    actual_duration,
                    assigned_employee_id,
                ) = task

                self.tableWidgetActualDates.setItem(row, 0, QTableWidgetItem(str(task_id)))
                self.tableWidgetActualDates.setItem(row, 1, QTableWidgetItem(name))
                self.tableWidgetActualDates.setItem(row, 2, QTableWidgetItem(direction))
                self.tableWidgetActualDates.setItem(row, 3, QTableWidgetItem(planned_start or ""))
                self.tableWidgetActualDates.setItem(row, 4, QTableWidgetItem(planned_end or ""))
                self.tableWidgetActualDates.setItem(row, 5, QTableWidgetItem(actual_start or ""))
                self.tableWidgetActualDates.setItem(row, 6, QTableWidgetItem(actual_end or ""))
                self.tableWidgetActualDates.setItem(row, 7, QTableWidgetItem(str(duration) or ""))
                self.tableWidgetActualDates.setItem(row, 8, QTableWidgetItem(str(actual_duration) or ""))
                self.tableWidgetActualDates.setItem(row, 9, QTableWidgetItem(dependencies))

            centered_columns = [0, 2, 3, 4, 5, 6, 7, 8, 9]
            for row in range(self.tableWidgetActualDates.rowCount()):
                for col in centered_columns:
                    item = self.tableWidgetActualDates.item(row, col)
                    if item:
                        item.setTextAlignment(Qt.AlignCenter)
            self.tableWidgetActualDates.setColumnWidth(0, 20)
            self.tableWidgetActualDates.setColumnWidth(1, 105)
            self.tableWidgetActualDates.setColumnWidth(2, 100)
            self.tableWidgetActualDates.setColumnWidth(3, 80)
            self.tableWidgetActualDates.setColumnWidth(4, 100)
            self.tableWidgetActualDates.setColumnWidth(5, 80)
            self.tableWidgetActualDates.setColumnWidth(6, 100)
            self.tableWidgetActualDates.setColumnWidth(7, 85)
            self.tableWidgetActualDates.setColumnWidth(8, 85)
            self.tableWidgetActualDates.setColumnWidth(9, 35)

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить задачи: {e}")

    def setup_read_only_table(self):
        for row in range(self.tableWidgetActualDates.rowCount()):
            for col in range(self.tableWidgetActualDates.columnCount()):
                item = self.tableWidgetActualDates.item(row, col)
                if item:
                    item.setFlags(Qt.ItemIsEnabled)

    def load_project_start_date(self):
        start_date = self.db_manager.get_project_start_date()
        if start_date:
            date_object = datetime.strptime(start_date, "%Y-%m-%d")
            formatted_date = date_object.strftime("%d-%m-%Y")
            self.labelStartDate.setText(formatted_date)
        else:
            self.labelStartDate.setText("Не задана")

    def save_project_start_date(self):
        selected_date = self.dateStartProject.date()
        start_date = selected_date.toString("yyyy-MM-dd")
        self.db_manager.save_project_start_date(start_date)
        self.labelStartDate.setText(start_date)

    def build_gantt_chart(self):
        try:
            query = """
                SELECT 
                    tvd.task_id,
                    t.name,
                    tvd.planned_start,
                    tvd.planned_end,
                    tvd.actual_start,
                    tvd.actual_end,
                    t.assigned_employee_id
                FROM 
                    task_visualization_dates tvd
                JOIN 
                    tasks t ON tvd.task_id = t.id
            """
            tasks = self.db_manager.execute_query(query)

            chart_data = []
            for task in tasks:
                task_id = task[0]
                name = task[1]
                planned_start = task[2]
                planned_end = task[3]
                actual_start = task[4]
                actual_end = task[5]
                assigned_employee_id = task[6]

                planned_start_dt = datetime.strptime(planned_start, "%Y-%m-%d")
                planned_end_dt = datetime.strptime(planned_end, "%Y-%m-%d")

                employee_name = self.db_manager.get_employee_name(assigned_employee_id)

                chart_data.append((
                    employee_name,
                    planned_start_dt,
                    planned_end_dt,
                    name,
                    "Planned"
                ))
                if actual_start and actual_end:
                    actual_start_dt = datetime.strptime(actual_start, "%Y-%m-%d")
                    actual_end_dt = datetime.strptime(actual_end, "%Y-%m-%d")

                    if actual_end_dt > planned_end_dt:
                        task_type = "ActualLate"
                    else:
                        task_type = "Actual"

                    chart_data.append((
                        employee_name,
                        actual_start_dt,
                        actual_end_dt,
                        name,
                        task_type
                    ))

            df = pd.DataFrame(chart_data, columns=["Employee", "Start", "Finish", "Task", "Type"])

            min_start_dates = df.groupby("Employee")["Start"].min().reset_index()
            min_start_dates.columns = ["Employee", "MinStart"]

            sorted_employees = min_start_dates.sort_values(by="MinStart", ascending=False)["Employee"].tolist()

            fig = px.timeline(
                df,
                x_start="Start",
                x_end="Finish",
                y="Employee",
                color="Type",
                title="График загрузки сотрудников",
                labels={
                    "Employee": "Сотрудник",
                    "Start": "Дата начала",
                    "Finish": "Дата завершения",
                    "Task": "Задача",
                    "Type": "Тип",
                },
                hover_data=["Task"],
                category_orders={"Type": ["Planned", "Actual", "ActualLate"]},
                color_discrete_map={
                    "Planned": "#ADD8E6",
                    "Actual": "rgba(50, 205, 50, 0.5)",
                    "ActualLate": "rgba(255, 69, 0, 0.5)"
                }
            )

            fig.for_each_trace(lambda trace: trace.update(name={
                "Planned": "Плановая длительность",
                "Actual": "Фактическая (согласно плану или с опережением)",
                "ActualLate": "Фактическая (отклонение от плана)"
            }[trace.name]))

            fig.update_layout(
                title_font_size=20,
                font=dict(size=12),
                plot_bgcolor="#F9F9F9",
                paper_bgcolor="#FFFFFF",
                margin=dict(l=150, r=20, t=80, b=20),
                showlegend=True,
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1
                ),
                dragmode="pan",
                xaxis=dict(
                    rangeselector=None,
                    rangeslider=dict(visible=False),
                    type="date",
                    fixedrange=False
                )
            )

            fig.update_yaxes(
                categoryorder="array",
                categoryarray=sorted_employees,
                tickfont=dict(size=12),
                title_font_size=14
            )
            fig.update_xaxes(
                tickformat="%Y-%m-%d",
                tickfont=dict(size=12),
                title_font_size=14
            )

            fig.update_traces(marker_line_width=0)
            fig.update_layout(bargap=0)

            html_content = fig.to_html(
                include_plotlyjs="cdn",
                config={"scrollZoom": True}
            )
            self.webEngineViewDiagramEmployee.setHtml(html_content)

        except Exception as e:
            print("")

    def build_gantt_chart_tasks(self):
        query = """
               SELECT 
                   tvd.task_id,
                   t.name,
                   tvd.planned_start,
                   tvd.planned_end,
                   tvd.actual_start,
                   tvd.actual_end
               FROM 
                   task_visualization_dates tvd
               JOIN 
                   tasks t ON tvd.task_id = t.id
           """
        tasks = self.db_manager.execute_query(query)

        chart_data = []
        for task in tasks:
            task_id = task[0]
            name = task[1]
            planned_start = task[2]
            planned_end = task[3]
            actual_start = task[4]
            actual_end = task[5]

            planned_start_dt = datetime.strptime(planned_start, "%Y-%m-%d")
            planned_end_dt = datetime.strptime(planned_end, "%Y-%m-%d")

            name = task[1][:20] + "..." if len(task[1]) > 20 else task[1]
            chart_data.append((
                name,
                planned_start_dt,
                planned_end_dt,
                "Planned"
            ))

            if actual_start and actual_end:
                actual_start_dt = datetime.strptime(actual_start, "%Y-%m-%d")
                actual_end_dt = datetime.strptime(actual_end, "%Y-%m-%d")

                if actual_end_dt > planned_end_dt:
                    task_type = "ActualLate"
                else:
                    task_type = "Actual"

                chart_data.append((
                    name,
                    actual_start_dt,
                    actual_end_dt,
                    task_type
                ))

        df = pd.DataFrame(chart_data, columns=["Task", "Start", "Finish", "Type"])
        df = df.sort_values(by="Start", ascending=False)

        fig = px.timeline(
            df,
            x_start="Start",
            x_end="Finish",
            y="Task",
            color="Type",
            title="График выполнения работ",
            labels={
                "Task": "Задача",
                "Start": "Дата начала",
                "Finish": "Дата завершения",
                "Type": "Тип",
            },
            hover_data=["Task"],
            category_orders={"Type": ["Planned", "Actual", "ActualLate"]},
            color_discrete_map={
                "Planned": "#ADD8E6",
                "Actual": "rgba(50, 205, 50, 0.5)",
                "ActualLate": "rgba(255, 69, 0, 0.5)"
            }
        )

        fig.for_each_trace(lambda trace: trace.update(name={
            "Planned": "Плановая длительность",
            "Actual": "Фактическая (согласно плану или с опережением)",
            "ActualLate": "Фактическая (отклонение от плана)"
        }[trace.name]))

        fig.update_layout(
            title_font_size=20,
            font=dict(size=12),
            plot_bgcolor="#F9F9F9",
            paper_bgcolor="#FFFFFF",
            margin=dict(l=50, r=20, t=80, b=20),
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            dragmode="pan",
            xaxis=dict(
                rangeselector=None,
                rangeslider=dict(visible=False),
                type="date",
                fixedrange=False
            )
        )

        fig.update_yaxes(
            categoryorder="array",
            tickfont=dict(size=10),
            title_font_size=12,
            automargin=True
        )
        fig.update_xaxes(
            tickformat="%Y-%m-%d",
            tickfont=dict(size=12),
            title_font_size=14
        )

        fig.update_traces(marker_line_width=0)
        fig.update_layout(bargap=0)

        html_content = fig.to_html(include_plotlyjs="cdn", config={"scrollZoom": True})
        self.webEngineViewDiagramTasks.setHtml(html_content)

    def prepare_gantt_data(self):
        tasks = self.db_manager.get_all_tasks()

        critical_data = self.calculate_critical_path()
        critical_path_ids = critical_data.get("critical_path", [])

        chart_data = []
        for task in tasks:
            task_id = task[0]
            name = task[1]
            planned_start = datetime.strptime(task[6], "%Y-%m-%d")
            planned_end = datetime.strptime(task[7], "%Y-%m-%d")

            task_type = "Critical" if task_id in critical_path_ids else "Normal"

            chart_data.append((
                name,
                planned_start,
                planned_end,
                task_type
            ))
        df = pd.DataFrame(chart_data, columns=["Task", "Start", "Finish", "Type"])
        return df

    def build_gantt_with_critical_path(self):
        df = self.prepare_gantt_data()
        df = df.sort_values(by="Start", ascending=False)
        df["Order"] = range(len(df))
        df["Type"] = df["Type"].replace({"Critical": "Критическая", "Normal": "Некритическая"})
        fig = px.timeline(
            df,
            x_start="Start",
            x_end="Finish",
            y="Order",
            color="Type",
            title="Критический путь проекта",
            labels={
                "Order": "Задача",
                "Start": "Дата начала",
                "Finish": "Дата завершения",
                "Type": "Тип задачи",
            },
            hover_data=["Task"],
            color_discrete_map={
                "Некритическая": "#ADD8E6",
                "Критическая": "rgba(255, 0, 0, 0.8)"
            }
        )

        fig.update_layout(
            title_font_size=20,
            font=dict(size=12),
            plot_bgcolor="#F9F9F9",
            paper_bgcolor="#FFFFFF",
            margin=dict(l=150, r=20, t=80, b=20),
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            dragmode="pan",
            xaxis=dict(
                rangeselector=None,
                rangeslider=dict(visible=False),
                type="date",
                fixedrange=False
            ),
            bargap=0
        )

        fig.update_yaxes(
            ticktext=df["Task"],
            tickvals=df["Order"],
            automargin=True,
            tickfont=dict(size=10)
        )
        fig.update_traces(width=1.0)
        fig.update_traces(marker_line_width=0)

        html_content = fig.to_html(include_plotlyjs="cdn")
        self.webEngineViewCriticalPath.setHtml(html_content)

    def add_task_to_db(self):
        try:
            task_name = self.addTask.text().strip()
            description = self.taskDescription.toPlainText().strip()
            direction = self.chooseDirection_2.currentText()
            duration = self.durationInput.value()
            dependencies_str = self.dependenciesInput.text().strip()
            assigned_employee_id = self.chooseEmployee.currentData()

            if not task_name:
                QMessageBox.warning(self, "Ошибка", "Введите название задачи!")
                return
            if not description:
                QMessageBox.warning(self, "Ошибка", "Введите описание задачи!")
                return
            if not direction or direction == "":
                QMessageBox.warning(self, "Ошибка", "Выберите специализацию!")
                return
            if not assigned_employee_id:
                QMessageBox.warning(self, "Ошибка", "Выберите сотрудника!")
                return

            tasks_in_db = self.db_manager.get_all_tasks()
            if tasks_in_db:
                if not dependencies_str.strip():
                    QMessageBox.warning(self, "Ошибка", "Укажите зависимости для задачи!")
                    return
            else:
                dependencies_str = ""

            self.db_manager.add_task_with_calculated_dates(
                task_name,
                description,
                direction,
                duration,
                dependencies_str,
                assigned_employee_id
            )

            self.addTask.clear()
            self.taskDescription.clear()
            self.durationInput.setValue(1)
            self.dependenciesInput.clear()
            self.load_tasks()
            self.load_tasks_to_table()
            self.update_analysis_tab()

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось добавить задачу: {e}")

    def calculate_actual_dates(self, task_id, actual_duration):
        task = self.db_manager.get_task_by_id(task_id)
        if not task:
            raise Exception("Задача не найдена!")

        dependencies_str = task[5]
        project_start_date = self.db_manager.get_project_start_date()

        project_start_dt = datetime.strptime(project_start_date, "%Y-%m-%d")

        if not dependencies_str or dependencies_str.strip() == "":
            actual_start_dt = project_start_dt
        else:
            dependency_ids = [int(dep.strip()) for dep in dependencies_str.split(",") if dep.strip()]

            latest_dependency_end_dt = None
            for dep_id in dependency_ids:
                dep_task = self.db_manager.get_task_by_id(dep_id)
                if dep_task and dep_task[9]:
                    dep_end_dt = datetime.strptime(dep_task[9], "%Y-%m-%d")
                    if latest_dependency_end_dt is None or dep_end_dt > latest_dependency_end_dt:
                        latest_dependency_end_dt = dep_end_dt

            if latest_dependency_end_dt is None:
                raise Exception("Необходимо задать фактические даты для всех зависимых задач!")

            actual_start_dt = latest_dependency_end_dt + timedelta(days=1)

        actual_end_dt = actual_start_dt + timedelta(days=actual_duration - 1)
        self.load_tasks_to_table()

        return actual_start_dt.strftime("%Y-%m-%d"), actual_end_dt.strftime("%Y-%m-%d")

    def save_actual_duration(self):
        try:
            current_item = self.listWidgetTasks.currentItem()
            if not current_item:
                QMessageBox.warning(self, "Ошибка", "Выберите задачу из списка!")
                return

            item_text = current_item.text()
            task_id_str = item_text.split(":")[0].strip()
            task_id = int(task_id_str)

            actual_duration = self.actualDurationInput.value()

            self.db_manager.update_task_actual_duration(task_id, actual_duration)

            actual_start, actual_end = self.calculate_actual_dates(task_id, actual_duration)

            self.db_manager.update_task_actual_dates(task_id, actual_start, actual_end)
            self.db_manager.update_task_visualization_dates(task_id, actual_start, actual_end)

            self.load_tasks()
            self.load_tasks_to_table()
            self.update_analysis_tab()

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить фактическую длительность: {e}")

    def calculate_task_status_statistics(self):
        tasks = self.db_manager.get_all_tasks()
        completed_on_time = 0
        overdue = 0
        not_completed = 0

        for task in tasks:
            planned_end = task[7]
            actual_start = task[8]
            actual_end = task[9]

            if not actual_start or not actual_end:
                not_completed += 1
                continue

            planned_end_dt = datetime.strptime(planned_end, "%Y-%m-%d")
            actual_end_dt = datetime.strptime(actual_end, "%Y-%m-%d")

            if actual_end_dt <= planned_end_dt:
                completed_on_time += 1
            else:
                overdue += 1

        return {
            "completed_on_time": completed_on_time,
            "overdue": overdue,
            "not_completed": not_completed,
        }

    def display_pie_chart(self):
        stats = self.calculate_task_status_statistics()

        labels = ["Завершенные в срок", "Просроченные", "Незавершенные"]
        values = [
            stats["completed_on_time"],
            stats["overdue"],
            stats["not_completed"],
        ]

        fig = px.pie(
            names=labels,
            values=values,
            title="Распределение заданий по статусам",
            color_discrete_sequence=["#4CAF50", "#FF5252", "#FFC107"],
        )

        fig.update_layout(
            title_font_size=15,
            font=dict(size=12),
            plot_bgcolor="#F9F9F9",
            paper_bgcolor="#FFFFFF",
            margin=dict(l=50, r=20, t=80, b=20)
        )

        html_content = fig.to_html(include_plotlyjs="cdn")
        self.webEngineViewPieChart.setHtml(html_content)

    def update_analysis_tab(self):
        try:
            self.update_progress_bar()
            self.display_pie_chart()
            self.display_average_durations()
            self.update_task_quantity_label()
            self.update_employee_quantity_label()
            self.build_bar_chart_quantity_employee()
            self.build_bar_chart_duration()
            self.fill_direction_analysis_table()
            self.build_pie_chart_completed_tasks_by_direction()
            self.build_gantt_with_critical_path()
            self.fill_direction_quality_table()
            self.calculate_and_display_project_deviation()
            critical_data = self.calculate_critical_path()
            self.labelProjectDuration.setText(str(critical_data["project_duration"]) + " дней")
        except Exception as e:
            print("")

    def update_progress_bar(self):
        tasks = self.db_manager.get_all_tasks()

        total_tasks = len(tasks)
        completed_tasks = sum(1 for task in tasks if task[8] and task[9])

        completion_percentage = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0

        self.progressBarCompletion.setValue(int(completion_percentage))

        if completion_percentage >= 80:
            bar_color = "#28A745"
        elif completion_percentage >= 50:
            bar_color = "#FFC107"
        else:
            bar_color = "#DC3545"

        self.progressBarCompletion.setStyleSheet(f"""
                        QProgressBar {{
                            border: 2px solid {bar_color};
                            border-radius: 10px;
                            background-color: #E9ECEF;
                            height: 20px;
                            text-align: center;
                            color: #333333;
                            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
                        }}
                        QProgressBar::chunk {{
                            background-color: {bar_color};
                            border-radius: 8px;
                        }}
                    """)

    def calculate_average_durations(self):
        try:
            tasks = self.db_manager.get_all_tasks()

            total_planned_duration = 0
            total_tasks_with_planned = 0

            for task in tasks:
                planned_start, planned_end = task[6], task[7]
                if planned_start and planned_end:
                    planned_start_dt = datetime.strptime(planned_start, "%Y-%m-%d")
                    planned_end_dt = datetime.strptime(planned_end, "%Y-%m-%d")
                    duration = (planned_end_dt - planned_start_dt).days + 1
                    total_planned_duration += duration
                    total_tasks_with_planned += 1

            avg_planned_duration = (
                total_planned_duration / total_tasks_with_planned if total_tasks_with_planned > 0 else 0
            )
            total_actual_duration = 0
            total_tasks_with_actual = 0

            for task in tasks:
                actual_start, actual_end = task[8], task[9]
                if actual_start and actual_end:
                    actual_start_dt = datetime.strptime(actual_start, "%Y-%m-%d")
                    actual_end_dt = datetime.strptime(actual_end, "%Y-%m-%d")
                    duration = (actual_end_dt - actual_start_dt).days + 1
                    total_actual_duration += duration
                    total_tasks_with_actual += 1

            avg_actual_duration = (
                total_actual_duration / total_tasks_with_actual if total_tasks_with_actual > 0 else 0
            )

            return {
                "avg_planned_duration": avg_planned_duration,
                "avg_actual_duration": avg_actual_duration,
            }

        except Exception as e:
            print(f"Ошибка при расчете средних длительностей: {e}")
            return {"avg_planned_duration": 0, "avg_actual_duration": 0}

    def display_average_durations(self):
        durations = self.calculate_average_durations()
        self.labelAvgPlannedDuration.setText(
            f"Средняя плановая длительность выполнения заданий: {durations['avg_planned_duration']:.1f} дней"
        )
        self.labelAvgActualDuration.setText(
            f"Средняя фактическая длительность выполнения заданий: {durations['avg_actual_duration']:.1f} дней"
        )

    def update_task_quantity_label(self):
        tasks = self.db_manager.get_all_tasks()
        total_tasks = len(tasks)
        self.labelQuantityTasks.setText(f"{total_tasks}")

    def update_employee_quantity_label(self):
        query = "SELECT COUNT(*) FROM employees"
        result = self.db_manager.execute_query(query)
        employee_count = result[0][0]
        self.labelQuantityEmployees.setText(str(employee_count))

    def calculate_critical_path(self):
        try:
            tasks = self.db_manager.get_all_tasks()

            task_map = {}
            for task in tasks:
                task_id = task[0]
                name = task[1]
                duration = task[4]
                dependencies = task[5]

                task_map[task_id] = {
                    "name": name,
                    "duration": duration,
                    "dependencies": [int(dep.strip()) for dep in dependencies.split(",")] if dependencies else [],
                    "es": 0,
                    "ef": 0,
                    "ls": 0,
                    "lf": 0,
                    "slack": 0,
                }

            def calculate_es_ef(task_id):
                task = task_map[task_id]
                if task["es"] != 0 and task["ef"] != 0:
                    return task["ef"]
                if not task["dependencies"]:
                    task["es"] = 0
                    task["ef"] = task["duration"]
                else:
                    max_ef = max(calculate_es_ef(dep) for dep in task["dependencies"])
                    task["es"] = max_ef
                    task["ef"] = task["es"] + task["duration"]
                return task["ef"]

            for task_id in task_map:
                calculate_es_ef(task_id)

            project_duration = max(task["ef"] for task in task_map.values())
            for task_id in reversed(list(task_map.keys())):
                task = task_map[task_id]
                if not any(task_id in task_map[tid]["dependencies"] for tid in task_map):
                    task["lf"] = project_duration
                    task["ls"] = task["lf"] - task["duration"]
                else:
                    min_ls = min(task_map[tid]["ls"] for tid in task_map if task_id in task_map[tid]["dependencies"])
                    task["lf"] = min_ls
                    task["ls"] = task["lf"] - task["duration"]

            for task in task_map.values():
                task["slack"] = task["ls"] - task["es"]

            critical_path = [task_id for task_id, task in task_map.items() if task["slack"] == 0]
            critical_path_names = [task_map[tid]["name"] for tid in critical_path]

            return {
                "critical_path": critical_path,
                "critical_path_names": critical_path_names,
                "project_duration": project_duration,
                "tasks": task_map,
            }

        except Exception as e:
            print("")
            return {}

    def build_bar_chart_quantity_employee(self):
        try:
            query = """
                SELECT direction, COUNT(*) AS count
                FROM employees
                GROUP BY direction
            """
            result = self.db_manager.execute_query(query)

            directions = [row[0] for row in result]
            counts = [row[1] for row in result]

            fig = px.bar(
                x=directions,
                y=counts,
                title="Количество сотрудников по направлениям",
                labels={"x": "Направление", "y": "Количество сотрудников"},
                color=counts,
                color_continuous_scale="Blues",
                range_color=[1, max(counts)],
            )

            fig.update_layout(
                title_font_size=15,
                font=dict(size=10),
                plot_bgcolor="#F9F9F9",
                paper_bgcolor="#FFFFFF",
                margin=dict(l=50, r=20, t=80, b=20),
                showlegend=False
            )

            fig.update_xaxes(
                tickfont=dict(size=10),
                title_font_size=12
            )
            fig.update_yaxes(
                tickfont=dict(size=10),
                title_font_size=12
            )

            html_content = fig.to_html(include_plotlyjs="cdn")
            self.webEngineViewBarChartQuantityEmployee.setHtml(html_content)

        except Exception as e:
            print("")

    def build_bar_chart_duration(self):
        try:
            query = """
                SELECT 
                    direction,
                    planned_start,
                    planned_end,
                    actual_start,
                    actual_end
                FROM 
                    tasks
            """
            result = self.db_manager.execute_query(query)

            duration_by_direction = {}
            for row in result:
                direction = row[0]
                planned_start = row[1]
                planned_end = row[2]
                actual_start = row[3]
                actual_end = row[4]

                if actual_start and actual_end:
                    start_date = datetime.strptime(actual_start, "%Y-%m-%d")
                    end_date = datetime.strptime(actual_end, "%Y-%m-%d")
                    duration = (end_date - start_date).days + 1
                elif planned_start and planned_end:
                    start_date = datetime.strptime(planned_start, "%Y-%m-%d")
                    end_date = datetime.strptime(planned_end, "%Y-%m-%d")
                    duration = (end_date - start_date).days + 1
                else:
                    continue

                if direction not in duration_by_direction:
                    duration_by_direction[direction] = 0
                duration_by_direction[direction] += duration

            directions = list(duration_by_direction.keys())
            durations = list(duration_by_direction.values())

            fig = px.bar(
                x=directions,
                y=durations,
                title="Общая длительность заданий по направлениям",
                labels={"x": "Направление", "y": "Общая длительность (дни)"},
                color=durations,
                color_continuous_scale="Blues",
                range_color=[10, max(durations)]
            )

            fig.update_layout(
                title_font_size=15,
                font=dict(size=10),
                plot_bgcolor="#F9F9F9",
                paper_bgcolor="#FFFFFF",
                margin=dict(l=50, r=20, t=80, b=20),
                showlegend=False
            )

            fig.update_xaxes(
                tickfont=dict(size=10),
                title_font_size=12
            )
            fig.update_yaxes(
                tickfont=dict(size=10),
                title_font_size=12
            )

            html_content = fig.to_html(include_plotlyjs="cdn")
            self.webEngineViewBarChartDuration.setHtml(html_content)

        except Exception as e:
            print("")

    def fill_direction_analysis_table(self):
        try:
            query_directions = "SELECT DISTINCT direction FROM employees"
            directions = self.db_manager.execute_query(query_directions)

            self.tableWidgetDirectionAnalysis.clearContents()
            self.tableWidgetDirectionAnalysis.setRowCount(0)
            for row_number, direction_row in enumerate(directions):
                direction = direction_row[0]

                query_employees = "SELECT COUNT(*) FROM employees WHERE direction = ?"
                employee_count = self.db_manager.execute_query(query_employees, (direction,))[0][0]
                query_tasks = "SELECT COUNT(*) FROM tasks WHERE direction = ?"
                task_count = self.db_manager.execute_query(query_tasks, (direction,))[0][0]

                query_duration = """
                    SELECT SUM(
                        CASE 
                            WHEN actual_duration IS NOT NULL THEN actual_duration
                            ELSE duration
                        END
                    )
                    FROM tasks
                    WHERE direction = ?
                """
                total_duration = self.db_manager.execute_query(query_duration, (direction,))[0][0]
                total_duration = total_duration if total_duration else 0  # Если нет задач, длительность = 0

                self.tableWidgetDirectionAnalysis.insertRow(row_number)
                self.tableWidgetDirectionAnalysis.setItem(row_number, 0, QTableWidgetItem(direction))  # Специализация
                self.tableWidgetDirectionAnalysis.setItem(row_number, 1, QTableWidgetItem(str(employee_count)))  # Количество сотрудников
                self.tableWidgetDirectionAnalysis.setItem(row_number, 2, QTableWidgetItem(str(task_count)))  # Количество заданий
                self.tableWidgetDirectionAnalysis.setItem(row_number, 3, QTableWidgetItem(str(total_duration)))  # Общая длительность
                self.tableWidgetDirectionAnalysis.setColumnWidth(0, 100)
                self.tableWidgetDirectionAnalysis.setColumnWidth(1, 145)
                self.tableWidgetDirectionAnalysis.setColumnWidth(2, 120)
                self.tableWidgetDirectionAnalysis.setColumnWidth(3, 200)
                centered_columns = [0, 1, 2, 3]
                for row in range(self.tableWidgetDirectionAnalysis.rowCount()):
                    for col in centered_columns:
                        item = self.tableWidgetDirectionAnalysis.item(row, col)
                        item.setTextAlignment(Qt.AlignCenter)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось заполнить таблицу анализа направлений: {e}")

    def build_pie_chart_completed_tasks_by_direction(self):
        try:
            query = """
                SELECT 
                    direction, 
                    COUNT(*) AS completed_count
                FROM 
                    tasks
                WHERE 
                    actual_start IS NOT NULL AND actual_end IS NOT NULL
                GROUP BY 
                    direction
            """
            result = self.db_manager.execute_query(query)

            directions = [row[0] for row in result]
            completed_counts = [row[1] for row in result]

            fig = px.pie(
                values=completed_counts,
                names=directions,
                title="Количество выполненных заданий по направлениям",
                color_discrete_sequence=[
                    "#9C27B0",
                    "#FF9800",
                    "#2196F3",
                ]
            )
            fig.update_layout(
                title_font_size=15,
                font=dict(size=12),
                plot_bgcolor="#F9F9F9",
                paper_bgcolor="#FFFFFF",
                margin=dict(l=50, r=20, t=80, b=20)
            )
            html_content = fig.to_html(include_plotlyjs="cdn")
            self.webEngineViewPieChart2.setHtml(html_content)
        except Exception as e:
            print("")

    def fill_direction_quality_table(self):
        try:
            tasks = self.db_manager.get_all_tasks()
            direction_data = {}

            for task in tasks:
                direction = task[3]
                planned_end = task[7]
                actual_end = task[9]

                if not planned_end or not actual_end:
                    continue

                planned_end_dt = datetime.strptime(planned_end, "%Y-%m-%d")
                actual_end_dt = datetime.strptime(actual_end, "%Y-%m-%d")
                deviation = (actual_end_dt - planned_end_dt).days

                if direction not in direction_data:
                    direction_data[direction] = {
                        "total_completed": 0,
                        "overdue_count": 0,
                        "total_deviation": 0,
                    }

                direction_data[direction]["total_completed"] += 1
                if actual_end_dt > planned_end_dt:
                    direction_data[direction]["overdue_count"] += 1
                direction_data[direction]["total_deviation"] += deviation

            self.tableWidgetDirectionQuality.clearContents()
            self.tableWidgetDirectionQuality.setRowCount(0)

            for row_number, (direction, data) in enumerate(direction_data.items()):
                total_completed = data["total_completed"]
                overdue_count = data["overdue_count"]
                total_deviation = data["total_deviation"]

                overdue_percentage = (
                    (overdue_count / total_completed) * 100 if total_completed > 0 else 0
                )
                average_deviation = (
                    total_deviation / total_completed if total_completed > 0 else 0
                )
                self.tableWidgetDirectionQuality.insertRow(row_number)
                self.tableWidgetDirectionQuality.setItem(row_number, 0, QTableWidgetItem(direction))
                self.tableWidgetDirectionQuality.setItem(row_number, 1, QTableWidgetItem(f"{overdue_percentage:.2f}%"))
                self.tableWidgetDirectionQuality.setItem(row_number, 2, QTableWidgetItem(f"{average_deviation:.2f} дней"))

            self.tableWidgetDirectionQuality.setColumnWidth(0, 100)
            self.tableWidgetDirectionQuality.setColumnWidth(1, 175)
            self.tableWidgetDirectionQuality.setColumnWidth(2, 90)
            centered_columns = [0, 1, 2]
            for row in range(self.tableWidgetDirectionQuality.rowCount()):
                for col in centered_columns:
                    item = self.tableWidgetDirectionQuality.item(row, col)
                    if item:
                        item.setTextAlignment(Qt.AlignCenter)

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось заполнить таблицу качества направлений: {e}")

    def calculate_and_display_project_deviation(self):
        try:
            tasks = self.db_manager.get_all_tasks()
            total_deviation = 0
            completed_tasks_count = 0
            for task in tasks:
                planned_duration = task[4]
                actual_duration = task[10]
                if not actual_duration:
                    continue
                deviation = actual_duration - planned_duration
                total_deviation += deviation
                completed_tasks_count += 1
            average_deviation = total_deviation / completed_tasks_count if completed_tasks_count > 0 else 0
            self.labelProjectDeviation.setText(f"{average_deviation:.2f} дней")

        except Exception as e:
            print(f"Ошибка при расчете среднего отклонения: {e}")
            self.labelProjectDeviation.setText("Не удалось рассчитать")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("logo.png"))
    db = DatabaseManager()
    window = MainWindow(db)
    window.show()
    sys.exit(app.exec())