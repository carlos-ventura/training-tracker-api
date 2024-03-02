from sqlalchemy.orm import Query


def process_game_query(query: Query) -> dict:
    query_result = query.all()

    game = query_result[0].game
    minutes = 0.0
    count = 0
    formatted_result = []

    for row in query_result:
        minutes += row.minutes
        count += row.count
        formatted_result.append(
            {
                "type": row.type,
                "sub_type": row.sub_type,
                "minutes": row.minutes,
                "count": row.count
            }
        )

    return {"game": game, "minutes": minutes, "count": count, "trainings": formatted_result}


def process_type_query(query: Query) -> dict:
    query_result = query.all()

    game = query_result[0].game
    minutes = 0.0
    count = 0
    formatted_result = []

    for row in query_result:
        minutes += row.minutes
        count += row.count
        formatted_result.append(
            {
                "type": row.type,
                "minutes": row.minutes,
                "count": row.count
            }
        )

def _time(minutes: float) -> str:
    minutes = int(minutes)
    hours, remaining_minutes = divmod(minutes, 60)
    return f"{hours}h:{remaining_minutes}m"
