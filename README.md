# Pasos hechos:

* Clonado el repositorio de la práctica y configurado el remoto apuntando a mi propio repositorio en GitHub.

* Instaladas las dependencias del proyecto con uv usando Python 3.12.

* Revisado el estado inicial del proyecto ejecutando el linter (ruff) por primera vez.

* Entendidos los conceptos clave de la práctica: uv, linter, formatter, tests unitarios, de integración y BDD.

* Completada la clase Expense con validaciones de dominio: título vacío lanza EmptyTitleError, cantidad negativa lanza InvalidAmountError y fecha futura lanza InvalidExpenseDateError.

* Completado InMemoryExpenseRepository con los métodos save, remove, get_by_id y list_all.

* Corregido el helper create_expense en test_expense_repository.py para aceptar description y expense_date con valores por defecto.

* Todos los tests unitarios (10/10) de core/tests/unit pasan correctamente.

* Configurado el workflow de GitHub Actions (ci-pipeline.yaml) para ejecutar lint, formato y tests unitarios, de integración y BDD en cada push.
