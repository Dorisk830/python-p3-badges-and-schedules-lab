def badge_maker(name):
    return f"Hello, my name is {name}."


def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names ]

# speakers_list = ["Arel", "Carol"]
# badge_messages = batch_badge_creator(speakers_list)
# print(badge_messages)


def assign_rooms(speakers):
    return [f"Hello, {name}! You'll be assigned to room {index + 1}!" for index, name in enumerate(speakers)]

# speakers_list = ["Arel", "Carol"]
# room_assignments = assign_rooms(speakers_list)
# print(room_assignments)

def printer(names):  
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)
def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    return [f"Hello, {name}! You'll be assigned to room {index + 1}!" for index, name in enumerate(names)]


    for badge in badges:
        print(badge)

    for assignment in room_assignments:
        print(assignment)

# speakers_list = ["Arel", "Carol"]
# printer(speakers_list)
