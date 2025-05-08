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

        # Установка названия окна
        self.setWindowTitle("Ресурсное планирование при ПНР")
        # Установка логотипа (иконки) приложения
        self.setWindowIcon(QIcon("logo.png"))

        # Настраиваем вкладки
        self.stackedWidget.setCurrentIndex(0)  # Устанавливаем первую вкладку как активную
        self.pushButtonEmployee.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButtonTasks.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))  # Задачи
        self.pushButtonGantt.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))  # Диаграмма Ганта
        self.pushButtonGantt.clicked.connect(self.build_gantt_chart)  # Переход на вкладку "Диаграмма Ганта"
        self.pushButtonGantt.clicked.connect(self.build_gantt_chart_tasks)  # Переход на вкладку "Диаграмма Ганта"
        self.pushButtonActualDates.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.pushButtonAnalysis.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))

        # Подключение сигналов для первой вкладки ("Главная")
        self.pushButtonAdd.clicked.connect(self.add_employee)
        self.chooseDirection_2.currentTextChanged.connect(self.update_employee_list)

        # Загрузка данных при старте
        self.load_employees()
        self.load_tasks()

        # Загружаем задачи в список
        self.load_tasks_to_list()
        self.listWidgetTasks.itemClicked.connect(self.on_task_selected)

        # Подключение сигналов к слотам
        self.pushButtonDeleteEmployee.clicked.connect(self.delete_employee)
        self.pushButtonDeleteTask.clicked.connect(self.delete_task)

        # Загрузка данных в QComboBox
        self.load_employees_to_delete()
        self.load_tasks_to_delete()

        # Загрузка данных
        self.load_tasks_to_table()
        self.setup_read_only_table()

        # Подключение сигнала кнопки к слоту
        self.pushButtonAddDateProject.clicked.connect(self.save_project_start_date)

        # Загрузка текущей даты начала проекта (если она есть)
        self.load_project_start_date()

        # Кнопка добавления задачи
        self.pushButtonAddTask.clicked.connect(self.add_task_to_db)

        # Кнопка сохранения фактической длительности
        self.pushButtonSaveActualDuration.clicked.connect(self.save_actual_duration)

        self.update_analysis_tab()

        # Подключаем кнопки к переключению страниц
        self.stackedWidgetDiagrams.setCurrentIndex(0)
        self.pushButtonDiagram1.clicked.connect(self.switch_to_previous_diagram)
        self.pushButtonDiagram2.clicked.connect(self.switch_to_next_diagram)


        # Подключаем кнопки к переключению страниц в stackedWidgetBarCharts
        self.pushButtonBarChart1.clicked.connect(lambda: self.switch_bar_chart_page(0))  # Первая страница
        self.pushButtonBarChart2.clicked.connect(lambda: self.switch_bar_chart_page(1))  # Вторая страница

        # Подключаем кнопки к переключению страниц в stackedWidgetPieCharts
        self.stackedWidgetPieCharts.setCurrentIndex(0)
        self.pushButtonPieChart1.clicked.connect(lambda: self.switch_pie_chart_page(0))  # Первая страница
        self.pushButtonPieChart2.clicked.connect(lambda: self.switch_pie_chart_page(1))  # Вторая страница

    def switch_to_previous_diagram(self):
        """
        Переключает stackedWidgetDiagrams на предыдущую страницу.
        Если текущая страница — первая, переходит на последнюю.
        """
        current_index = self.stackedWidgetDiagrams.currentIndex()
        total_pages = self.stackedWidgetDiagrams.count()
        new_index = (current_index - 1) % total_pages  # Циклический переход
        self.stackedWidgetDiagrams.setCurrentIndex(new_index)

    def switch_to_next_diagram(self):
        """
        Переключает stackedWidgetDiagrams на следующую страницу.
        Если текущая страница — последняя, переходит на первую.
        """
        current_index = self.stackedWidgetDiagrams.currentIndex()
        total_pages = self.stackedWidgetDiagrams.count()
        new_index = (current_index + 1) % total_pages  # Циклический переход
        self.stackedWidgetDiagrams.setCurrentIndex(new_index)

    def switch_bar_chart_page(self, index):
        """
        Переключает страницу в stackedWidgetBarCharts.
        :param index: Индекс страницы (0 или 1).
        """
        self.stackedWidgetBarCharts.setCurrentIndex(index)

    def switch_pie_chart_page(self, index):
        """
        Переключает страницу в stackedWidgetPieCharts.
        :param index: Индекс страницы (0 или 1).
        """
        self.stackedWidgetPieCharts.setCurrentIndex(index)

    def load_employees_to_delete(self):
        """Загружает список сотрудников в QComboBox для удаления."""
        try:
            employees = self.db_manager.get_all_employees()  # Получаем всех сотрудников из базы данных
            self.deleteEmployee.clear()
            for employee in employees:
                employee_id, name, direction = employee
                self.deleteEmployee.addItem(f"{name} ({direction})", userData=employee_id)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить сотрудников: {e}")

    def load_tasks_to_delete(self):
        """Загружает список задач в QComboBox для удаления."""
        try:
            tasks = self.db_manager.get_tasks_for_deletion()  # Используем новый метод
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
        """Удаляет выбранного сотрудника."""
        selected_index = self.deleteEmployee.currentIndex()
        if selected_index == -1:
            QMessageBox.warning(self, "Ошибка", "Выберите сотрудника для удаления!")
            return

        employee_id = self.deleteEmployee.currentData()  # Получаем ID выбранного сотрудника
        try:
            self.db_manager.delete_employee(employee_id)  # Удаляем сотрудника из базы данных
            QMessageBox.information(self, "Успех", "Сотрудник успешно удален!")
            self.load_employees_to_delete()  # Обновляем выпадающий список
            self.load_employees()  # Обновляем таблицу сотрудников
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось удалить сотрудника: {e}")

    def delete_task(self):
        """Удаляет выбранную задачу."""
        selected_index = self.deleteTask.currentIndex()
        if selected_index == -1:
            QMessageBox.warning(self, "Ошибка", "Выберите задачу для удаления!")
            return

        task_id = self.deleteTask.currentData()  # Получаем ID выбранной задачи
        try:
            self.db_manager.delete_task(task_id)  # Удаляем задачу из базы данных
            QMessageBox.information(self, "Успех", "Задача успешно удалена!")
            self.load_tasks_to_delete()  # Обновляем выпадающий список
            self.load_tasks()  # Обновляем таблицу задач
            self.load_tasks_to_table()
            self.update_analysis_tab()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось удалить задачу: {e}")

    def load_tasks(self):
        try:
            # Получаем задачи из базы данных
            tasks = self.db_manager.get_all_tasks()

            # Очищаем таблицу
            self.tableWidgetTasks.setRowCount(0)

            # Заполняем таблицу данными
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

                # Вставляем новую строку в таблицу
                self.tableWidgetTasks.insertRow(row_number)

                # Заполняем столбцы данными
                self.tableWidgetTasks.setItem(row_number, 0, QTableWidgetItem(str(id)))  # ID задачи
                self.tableWidgetTasks.setItem(row_number, 1, QTableWidgetItem(name))  # Название задачи
                self.tableWidgetTasks.setItem(row_number, 2, QTableWidgetItem(direction))  # Направление
                self.tableWidgetTasks.setItem(row_number, 3, QTableWidgetItem(planned_start))  # Плановая дата начала
                self.tableWidgetTasks.setItem(row_number, 4, QTableWidgetItem(planned_end))  # Плановая дата завершения
                self.tableWidgetTasks.setItem(row_number, 5, QTableWidgetItem(str(duration)))  # Длительность
                self.tableWidgetTasks.setItem(row_number, 6, QTableWidgetItem(dependencies))  # Длительность

            centered_columns = [0, 2, 3, 4, 5, 6]
            for row in range(self.tableWidgetTasks.rowCount()):
                for col in centered_columns:
                    item = self.tableWidgetTasks.item(row, col)
                    if item:  # Если ячейка не пустая
                        item.setTextAlignment(Qt.AlignCenter)

            self.tableWidgetTasks.setColumnWidth(0, 30)
            self.tableWidgetTasks.setColumnWidth(1, 350)
            self.tableWidgetTasks.setColumnWidth(2, 100)
            self.tableWidgetTasks.setColumnWidth(3, 100)
            self.tableWidgetTasks.setColumnWidth(4, 110)
            self.tableWidgetTasks.setColumnWidth(5, 110)
            self.tableWidgetTasks.setColumnWidth(6, 30)

            self.load_tasks_to_delete()
            self.load_tasks_to_list() # Обновляем таблицу задач для фактической длительности

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить задачи: {e}")

    def load_employees(self):
        """Загружает сотрудников в таблицу."""
        try:
            employees = self.db_manager.get_all_employees()
            self.tableWidget.setRowCount(0)
            for row_number, employee in enumerate(employees):
                self.tableWidget.insertRow(row_number)
                self.tableWidget.setItem(row_number, 0, QTableWidgetItem(employee[1]))  # Имя
                self.tableWidget.setItem(row_number, 1, QTableWidgetItem(employee[2]))  # Специализация
            self.tableWidget.setColumnWidth(0, 250)
            self.tableWidget.setColumnWidth(1, 50)
            centered_columns = [0, 1]
            for row in range(self.tableWidget.rowCount()):
                for col in centered_columns:
                    item = self.tableWidget.item(row, col)
                    item.setTextAlignment(Qt.AlignCenter)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить сотрудников: {e}")

    def update_employee_list(self):
        direction = self.chooseDirection_2.currentText()
        if not direction:
            return

        try:
            employees = self.db_manager.get_employees_by_direction(direction)
            self.chooseEmployee.clear()
            for employee in employees:
                self.chooseEmployee.addItem(employee[1], userData=employee[0])
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить сотрудников: {e}")

    def add_employee(self):
        """Добавляет нового сотрудника."""
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
            QMessageBox.information(self, "Успех", "Сотрудник успешно добавлен!")

            # Очищаем поля ввода
            self.addEmployee.clear()

            # Обновляем таблицу сотрудников
            self.load_employees()

            # Обновляем выпадающий список для удаления сотрудников
            self.load_employees_to_delete()

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось добавить сотрудника: {e}")

    def load_tasks_to_list(self):
        """Загружает задачи в список."""
        try:
            tasks = self.db_manager.get_tasks_for_list()
            self.listWidgetTasks.clear()

            if not tasks:
                print("В базе данных нет задач.")
                return

            for task in tasks:
                task_id, name = task  # Распаковываем ID и название задачи
                item = QListWidgetItem(f"{task_id}: {name}")  # Создаем элемент с форматом "ID: Название"
                self.listWidgetTasks.addItem(item)

        except Exception as e:
            print(f"Ошибка при загрузке задач: {e}")

    def on_task_selected(self, current_item):
        """Обработчик выбора задачи из списка."""
        try:
            # Проверяем, выбран ли элемент
            if not current_item:
                QMessageBox.warning(self, "Ошибка", "Выберите задачу!")
                return

            # Извлекаем ID задачи из текста элемента списка
            item_text = current_item.text()
            if ":" not in item_text:
                QMessageBox.critical(self, "Ошибка", "Некорректный формат элемента списка.")
                return

            task_id = int(item_text.split(":")[0])

            # Получаем данные о задаче
            task = self.db_manager.get_task_by_id(task_id)
            if not task:
                QMessageBox.warning(self, "Ошибка", "Задача не найдена!")
                return

            # Распаковываем только те поля, которые возвращает get_task_by_id (их 11)
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
                assigned_employee_id
            ) = task

            # Теперь можно обновлять интерфейс
            self.actualDurationInput.setValue(1)  # По умолчанию 1 день
            # Здесь можно позже загрузить реальное значение actual_duration, если оно есть

        except ValueError:
            QMessageBox.critical(self, "Ошибка", "Некорректный ID задачи.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные задачи: {e}")

    def load_tasks_to_table(self):
        """
        Загружает задачи в таблицу tableWidgetActualDates.
        """
        try:
            # Очищаем таблицу
            self.tableWidgetActualDates.clearContents()
            self.tableWidgetActualDates.setRowCount(0)

            # Получаем задачи из базы данных
            tasks = self.db_manager.get_all_tasks()

            # Устанавливаем количество строк в таблице
            self.tableWidgetActualDates.setRowCount(len(tasks))

            # Заполняем таблицу данными
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

                # Заполняем столбцы данными
                self.tableWidgetActualDates.setItem(row, 0, QTableWidgetItem(str(task_id)))  # Название задачи
                self.tableWidgetActualDates.setItem(row, 1, QTableWidgetItem(name))  # Название задачи
                self.tableWidgetActualDates.setItem(row, 2, QTableWidgetItem(direction))  # Название задачи
                self.tableWidgetActualDates.setItem(row, 3, QTableWidgetItem(planned_start or ""))  # Плановая дата начала
                self.tableWidgetActualDates.setItem(row, 4, QTableWidgetItem(planned_end or ""))  # Плановая дата завершения
                self.tableWidgetActualDates.setItem(row, 5, QTableWidgetItem(actual_start or ""))  # Фактическая дата начала
                self.tableWidgetActualDates.setItem(row, 6, QTableWidgetItem(actual_end or ""))  # Фактическая дата завершения
                self.tableWidgetActualDates.setItem(row, 7, QTableWidgetItem(str(duration) or ""))  # Плановая длительность
                self.tableWidgetActualDates.setItem(row, 8, QTableWidgetItem(str(actual_duration) or ""))  # Фактическая длительность
                self.tableWidgetActualDates.setItem(row, 9, QTableWidgetItem(dependencies))  # Название задачи

            centered_columns = [0, 2, 3, 4, 5, 6, 7, 8, 9]
            for row in range(self.tableWidgetActualDates.rowCount()):
                for col in centered_columns:
                    item = self.tableWidgetActualDates.item(row, col)
                    if item:  # Если ячейка не пустая
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
        """Делает таблицу только для чтения."""
        for row in range(self.tableWidgetActualDates.rowCount()):
            for col in range(self.tableWidgetActualDates.columnCount()):
                item = self.tableWidgetActualDates.item(row, col)
                if item:
                    item.setFlags(Qt.ItemIsEnabled)  # Только чтение

    def load_project_start_date(self):
        """Загружает дату начала проекта из базы данных и отображает её в QDateEdit."""
        start_date = self.db_manager.get_project_start_date()
        if start_date:
            qdate = QDate.fromString(start_date, "yyyy-MM-dd")
            self.dateStartProject.setDate(qdate)

    def save_project_start_date(self):
        """Сохраняет дату начала проекта в базу данных."""
        try:
            # Получаем дату из QDateEdit
            selected_date = self.dateStartProject.date()
            start_date = selected_date.toString("yyyy-MM-dd")

            # Сохраняем дату в базу данных
            self.db_manager.save_project_start_date(start_date)

            # Уведомляем пользователя об успешном сохранении
            QMessageBox.information(self, "Успех", "Дата начала проекта успешно сохранена!")

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить дату начала проекта: {e}")

    def build_gantt_chart(self):
        """
        Построение диаграммы Ганта с использованием данных из таблиц task_visualization_dates и tasks.
        """
        try:
            # Получаем все задачи из базы данных
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

            # Проверяем, есть ли задачи
            if not tasks:
                QMessageBox.warning(self, "Внимание", "В базе данных нет задач!")
                return

            chart_data = []
            for task in tasks:
                # Распаковываем данные задачи
                task_id = task[0]
                name = task[1]
                planned_start = task[2]
                planned_end = task[3]
                actual_start = task[4]
                actual_end = task[5]
                assigned_employee_id = task[6]

                # Пропускаем задачи без плановых дат
                if not planned_start or not planned_end:
                    print(f"Пропущена задача '{name}' из-за отсутствия плановых дат.")
                    continue

                # Преобразуем строки в объекты datetime
                planned_start_dt = datetime.strptime(planned_start, "%Y-%m-%d")
                planned_end_dt = datetime.strptime(planned_end, "%Y-%m-%d")

                # Получаем имя сотрудника
                employee_name = self.db_manager.get_employee_name(assigned_employee_id)

                # Добавляем данные для плановых дат
                chart_data.append((
                    employee_name,  # Сотрудник
                    planned_start_dt,
                    planned_end_dt,
                    name,  # Название задачи
                    "Planned"
                ))

                # Если есть фактические даты, добавляем их
                if actual_start and actual_end:
                    actual_start_dt = datetime.strptime(actual_start, "%Y-%m-%d")
                    actual_end_dt = datetime.strptime(actual_end, "%Y-%m-%d")

                    # Проверяем, является ли задача просроченной
                    if actual_end_dt > planned_end_dt:  # Учитываем корректировку на 1 день
                        task_type = "ActualLate"  # Новый тип для просроченных задач
                    else:
                        task_type = "Actual"

                    chart_data.append((
                        employee_name,  # Сотрудник
                        actual_start_dt,
                        actual_end_dt,
                        name,  # Название задачи
                        task_type
                    ))

            # Создаем DataFrame
            df = pd.DataFrame(chart_data, columns=["Employee", "Start", "Finish", "Task", "Type"])

            # Находим минимальную дату начала для каждого сотрудника
            min_start_dates = df.groupby("Employee")["Start"].min().reset_index()
            min_start_dates.columns = ["Employee", "MinStart"]

            # Сортируем сотрудников по минимальной дате начала (в обратном порядке: от поздней к ранней)
            sorted_employees = min_start_dates.sort_values(by="MinStart", ascending=False)["Employee"].tolist()

            # Строим диаграмму Ганта
            fig = px.timeline(
                df,
                x_start="Start",
                x_end="Finish",
                y="Employee",  # Ось Y теперь содержит сотрудников
                color="Type",  # Разделяем плановые и фактические даты по цвету
                title="График загрузки сотрудников",
                labels={
                    "Employee": "Сотрудник",
                    "Start": "Дата начала",
                    "Finish": "Дата завершения",
                    "Task": "Задача",
                    "Type": "Тип",  # Общий заголовок для легенды
                },
                hover_data=["Task"],  # Добавляем название задачи в подсказки
                category_orders={"Type": ["Planned", "Actual", "ActualLate"]},  # Порядок отображения типов
                color_discrete_map={
                    "Planned": "#ADD8E6",  # Светло-голубой для плановых дат (непрозрачный)
                    "Actual": "rgba(50, 205, 50, 0.5)",  # Полупрозрачный зеленый для фактических дат
                    "ActualLate": "rgba(255, 69, 0, 0.5)"  # Полупрозрачный красный для просроченных задач
                }
            )

            # Переопределяем названия типов для легенды
            fig.for_each_trace(lambda trace: trace.update(name={
                "Planned": "Плановая длительность",
                "Actual": "Фактическая (согласно плану или с опережением)",
                "ActualLate": "Фактическая (отклонение от плана)"
            }[trace.name]))

            # Настройка внешнего вида
            fig.update_layout(
                title_font_size=20,  # Размер шрифта заголовка
                font=dict(size=12),  # Размер шрифта текста
                plot_bgcolor="#F9F9F9",  # Цвет фона графика
                paper_bgcolor="#FFFFFF",  # Цвет фона всей диаграммы
                margin=dict(l=150, r=20, t=80, b=20),  # Отступы
                showlegend=True,  # Отображение легенды
                legend=dict(
                    orientation="h",  # Горизонтальная ориентация легенды
                    yanchor="bottom",
                    y=1.02,  # Положение легенды по вертикали
                    xanchor="right",  # Выравнивание легенды по правому краю
                    x=1  # Положение легенды по горизонтали (1 — правый край)
                ),
                dragmode="pan",  # Режим панорамирования
                xaxis=dict(
                    rangeselector=None,  # Убираем кнопки выбора диапазона
                    rangeslider=dict(visible=False),  # Убираем ползунок для масштабирования
                    type="date",  # Тип оси X — дата
                    fixedrange=False  # Разрешаем масштабирование по оси X
                )
            )

            # Настройка осей
            fig.update_yaxes(
                categoryorder="array",  # Используем пользовательский порядок
                categoryarray=sorted_employees,  # Задаем порядок сотрудников
                tickfont=dict(size=12),  # Размер шрифта меток оси Y
                title_font_size=14  # Размер шрифта заголовка оси Y
            )
            fig.update_xaxes(
                tickformat="%Y-%m-%d",  # Формат дат на оси X
                tickfont=dict(size=12),  # Размер шрифта меток оси X
                title_font_size=14  # Размер шрифта заголовка оси X
            )

            # Уменьшаем высоту полос
            fig.update_traces(marker_line_width=0)  # Убираем границы между полосами
            fig.update_layout(bargap=0)  # Убираем отступы между полосами

            # Отображаем диаграмму в QWebEngineViewEmployee
            html_content = fig.to_html(
                include_plotlyjs="cdn",
                config={"scrollZoom": True}
            )
            self.webEngineViewDiagramEmployee.setHtml(html_content)

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось построить диаграмму Ганта: {e}")

    def build_gantt_chart_tasks(self):
        """
        Построение диаграммы Ганта с названиями задач по оси OY.
        Задачи отсортированы в обратном порядке по дате начала.
        """
        try:
            # Получаем все задачи из базы данных
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

            # Проверяем, есть ли задачи
            if not tasks:
                QMessageBox.warning(self, "Внимание", "В базе данных нет задач!")
                return

            chart_data = []
            for task in tasks:
                # Распаковываем данные задачи
                task_id = task[0]
                name = task[1]
                planned_start = task[2]
                planned_end = task[3]
                actual_start = task[4]
                actual_end = task[5]

                # Пропускаем задачи без плановых дат
                if not planned_start or not planned_end:
                    print(f"Пропущена задача '{name}' из-за отсутствия плановых дат.")
                    continue

                # Преобразуем строки в объекты datetime
                planned_start_dt = datetime.strptime(planned_start, "%Y-%m-%d")
                planned_end_dt = datetime.strptime(planned_end, "%Y-%m-%d")

                # Добавляем данные для плановых дат
                name = task[1][:20] + "..." if len(task[1]) > 20 else task[1]
                chart_data.append((
                    name,  # Название задачи
                    planned_start_dt,
                    planned_end_dt,
                    "Planned"
                ))

                # Если есть фактические даты, добавляем их
                if actual_start and actual_end:
                    actual_start_dt = datetime.strptime(actual_start, "%Y-%m-%d")
                    actual_end_dt = datetime.strptime(actual_end, "%Y-%m-%d")

                    # Проверяем, является ли задача просроченной
                    if actual_end_dt > planned_end_dt:  # Учитываем корректировку на 1 день
                        task_type = "ActualLate"  # Новый тип для просроченных задач
                    else:
                        task_type = "Actual"

                    chart_data.append((
                        name,  # Название задачи
                        actual_start_dt,
                        actual_end_dt,
                        task_type
                    ))

            # Создаем DataFrame
            df = pd.DataFrame(chart_data, columns=["Task", "Start", "Finish", "Type"])

            # Сортируем задачи в обратном порядке по дате начала
            df = df.sort_values(by="Start", ascending=False)

            # Строим диаграмму Ганта
            fig = px.timeline(
                df,
                x_start="Start",
                x_end="Finish",
                y="Task",  # Ось Y теперь содержит названия задач
                color="Type",  # Разделяем плановые и фактические даты по цвету
                title="График выполнения работ",
                labels={
                    "Task": "Задача",
                    "Start": "Дата начала",
                    "Finish": "Дата завершения",
                    "Type": "Тип",  # Общий заголовок для легенды
                },
                hover_data=["Task"],  # Добавляем название задачи в подсказки
                category_orders={"Type": ["Planned", "Actual", "ActualLate"]},  # Порядок отображения типов
                color_discrete_map={
                    "Planned": "#ADD8E6",  # Светло-голубой для плановых дат (непрозрачный)
                    "Actual": "rgba(50, 205, 50, 0.5)",  # Полупрозрачный зеленый для фактических дат
                    "ActualLate": "rgba(255, 69, 0, 0.5)"  # Полупрозрачный красный для просроченных задач
                }
            )

            # Переопределяем названия типов для легенды
            fig.for_each_trace(lambda trace: trace.update(name={
                "Planned": "Плановая длительность",
                "Actual": "Фактическая (согласно плану или с опережением)",
                "ActualLate": "Фактическая (отклонение от плана)"
            }[trace.name]))

            # Настройка внешнего вида
            fig.update_layout(
                title_font_size=20,  # Размер шрифта заголовка
                font=dict(size=12),  # Размер шрифта текста
                plot_bgcolor="#F9F9F9",  # Цвет фона графика
                paper_bgcolor="#FFFFFF",  # Цвет фона всей диаграммы
                margin=dict(l=50, r=20, t=80, b=20),  # Уменьшаем левый отступ до 50
                showlegend=True,  # Отображение легенды
                legend=dict(
                    orientation="h",  # Горизонтальная ориентация легенды
                    yanchor="bottom",
                    y=1.02,  # Положение легенды по вертикали
                    xanchor="right",  # Выравнивание легенды по правому краю
                    x=1  # Положение легенды по горизонтали (1 — правый край)
                ),
                dragmode="pan",  # Режим панорамирования
                xaxis=dict(
                    rangeselector=None,  # Убираем кнопки выбора диапазона
                    rangeslider=dict(visible=False),  # Убираем ползунок для масштабирования
                    type="date",  # Тип оси X — дата
                    fixedrange=False  # Разрешаем масштабирование по оси X
                )
            )

            # Настройка осей
            fig.update_yaxes(
                categoryorder="array",  # Используем пользовательский порядок
                tickfont=dict(size=10),  # Уменьшаем размер шрифта меток оси Y
                title_font_size=12,  # Размер шрифта заголовка оси Y
                automargin=True  # Автоматическая настройка отступов
            )
            fig.update_xaxes(
                tickformat="%Y-%m-%d",  # Формат дат на оси X
                tickfont=dict(size=12),  # Размер шрифта меток оси X
                title_font_size=14  # Размер шрифта заголовка оси X
            )

            # Уменьшаем высоту полос
            fig.update_traces(marker_line_width=0)  # Убираем границы между полосами
            fig.update_layout(bargap=0)  # Убираем отступы между полосами

            # Отображаем диаграмму в QWebEngineViewDiagramTasks
            html_content = fig.to_html(include_plotlyjs="cdn", config={"scrollZoom": True})
            self.webEngineViewDiagramTasks.setHtml(html_content)

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось построить диаграмму Ганта: {e}")

    def add_task_to_db(self):
        """
        Добавляет новую задачу в базу данных.
        Первая задача может быть добавлена без зависимостей.
        Для всех последующих задач зависимости обязательны.
        """
        try:
            # Получаем данные из формы
            task_name = self.addTask.text().strip()
            description = self.taskDescription.toPlainText().strip()
            direction = self.chooseDirection_2.currentText()
            duration = self.durationInput.value()
            dependencies_str = self.dependenciesInput.text().strip()
            assigned_employee_id = self.chooseEmployee.currentData()

            # Проверяем корректность данных
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

            # Проверяем, есть ли задачи в базе данных
            tasks_in_db = self.db_manager.get_all_tasks()  # Получаем список всех задач
            if tasks_in_db:
                # Если в базе есть задачи, проверяем наличие зависимостей
                if not dependencies_str.strip():
                    QMessageBox.warning(self, "Ошибка", "Укажите зависимости для задачи!")
                    return
            else:
                # Если это первая задача, зависимости не нужны
                dependencies_str = ""

            # Добавляем задачу в базу данных
            self.db_manager.add_task_with_calculated_dates(
                task_name,
                description,
                direction,
                duration,
                dependencies_str,
                assigned_employee_id
            )

            # Уведомляем пользователя об успешном добавлении
            QMessageBox.information(self, "Успех", "Задача успешно добавлена!")

            # Очищаем поля ввода
            self.addTask.clear()
            self.taskDescription.clear()
            self.durationInput.setValue(1)
            self.dependenciesInput.clear()

            # Обновляем таблицу задач
            self.load_tasks()
            self.load_tasks_to_table()

            # Обновляем аналитические данные
            self.update_analysis_tab()

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось добавить задачу: {e}")

    def calculate_actual_dates(self, task_id, actual_duration):
        """
        Рассчитывает фактические даты для задачи на основе её ID и длительности.
        :param task_id: ID задачи.
        :param actual_duration: Фактическая длительность задачи (в днях).
        :return: Кортеж (actual_start, actual_end).
        """
        # Получаем данные о задаче
        task = self.db_manager.get_task_by_id(task_id)
        if not task:
            raise Exception("Задача не найдена!")

        # Извлекаем необходимые данные
        dependencies_str = task[5]  # Поле dependencies
        project_start_date = self.db_manager.get_project_start_date()

        if not project_start_date:
            raise Exception("Дата начала проекта не задана!")

        # Преобразуем дату начала проекта в объект datetime
        project_start_dt = datetime.strptime(project_start_date, "%Y-%m-%d")

        # Если нет зависимостей
        if not dependencies_str or dependencies_str.strip() == "":
            actual_start_dt = project_start_dt
        else:
            # Разбиваем зависимости на список ID
            dependency_ids = [int(dep.strip()) for dep in dependencies_str.split(",") if dep.strip()]

            # Находим самую позднюю дату завершения среди зависимых задач
            latest_dependency_end_dt = None
            for dep_id in dependency_ids:
                dep_task = self.db_manager.get_task_by_id(dep_id)
                if dep_task and dep_task[9]:  # Проверяем наличие actual_end
                    dep_end_dt = datetime.strptime(dep_task[9], "%Y-%m-%d")
                    if latest_dependency_end_dt is None or dep_end_dt > latest_dependency_end_dt:
                        latest_dependency_end_dt = dep_end_dt

            # Если есть зависимости, но их даты не заданы
            if latest_dependency_end_dt is None:
                raise Exception("Необходимо задать фактические даты для всех зависимых задач!")

            # Фактическая дата начала
            actual_start_dt = latest_dependency_end_dt + timedelta(days=1)

        # Фактическая дата завершения
        actual_end_dt = actual_start_dt + timedelta(days=actual_duration - 1)

        self.load_tasks_to_table()

        # Возвращаем даты в формате строк
        return actual_start_dt.strftime("%Y-%m-%d"), actual_end_dt.strftime("%Y-%m-%d")

    def save_actual_duration(self):
        """Обработчик нажатия кнопки сохранения фактической длительности."""
        try:
            # Проверяем, выбрана ли задача
            current_item = self.listWidgetTasks.currentItem()
            if not current_item:
                QMessageBox.warning(self, "Ошибка", "Выберите задачу из списка!")
                return

            # Извлекаем ID задачи
            item_text = current_item.text()
            if ":" not in item_text:
                QMessageBox.critical(self, "Ошибка", "Неверный формат элемента списка.")
                return

            task_id_str = item_text.split(":")[0].strip()
            if not task_id_str.isdigit():
                QMessageBox.critical(self, "Ошибка", "ID задачи должен быть числом.")
                return

            task_id = int(task_id_str)

            # Получаем фактическую длительность из QSpinBox
            actual_duration = self.actualDurationInput.value()
            if actual_duration <= 0:
                QMessageBox.warning(self, "Ошибка", "Фактическая длительность должна быть больше 0 дней.")
                return

            # Обновляем фактическую длительность в базе данных
            self.db_manager.update_task_actual_duration(task_id, actual_duration)

            # Рассчитываем фактические даты
            actual_start, actual_end = self.calculate_actual_dates(task_id, actual_duration)

            # Сохраняем фактические даты в базу данных
            self.db_manager.update_task_actual_dates(task_id, actual_start, actual_end)

            self.db_manager.update_task_visualization_dates(task_id, actual_start, actual_end)

            # Обновляем таблицу задач
            self.load_tasks()
            self.load_tasks_to_table()

            self.update_analysis_tab()

            # Уведомляем пользователя
            QMessageBox.information(self, "Успех", "Фактическая длительность и даты успешно сохранены!")

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить фактическую длительность: {e}")

    def calculate_task_status_statistics(self):
        """
        Рассчитывает количество задач по статусам.
        :return: Словарь с количеством задач для каждого статуса.
        """
        try:
            # Получаем все задачи из базы данных
            tasks = self.db_manager.get_all_tasks()

            # Инициализируем счетчики
            completed_on_time = 0
            overdue = 0
            not_completed = 0

            for task in tasks:
                planned_end = task[7]  # Индекс для planned_end
                actual_start = task[8]  # Индекс для actual_start
                actual_end = task[9]  # Индекс для actual_end

                # Если фактические даты не заполнены, задача считается незавершенной
                if not actual_start or not actual_end:
                    not_completed += 1
                    continue

                # Преобразуем строки в объекты datetime
                planned_end_dt = datetime.strptime(planned_end, "%Y-%m-%d")
                actual_end_dt = datetime.strptime(actual_end, "%Y-%m-%d")

                # Проверяем статус завершения
                if actual_end_dt <= planned_end_dt:
                    completed_on_time += 1
                else:
                    overdue += 1

            # Возвращаем словарь с результатами
            return {
                "completed_on_time": completed_on_time,
                "overdue": overdue,
                "not_completed": not_completed,
            }

        except Exception as e:
            print(f"Ошибка при расчете статусов задач: {e}")
            return {}

    def display_pie_chart(self):
        """
        Строит круговую диаграмму распределения задач по статусам.
        """
        try:
            # Рассчитываем статистику
            stats = self.calculate_task_status_statistics()

            # Проверяем, что словарь содержит нужные ключи
            if not all(key in stats for key in ["completed_on_time", "overdue", "not_completed"]):
                raise ValueError("Некорректные данные для построения диаграммы!")

            # Данные для диаграммы
            labels = ["Завершенные в срок", "Просроченные", "Незавершенные"]
            values = [
                stats["completed_on_time"],
                stats["overdue"],
                stats["not_completed"],
            ]

            # Создаем круговую диаграмму
            fig = px.pie(
                names=labels,
                values=values,
                title="Распределение задач по статусам",
                color_discrete_sequence=["#4CAF50", "#FF5252", "#FFC107"],  # Зелёный, красный, жёлтый
            )

            # Настройка внешнего вида
            fig.update_layout(
                title_font_size=15,  # Размер шрифта заголовка
                font=dict(size=12),  # Размер шрифта текста
                plot_bgcolor="#F9F9F9",  # Цвет фона графика
                paper_bgcolor="#FFFFFF",  # Цвет фона всей диаграммы
                margin=dict(l=50, r=20, t=80, b=20)  # Отступы
            )

            # Преобразуем диаграмму в HTML
            html_content = fig.to_html(include_plotlyjs="cdn")

            # Отображаем диаграмму в QWebEngineView
            self.webEngineViewPieChart.setHtml(html_content)

        except Exception as e:
            print(f"Ошибка при отображении круговой диаграммы: {e}")

    def update_analysis_tab(self):
        """
        Обновляет вкладку анализа проекта.
        """
        try:
            # Обновляем progress bar
            self.update_progress_bar()

            # Строим круговую диаграмму
            self.display_pie_chart()

            # Отображаем средние длительности
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

            # Рассчитываем критический путь
            critical_data = self.calculate_critical_path()

            # Проверяем, что данные были успешно рассчитаны
            if not critical_data or "critical_path_names" not in critical_data:
                QMessageBox.warning(self, "Ошибка", "Не удалось рассчитать критический путь!")
                return

            self.labelProjectDuration.setText(str(critical_data["project_duration"]) + " дней")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось обновить вкладку анализа: {e}")

    def update_progress_bar(self):
        """
        Обновляет значение progress bar и применяет динамическую стилизацию.
        """
        try:
            # Получаем все задачи из базы данных
            tasks = self.db_manager.get_all_tasks()

            total_tasks = len(tasks)
            completed_tasks = sum(1 for task in tasks if task[8] and task[9])  # actual_start и actual_end заполнены

            # Рассчитываем процент завершения
            completion_percentage = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0

            # Устанавливаем значение progress bar
            self.progressBarCompletion.setValue(int(completion_percentage))

            # Динамическая стилизация
            if completion_percentage >= 80:
                bar_color = "#28A745"  # Зеленый
            elif completion_percentage >= 50:
                bar_color = "#FFC107"  # Желтый
            else:
                bar_color = "#DC3545"  # Красный

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

        except Exception as e:
            print(f"Ошибка при обновлении progress bar: {e}")

    def calculate_average_durations(self):
        """
        Рассчитывает среднюю плановую и фактическую длительность задач.
        - Средняя плановая длительность = сумма всех плановых длительностей / количество заданий.
        - Средняя фактическая длительность = сумма всех фактических длительностей / количество заданий с фактическими длительностями.
        :return: Словарь с средними значениями.
        """
        try:
            tasks = self.db_manager.get_all_tasks()

            # Рассчитываем среднюю плановую длительность
            total_planned_duration = 0
            total_tasks_with_planned = 0

            for task in tasks:
                planned_start, planned_end = task[6], task[7]  # Индексы для planned_start и planned_end
                if planned_start and planned_end:  # Проверяем, что даты не пустые
                    planned_start_dt = datetime.strptime(planned_start, "%Y-%m-%d")
                    planned_end_dt = datetime.strptime(planned_end, "%Y-%m-%d")
                    duration = (planned_end_dt - planned_start_dt).days + 1  # Добавляем 1 день (включительно)
                    total_planned_duration += duration
                    total_tasks_with_planned += 1

            avg_planned_duration = (
                total_planned_duration / total_tasks_with_planned if total_tasks_with_planned > 0 else 0
            )

            # Рассчитываем среднюю фактическую длительность
            total_actual_duration = 0
            total_tasks_with_actual = 0

            for task in tasks:
                actual_start, actual_end = task[8], task[9]  # Индексы для actual_start и actual_end
                if actual_start and actual_end:  # Проверяем, что даты не пустые
                    actual_start_dt = datetime.strptime(actual_start, "%Y-%m-%d")
                    actual_end_dt = datetime.strptime(actual_end, "%Y-%m-%d")
                    duration = (actual_end_dt - actual_start_dt).days + 1  # Добавляем 1 день (включительно)
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
        """
        Отображает средние длительности задач в метках.
        """
        try:
            # Рассчитываем средние длительности
            durations = self.calculate_average_durations()

            # Обновляем метки
            self.labelAvgPlannedDuration.setText(
                f"Средняя плановая длительность выполнения заданий: {durations['avg_planned_duration']:.1f} дней"
            )
            self.labelAvgActualDuration.setText(
                f"Средняя фактическая длительность выполнения заданий: {durations['avg_actual_duration']:.1f} дней"
            )

        except Exception as e:
            print(f"Ошибка при отображении средних длительностей: {e}")

    def update_task_quantity_label(self):
        """
        Обновляет метку с общим количеством задач.
        """
        try:
            # Получаем все задачи из базы данных
            tasks = self.db_manager.get_all_tasks()

            # Рассчитываем общее количество задач
            total_tasks = len(tasks)

            # Обновляем текст метки
            self.labelQuantityTasks.setText(f"{total_tasks}")

        except Exception as e:
            print(f"Ошибка при обновлении метки с количеством задач: {e}")

    def update_employee_quantity_label(self):
        """
        Обновляет labelQuantityEmployees, отображая общее количество сотрудников.
        """
        try:
            # SQL-запрос для подсчета сотрудников
            query = "SELECT COUNT(*) FROM employees"
            result = self.db_manager.execute_query(query)

            # Получаем количество сотрудников (первый элемент первого кортежа)
            employee_count = result[0][0]

            # Обновляем текст в labelQuantityEmployees
            self.labelQuantityEmployees.setText(str(employee_count))

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось обновить количество сотрудников: {e}")

    def calculate_critical_path(self):
        """
        Рассчитывает критический путь проекта и возвращает данные для визуализации.
        :return: Словарь с данными критического пути.
        """
        try:
            # Получаем все задачи из базы данных
            tasks = self.db_manager.get_all_tasks()

            if not tasks:
                print("В базе данных нет задач.")
                return {}

            # Создаем словарь для хранения данных задач
            task_map = {}
            for task in tasks:
                # Распаковываем только те поля, которые нам нужны
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

            # Расчет ранних сроков (ES и EF)
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

            # Расчет поздних сроков (LS и LF)
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

            # Расчет резерва времени
            for task in task_map.values():
                task["slack"] = task["ls"] - task["es"]

            # Определение критического пути
            critical_path = [task_id for task_id, task in task_map.items() if task["slack"] == 0]
            critical_path_names = [task_map[tid]["name"] for tid in critical_path]

            # Возвращаем результат
            return {
                "critical_path": critical_path,
                "critical_path_names": critical_path_names,
                "project_duration": project_duration,
                "tasks": task_map,
            }

        except Exception as e:
            print(f"Ошибка при расчете критического пути: {e}")
            return {}

    def build_bar_chart_quantity_employee(self):
        """
        Строит столбчатую диаграмму с количеством сотрудников по направлениям.
        """
        try:
            # SQL-запрос для подсчета сотрудников по направлениям
            query = """
                SELECT direction, COUNT(*) AS count
                FROM employees
                GROUP BY direction
            """
            result = self.db_manager.execute_query(query)

            # Разделяем данные на категории и значения
            directions = [row[0] for row in result]  # Направления (АСУ ТП, ТМО, ЭТО)
            counts = [row[1] for row in result]  # Количество сотрудников

            # Проверяем, что данные не пустые
            if not directions or not counts:
                QMessageBox.warning(self, "Внимание", "Нет данных о сотрудниках!")
                return

            # Строим столбчатую диаграмму
            fig = px.bar(
                x=directions,
                y=counts,
                title="Количество сотрудников по направлениям",
                labels={"x": "Направление", "y": "Количество сотрудников"},
                color=counts,  # Цвет столбцов зависит от количества
                color_continuous_scale="Blues",  # Градиент цветов
                range_color=[1, max(counts)],  # Фиксируем диапазон цветов от 1 до максимума
            )

            # Настройка внешнего вида
            fig.update_layout(
                title_font_size=15,  # Размер шрифта заголовка
                font=dict(size=10),  # Размер шрифта текста
                plot_bgcolor="#F9F9F9",  # Цвет фона графика
                paper_bgcolor="#FFFFFF",  # Цвет фона всей диаграммы
                margin=dict(l=50, r=20, t=80, b=20),  # Отступы
                showlegend=False  # Убираем легенду
            )

            # Настройка осей
            fig.update_xaxes(
                tickfont=dict(size=10),  # Размер шрифта меток оси X
                title_font_size=12  # Размер шрифта заголовка оси X
            )
            fig.update_yaxes(
                tickfont=dict(size=10),  # Размер шрифта меток оси Y
                title_font_size=12  # Размер шрифта заголовка оси Y
            )

            # Преобразуем диаграмму в HTML
            html_content = fig.to_html(include_plotlyjs="cdn")

            # Отображаем диаграмму в webEngineViewBarChartQuantityEmployee
            self.webEngineViewBarChartQuantityEmployee.setHtml(html_content)

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось построить диаграмму: {e}")

    def build_bar_chart_duration(self):
        """
        Строит столбчатую диаграмму с общей длительностью задач по направлениям.
        Если фактическая длительность отсутствует, используется плановая.
        """
        try:
            # SQL-запрос для получения данных о задачах
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

            # Разделяем данные по направлениям
            duration_by_direction = {}
            for row in result:
                direction = row[0]
                planned_start = row[1]
                planned_end = row[2]
                actual_start = row[3]
                actual_end = row[4]

                # Рассчитываем длительность
                if actual_start and actual_end:  # Если есть фактические даты
                    start_date = datetime.strptime(actual_start, "%Y-%m-%d")
                    end_date = datetime.strptime(actual_end, "%Y-%m-%d")
                    duration = (end_date - start_date).days + 1  # Добавляем 1 день (включительно)
                elif planned_start and planned_end:  # Если только плановые даты
                    start_date = datetime.strptime(planned_start, "%Y-%m-%d")
                    end_date = datetime.strptime(planned_end, "%Y-%m-%d")
                    duration = (end_date - start_date).days + 1
                else:  # Если даты отсутствуют, пропускаем задачу
                    continue

                # Добавляем длительность к соответствующему направлению
                if direction not in duration_by_direction:
                    duration_by_direction[direction] = 0
                duration_by_direction[direction] += duration

            # Проверяем, что данные не пустые
            if not duration_by_direction:
                QMessageBox.warning(self, "Внимание", "Нет данных о задачах!")
                return

            # Преобразуем данные в списки для диаграммы
            directions = list(duration_by_direction.keys())
            durations = list(duration_by_direction.values())

            # Строим столбчатую диаграмму
            fig = px.bar(
                x=directions,
                y=durations,
                title="Общая длительность заданий по направлениям",
                labels={"x": "Направление", "y": "Общая длительность (дни)"},
                color=durations,  # Цвет столбцов зависит от длительности
                color_continuous_scale="Blues",  # Градиент цветов
                range_color=[10, max(durations)]  # Диапазон цветов
            )

            # Настройка внешнего вида
            fig.update_layout(
                title_font_size=15,  # Размер шрифта заголовка
                font=dict(size=10),  # Размер шрифта текста
                plot_bgcolor="#F9F9F9",  # Цвет фона графика
                paper_bgcolor="#FFFFFF",  # Цвет фона всей диаграммы
                margin=dict(l=50, r=20, t=80, b=20),  # Отступы
                showlegend=False  # Убираем легенду
            )

            # Настройка осей
            fig.update_xaxes(
                tickfont=dict(size=10),  # Размер шрифта меток оси X
                title_font_size=12  # Размер шрифта заголовка оси X
            )
            fig.update_yaxes(
                tickfont=dict(size=10),  # Размер шрифта меток оси Y
                title_font_size=12  # Размер шрифта заголовка оси Y
            )

            # Преобразуем диаграмму в HTML
            html_content = fig.to_html(include_plotlyjs="cdn")

            # Отображаем диаграмму в webEngineViewBarChartDuration
            self.webEngineViewBarChartDuration.setHtml(html_content)

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось построить диаграмму: {e}")

    def fill_direction_analysis_table(self):
        """
        Заполняет таблицу tableWidgetDirectionAnalysis данными:
        Специализация, Количество сотрудников, Количество заданий, Общая длительность заданий.
        Общая длительность считается так: если у задачи есть фактическая длительность,
        используется она; иначе используется плановая длительность.
        """
        try:
            # SQL-запрос для получения данных о специализациях
            query_directions = "SELECT DISTINCT direction FROM employees"
            directions = self.db_manager.execute_query(query_directions)

            # Проверяем, что данные не пустые
            if not directions:
                QMessageBox.warning(self, "Внимание", "Нет данных о специализациях!")
                return

            # Очищаем таблицу
            self.tableWidgetDirectionAnalysis.clearContents()
            self.tableWidgetDirectionAnalysis.setRowCount(0)

            # Заполняем таблицу данными
            for row_number, direction_row in enumerate(directions):
                direction = direction_row[0]

                # Получаем количество сотрудников для направления
                query_employees = "SELECT COUNT(*) FROM employees WHERE direction = ?"
                employee_count = self.db_manager.execute_query(query_employees, (direction,))[0][0]

                # Получаем количество задач для направления
                query_tasks = "SELECT COUNT(*) FROM tasks WHERE direction = ?"
                task_count = self.db_manager.execute_query(query_tasks, (direction,))[0][0]

                # Получаем общую длительность задач (с учетом фактической и плановой длительности)
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

                # Вставляем новую строку в таблицу
                self.tableWidgetDirectionAnalysis.insertRow(row_number)

                # Заполняем столбцы данными
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
        """
        Строит круговую диаграмму в webEngineViewPieChart2,
        показывающую количество выполненных заданий по направлениям.
        """
        try:
            # SQL-запрос для получения данных о выполненных задачах по направлениям
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

            # Разделяем данные на категории и значения
            directions = [row[0] for row in result]  # Направления (АСУ ТП, ТМО, ЭТО)
            completed_counts = [row[1] for row in result]  # Количество выполненных задач

            # Проверяем, что данные не пустые
            if not directions or not completed_counts:
                QMessageBox.warning(self, "Внимание", "Нет данных о выполненных задачах!")
                return

            # Строим круговую диаграмму
            fig = px.pie(
                values=completed_counts,
                names=directions,
                title="Количество выполненных задач по направлениям",
                color_discrete_sequence=[
                    "#9C27B0",
                    "#FF9800",  # Оранжевый
                    "#2196F3",  # Синий
                ]  # Градиент цветов
            )

            # Настройка внешнего вида
            fig.update_layout(
                title_font_size=15,  # Размер шрифта заголовка
                font=dict(size=12),  # Размер шрифта текста
                plot_bgcolor="#F9F9F9",  # Цвет фона графика
                paper_bgcolor="#FFFFFF",  # Цвет фона всей диаграммы
                margin=dict(l=50, r=20, t=80, b=20)  # Отступы
            )

            # Преобразуем диаграмму в HTML
            html_content = fig.to_html(include_plotlyjs="cdn")

            # Отображаем диаграмму в webEngineViewPieChart2
            self.webEngineViewPieChart2.setHtml(html_content)

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось построить диаграмму: {e}")

    def prepare_gantt_data(self):
        """
        Подготавливает данные для построения диаграммы Ганта с критическим путем.
        :return: DataFrame с данными для диаграммы.
        """
        # Получаем все задачи из базы данных
        tasks = self.db_manager.get_all_tasks()

        # Рассчитываем критический путь
        critical_data = self.calculate_critical_path()
        critical_path_ids = critical_data.get("critical_path", [])

        chart_data = []
        for task in tasks:
            task_id = task[0]
            name = task[1]
            planned_start = datetime.strptime(task[6], "%Y-%m-%d")
            planned_end = datetime.strptime(task[7], "%Y-%m-%d")

            # Определяем тип задачи
            task_type = "Critical" if task_id in critical_path_ids else "Normal"

            # Добавляем данные для диаграммы
            chart_data.append((
                name,  # Название задачи
                planned_start,
                planned_end,
                task_type  # Тип задачи
            ))

        # Создаем DataFrame
        df = pd.DataFrame(chart_data, columns=["Task", "Start", "Finish", "Type"])
        return df

    def build_gantt_with_critical_path(self):
        """
        Построение диаграммы Ганта с отображением критического пути.
        Все прямоугольники имеют одинаковую высоту, и отступы между ними убраны.
        """
        try:
            # Подготавливаем данные
            df = self.prepare_gantt_data()

            # Сортируем задачи по дате начала (от ранней к поздней)
            df = df.sort_values(by="Start", ascending=False)

            # Создаем новый столбец для порядка отображения задач
            df["Order"] = range(len(df))  # Простой порядковый номер

            # Переименовываем типы задач для легенды
            df["Type"] = df["Type"].replace({"Critical": "Критическая", "Normal": "Некритическая"})

            # Строим диаграмму Ганта
            fig = px.timeline(
                df,
                x_start="Start",
                x_end="Finish",
                y="Order",  # Используем столбец "Order" для оси Y
                color="Type",  # Разделяем типы задач по цвету
                title="Критический путь проекта",
                labels={
                    "Order": "Задача",  # Переименовываем ось Y для удобства
                    "Start": "Дата начала",
                    "Finish": "Дата завершения",
                    "Type": "Тип задачи",  # Общий заголовок для легенды
                },
                hover_data=["Task"],  # Добавляем название задачи в подсказки
                color_discrete_map={
                    "Некритическая": "#ADD8E6",  # Светло-голубой для обычных задач
                    "Критическая": "rgba(255, 0, 0, 0.8)"  # Красный для задач на критическом пути
                }
            )

            # Настройка внешнего вида
            fig.update_layout(
                title_font_size=20,  # Размер шрифта заголовка
                font=dict(size=12),  # Размер шрифта текста
                plot_bgcolor="#F9F9F9",  # Цвет фона графика
                paper_bgcolor="#FFFFFF",  # Цвет фона всей диаграммы
                margin=dict(l=150, r=20, t=80, b=20),  # Отступы
                showlegend=True,  # Отображение легенды
                legend=dict(
                    orientation="h",  # Горизонтальная ориентация легенды
                    yanchor="bottom",
                    y=1.02,  # Положение легенды по вертикали
                    xanchor="right",  # Выравнивание легенды по правому краю
                    x=1  # Положение легенды по горизонтали (1 — правый край)
                ),
                dragmode="pan",  # Режим панорамирования
                xaxis=dict(
                    rangeselector=None,  # Убираем кнопки выбора диапазона
                    rangeslider=dict(visible=False),  # Убираем ползунок для масштабирования
                    type="date",  # Тип оси X — дата
                    fixedrange=False  # Разрешаем масштабирование по оси X
                ),
                bargap=0  # Убираем отступы между полосами
            )

            # Настройка меток на оси Y
            fig.update_yaxes(
                ticktext=df["Task"],  # Отображаем названия задач
                tickvals=df["Order"],  # Используем порядковые номера для позиций
                automargin=True,  # Автоматическая настройка отступов
                tickfont=dict(size=10)  # Размер шрифта меток оси Y
            )

            # Устанавливаем одинаковую высоту для всех полос
            fig.update_traces(width=1.0)  # Одинаковая ширина (высота) для всех задач

            # Убираем границы между полосами
            fig.update_traces(marker_line_width=0)

            # Отображаем диаграмму в webEngineViewCriticalPath
            html_content = fig.to_html(include_plotlyjs="cdn")
            self.webEngineViewCriticalPath.setHtml(html_content)

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось построить диаграмму Ганта: {e}")

    def fill_direction_quality_table(self):
        """
        Заполняет таблицу tableWidgetDirectionQuality данными:
        - Специализация,
        - Процент просроченных задач,
        - Среднее отклонение от плановых сроков.
        """
        try:
            # Получаем все задачи из базы данных
            tasks = self.db_manager.get_all_tasks()

            # Создаем словарь для хранения данных по специализациям
            direction_data = {}

            for task in tasks:
                direction = task[3]  # Индекс для специализации
                planned_end = task[7]  # Индекс для плановой даты завершения
                actual_end = task[9]  # Индекс для фактической даты завершения

                # Пропускаем задачи без фактической даты завершения
                if not planned_end or not actual_end:
                    continue

                # Преобразуем строки в объекты datetime
                planned_end_dt = datetime.strptime(planned_end, "%Y-%m-%d")
                actual_end_dt = datetime.strptime(actual_end, "%Y-%m-%d")

                # Рассчитываем отклонение (в днях)
                deviation = (actual_end_dt - planned_end_dt).days

                # Инициализируем данные для специализации
                if direction not in direction_data:
                    direction_data[direction] = {
                        "total_completed": 0,  # Общее количество завершенных задач
                        "overdue_count": 0,  # Количество просроченных задач
                        "total_deviation": 0,  # Сумма всех отклонений
                    }

                # Обновляем данные для специализации
                direction_data[direction]["total_completed"] += 1
                if actual_end_dt > planned_end_dt:
                    direction_data[direction]["overdue_count"] += 1
                direction_data[direction]["total_deviation"] += deviation

            # Очищаем таблицу
            self.tableWidgetDirectionQuality.clearContents()
            self.tableWidgetDirectionQuality.setRowCount(0)

            # Заполняем таблицу данными
            for row_number, (direction, data) in enumerate(direction_data.items()):
                total_completed = data["total_completed"]
                overdue_count = data["overdue_count"]
                total_deviation = data["total_deviation"]

                # Рассчитываем процент просроченных задач
                overdue_percentage = (
                    (overdue_count / total_completed) * 100 if total_completed > 0 else 0
                )

                # Рассчитываем среднее отклонение
                average_deviation = (
                    total_deviation / total_completed if total_completed > 0 else 0
                )

                # Вставляем новую строку в таблицу
                self.tableWidgetDirectionQuality.insertRow(row_number)

                # Заполняем столбцы данными
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
        """
        Рассчитывает среднее отклонение от плановых сроков по всему проекту
        и обновляет текст в labelProjectDeviation.
        """
        try:
            # Получаем все задачи из базы данных
            tasks = self.db_manager.get_all_tasks()

            total_deviation = 0  # Суммарное отклонение
            completed_tasks_count = 0  # Количество завершенных задач

            for task in tasks:
                planned_end = task[7]  # Индекс для плановой даты завершения
                actual_end = task[9]  # Индекс для фактической даты завершения

                # Пропускаем задачи без фактической даты завершения
                if not planned_end or not actual_end:
                    continue

                try:
                    # Преобразуем строки в объекты datetime
                    planned_end_dt = datetime.strptime(planned_end, "%Y-%m-%d")
                    actual_end_dt = datetime.strptime(actual_end, "%Y-%m-%d")

                    # Рассчитываем отклонение (в днях)
                    deviation = (actual_end_dt - planned_end_dt).days

                    # Обновляем суммарное отклонение и счетчик завершенных задач
                    total_deviation += deviation
                    completed_tasks_count += 1

                except ValueError as e:
                    print(f"Ошибка при обработке дат для задачи {task[1]}: {e}")
                    continue

            # Рассчитываем среднее отклонение
            average_deviation = (
                total_deviation / completed_tasks_count if completed_tasks_count > 0 else 0
            )

            # Обновляем текст в labelProjectDeviation
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