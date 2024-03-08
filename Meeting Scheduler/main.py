
class Meeting:
    def __init__(self, start_time, end_time, meeting_room, users) -> None:
        self.start_time = start_time
        self.end_time = end_time
        self.meeting_room = meeting_room
        self.user_lists = users

class Calender:
    def __init__(self, user_id, meetings):
        self.user_id = user_id
        self.meetings = meetings


