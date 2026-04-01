from .database.db_connexion import collection_tint_raw_data

def get_all_parties():
    return list(collection_tint_raw_data.find({}, {"_id": 0}))

def get_partie_by_id(Partie: int):
    return collection_tint_raw_data.find_one({"Partie": Partie}, {"_id": 0})


def get_tours_by_partie_id(Partie: int):
    partie = collection_tint_raw_data.find_one({"Partie": Partie}, {"_id": 0})
    if not partie:
        return None
    return partie.get("Tours", [])


def get_tour_by_id(Partie: int, Tour: int):
    partie = collection_tint_raw_data.find_one({"Partie": Partie}, {"_id": 0})
    if not partie:
        return None

    for tour in partie.get("Tours", []):
        if tour["Tour"] == Tour:
            return tour

    return None


"""def get_actions_by_tour_id(partie_id: int, tour_id: int):
    partie = collection_tint_raw_data.find_one({"partie_id": partie_id}, {"_id": 0})
    if not partie:
        return None

    for tour in partie.get("tours", []):
        if tour["tour_id"] == tour_id:
            return tour.get("actions", [])

    return None"""




