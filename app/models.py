import os


class Report():
    def __init__(self, id, incident_type, comment_description, status,
                 current_location,
                 created,
                 user_id):
        self.id = id
        self.incident_type = incident_type,
        self.comment_description = comment_description,
        self.status = status,
        self.current_location = current_location,
        self.created = created,
        self.user_id = user_id

    def __str__(self):
        return "id:{} incident_type:{} status:{}  ".format(
            self.id, self.incident_type, self.status)

    def __repr__(self):
        return "id:{} incident_type:{} status:{}  ".format(
            self.id, self.incident_type, self.status)


report = Report(1, 'Intervation',  'myc comment', 'under investigation', 'kira', 'now', 1)
print(report)
