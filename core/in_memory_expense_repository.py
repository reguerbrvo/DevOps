from core.expense import Expense


class InMemoryExpenseRepository:
    def __init__(self):
        self._expenses: list[Expense] = []

    def save(self, expense: Expense) -> None:
        existing = self.get_by_id(expense.id)
        if existing is None:
            self._expenses.append(expense)
            return

        index = self._expenses.index(existing)
        self._expenses[index] = expense

    def remove(self, expense_id: int) -> None:
        self._expenses = [
            expense for expense in self._expenses if expense.id != expense_id
        ]

    def get_by_id(self, expense_id: int) -> Expense | None:
        for expense in self._expenses:
            if expense.id == expense_id:
                return expense
        return None

    def list_all(self) -> list[Expense]:
        return self._expenses.copy()
