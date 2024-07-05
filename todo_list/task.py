from datetime import datetime

class Task:
    CATEGORY_RANKING = {
        "Self": 1,
        "Family": 2,
        "School": 3,
        "Work": 4,
        "Friends": 5,
        "Hobbies": 6
    }

    def __init__(self, description, due_date=None, category="Self", priority_score=1):
        self.description = description
        self.completed = False
        self.due_date = due_date
        self.category = category
        self.priority_score = priority_score

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {
            "description": self.description,
            "completed": self.completed,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "category": self.category,
            "priority_score": self.priority_score
        }

    @classmethod
    def from_dict(cls, data):
        due_date = datetime.fromisoformat(data["due_date"]) if data["due_date"] else None
        task = cls(data["description"], due_date, data["category"], data["priority_score"])
        task.completed = data["completed"]
        return task

    def __str__(self):
        status = "✔" if self.completed else "✘"
        due_date_str = self.due_date.strftime("%Y-%m-%d %H:%M") if self.due_date else "No due date"
        return f"{status} {self.description} [Due: {due_date_str}, Category: {self.category}, Priority: {self.priority_score}]"

    def get_category_rank(self):
        return self.CATEGORY_RANKING.get(self.category, 7)  # Default rank if category not found
