CREATE TABLE IF NOT EXISTS project_settings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    start_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    direction TEXT CHECK(direction IN ('ЭТО', 'ТМО', 'АСУ ТП'))
);

CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    direction TEXT CHECK(direction IN ('ЭТО', 'ТМО', 'АСУ ТП')),
    duration INTEGER NOT NULL,
    dependencies TEXT,
    planned_start DATE,
    planned_end DATE,
    actual_start DATE,
    actual_end DATE,
    actual_duration INTEGER,
    assigned_employee_id INTEGER,
    FOREIGN KEY(assigned_employee_id) REFERENCES employees(id)
);

CREATE TABLE IF NOT EXISTS task_visualization_dates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id INTEGER NOT NULL,
    planned_start DATE,
    planned_end DATE,
    actual_start DATE,
    actual_end DATE,
    FOREIGN KEY(task_id) REFERENCES tasks(id)
);