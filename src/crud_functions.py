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


# -------------------------
# ANALYTICS / KPI
# -------------------------


def get_kpi_globaux():
    parties = list(
        collection_tint_raw_data.find({}, {"_id": 0, "score_final": 1})
    )

    total_parties = len(parties)

    avg_score_final = (
        round(sum(p.get("score_final", 0) for p in parties) / total_parties, 2)
        if total_parties > 0
        else 0.0
    )

    max_doc = collection_tint_raw_data.find_one(
        {},
        {"_id": 0, "score_final": 1},
        sort=[("score_final", -1)]
    )

    max_score = max_doc["score_final"] if max_doc else 0

    return {
        "max_score": max_score,
        "total_parties": total_parties,
        "avg_score_final": avg_score_final
    }


def get_users_level_points():
    parties = list(
        collection_tint_raw_data.find(
            {},
            {"_id": 0, "utilisateur": 1, "Tours.Level": 1}
        )
    )

    result = []

    for partie in parties:
        tours = partie.get("Tours", [])
        if not tours:
            continue

        # le level est le meme pour tous les tours, donc on prend celui du premier tour
        level = tours[0].get("Level", 0)

        result.append({
            "utilisateur": partie.get("utilisateur"),
            "level": level
        })

    return result

def get_score_final_evolution():
    parties = list(
        collection_tint_raw_data.find(
            {},
            {"_id": 0, "Partie": 1, "utilisateur": 1, "score_final": 1}
        ).sort([
            ("utilisateur", 1),
            ("Partie", 1)
        ])
    )

    return [
        {
            "partie": p.get("Partie", 0),
            "utilisateur": p.get("utilisateur", "Inconnu"),
            "score_final": p.get("score_final", 0)
        }
        for p in parties
    ]

# ici en entrant les paramètres
"""def get_score_final_evolution(utilisateur: str, partie: int):
    query = {}

    if utilisateur is not None:
        query["utilisateur"] = utilisateur

    if partie is not None:
        query["Partie"] = partie

    parties = list(
        collection_tint_raw_data.find(
            query,
            {"_id": 0, "Partie": 1, "utilisateur": 1, "score_final": 1}
        ).sort("Partie", 1)
    )

    return [
        {
            "partie": p["Partie"],
            "utilisateur": p.get("utilisateur", "Inconnu"),
            "score_final": p.get("score_final", 0)
        }
        for p in parties
    ]
"""

def get_score_tour_evolution():
    parties = list(
        collection_tint_raw_data.find(
            {},
            {"_id": 0, "Partie": 1, "utilisateur": 1, "Tours.Tour": 1, "Tours.Score": 1}
        )
    )

    result = []

    for p in parties:
        for tour in p.get("Tours", []):
            result.append({
                "partie": p.get("Partie", 0),
                "utilisateur": p.get("utilisateur", "Inconnu"),
                "tour": tour.get("Tour", 0),
                "score": tour.get("Score", 0)
            })

    result.sort(key=lambda x: (x["utilisateur"], x["partie"], x["tour"]))
    return result

"""def get_score_tour_evolution(partie: int | None = None, utilisateur: str | None = None):
    query = {}

    if partie is not None:
        query["Partie"] = partie

    if utilisateur is not None:
        query["utilisateur"] = utilisateur

    parties = list(
        collection_tint_raw_data.find(
            query,
            {"_id": 0, "Partie": 1, "utilisateur": 1, "Tours.Tour": 1, "Tours.Score": 1}
        )
    )

    result = []

    for p in parties:
        for tour in p.get("Tours", []):
            result.append({
                "partie": p["Partie"],
                "utilisateur": p.get("utilisateur", "Inconnu"),
                "tour": tour.get("Tour", 0),
                "score": tour.get("Score", 0)
            })

    result.sort(key=lambda x: (x["utilisateur"], x["partie"], x["tour"]))
    return result"""

