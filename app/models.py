class User:
    def __init__(self, name, surname, mail):
        self.name = name
        self.surname = surname
        self.mail = mail
        self.assigned = []

    def assign_task(self, task):
        if task not in self.assigned:
            self.assigned.append(task)
            task.owner = self

    def unassign_task(self, task):
        if task in self.assigned:
            self.assigned.remove(task)
            task.owner = None

    def __str__(self):
        return f"{self.name} {self.surname} - {self.mail}" 
    
    
class Task:
    def __init__(self, title, priority, status="Pending"):
        self.title = title
        self.priority = priority
        self.status = status
        self.owner = None
    def mark_status(self, status):
        self.status = status
    def __str__(self):
        who = self.owner.name if self.owner else "Nobody"
        return f"[{self.title}] | Priority: {self.priority} | Status: {self.status} | Assigned to: {who}"

class Project:
    def __init__(self, title):
        self.title = title
        self.members = []
        self.items = []
    def add_user(self, user):
        if user not in self.members:
            self.members.append(user)
    def add_task(self, task):
        if task not in self.items:
            self.items.append(task)
    def __str__(self):
        return f"Project: {self.title} (Users: {len(self.members)}, Tasks: {len(self.items)})"


if __name__ == "__main__":
    prj = Project("Mobile App")

    u1 = User("giorgi", "giorgardze", "gio@mail.com")
    u2 = User("mariam", "mayvaladze", "mari@mail.com")

    t1 = Task("Login page", "High")
    t2 = Task("Register page", "Medium")
    t3 = Task("Testing", "Low")

    prj.add_user(u1)
    prj.add_user(u2)
    prj.add_task(t1)
    prj.add_task(t2)
    prj.add_task(t3)

    u1.assign_task(t1)
    u2.assign_task(t2)
    t1.mark_status("Ongoing")
    t2.mark_status("Done")

    print(prj)
    print(u1)
    print(u2)
    for t in prj.items:
        print(t)
