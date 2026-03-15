from datetime import date

from core.expense import Expense
from core.in_memory_expense_repository import InMemoryExpenseRepository


def create_expense(
    id=1,
    title="Test",
    amount=10,
    description="",
    expense_date=None,
):
    return Expense(
        id=id,
        title=title,
        amount=amount,
        description=description,
        expense_date=expense_date or date.today(),
    )


def test_save_new_expense():
    repo = InMemoryExpenseRepository()
    expense = create_expense()
    repo.save(expense)
    expenses = repo.list_all()
    assert len(expenses) == 1
    assert expenses[0].id == 1


def test_save_updates_existing_expense():
    repo = InMemoryExpenseRepository()
    expense = create_expense()

    repo.save(expense)

    updated = create_expense(id=1, title="Updated", amount=20)
    repo.save(updated)

    expenses = repo.list_all()
    assert len(expenses) == 1
    assert expenses[0].title == "Updated"
    assert expenses[0].amount == 20


def test_remove_expense():
    repo = InMemoryExpenseRepository()
    expense = create_expense()
    repo.save(expense)
    repo.remove(expense_id=1)
    assert repo.list_all() == []


def test_list_all_returns_copy():
    repo = InMemoryExpenseRepository()
    repo.save(create_expense())
    expenses = repo.list_all()
    expenses.clear()
    assert len(repo.list_all()) == 1


def test_get_by_id_returns_expense():
    repo = InMemoryExpenseRepository()
    expense = create_expense(id=1, amount=50.0, description="Café")
    repo.save(expense)
    retrieved = repo.get_by_id(1)
    assert retrieved is not None
    assert retrieved.id == 1
    assert retrieved.amount == 50.0
    assert retrieved.description == "Café"


def test_get_by_id_returns_none_if_not_found():
    repo = InMemoryExpenseRepository()
    retrieved = repo.get_by_id(999)
    assert retrieved is None
