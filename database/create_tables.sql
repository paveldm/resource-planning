-- Таблица даты начала проекта
CREATE TABLE IF NOT EXISTS project_settings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    start_date DATE NOT NULL
);

-- Таблица сотрудников
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    direction TEXT CHECK(direction IN ('ЭТО', 'ТМО', 'АСУ ТП'))
);

-- Таблица задач
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    direction TEXT CHECK(direction IN ('ЭТО', 'ТМО', 'АСУ ТП')),
    duration INTEGER NOT NULL,
    dependencies TEXT,
    planned_start DATE,
    planned_end DATE,
    actual_start DATE, -- Фактическая дата начала
    actual_end DATE, -- Фактическая дата завершения
    actual_duration INTEGER,
    assigned_employee_id INTEGER,
    FOREIGN KEY(assigned_employee_id) REFERENCES employees(id)
);

-- Для диаграммы Ганта
CREATE TABLE IF NOT EXISTS task_visualization_dates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id INTEGER NOT NULL, -- ID задачи
    planned_start DATE,       -- Плановая дата начала (такая же, как в tasks)
    planned_end DATE,         -- Плановая дата завершения (увеличенная на 1 день)
    actual_start DATE, -- Фактическая дата начала
    actual_end DATE, -- Фактическая дата завершения
    FOREIGN KEY(task_id) REFERENCES tasks(id)
);