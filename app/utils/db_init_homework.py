from app.models import (
    Homework, 
)

from sqlalchemy.ext.asyncio import AsyncSession

description = [
    "Introduction. Python and VSCode installation. Gi",
    "Basic types. If condition. Modules.",
    "Cycle",
    "Collections: sets, strings, lists, tupl",
    "Collections methods. Nump",
    "Dict and list comprehensio",
    "Functions closures. Recursion. Using *args, **kwargs",
    "Functions as object. Lambda functions",
    "Sort I. Algorithm complexity, bubble sort, counting sor",
    "Sort II. Merge sort, heap sort",
    "Sort III. Fast sort, radix sort",
    "Examination",
]



deadlines = [
    "September, 14",
    "September, 21",
    "September, 28",
    "October, 5",
    "October, 12",
    "October, 19",
    "October, 26",
    "November, 3",
    "November, 10",
    "November, 24",
]





def test_homework_model(
        
        user_id : int,
        user_name: str,
        session: AsyncSession,):