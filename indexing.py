


records = [
    ("Corey", "iOS"),
    ("Tyler", "DS"),
    ("Anika", "DS"),
    ("Jenna", "web"),
    ("Leighton", "web"),
    ("Nico", "web"),
    ("Carl", "web")
    ("Michael", "iOS")
]

def build_index(records):
    index = {}

    #loops over our records
    for record in records:
        name, track = record
    ## key is track
    ## if key isn't in dict add
        if track not in index:
            index[track] = []
        
        index[track].append(name)
    ## value: list of names
    return index
