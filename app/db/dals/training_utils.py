from sqlalchemy.orm import Query


def process_game_query(query: Query) -> dict:
    query_result = query.all()

    game = query_result[0].game
    hours = 0.0
    count = 0
    formatted_result = []

    for row in query_result:
        hours += row.hours
        count += row.count
        formatted_result.append(
            {
                "type": row.type,
                "sub_type": row.sub_type,
                "hours": row.hours,
                "count": row.count
            }
        )

    return {"game": game, "hours": hours, "count": count, "trainings": formatted_result}


def process_type_query(query: Query) -> dict:
    query_result = query.all()

    game = query_result[0].game
    hours = 0.0
    count = 0
    formatted_result = []

    for row in query_result:
        hours += row.hours
        count += row.count
        formatted_result.append(
            {
                "type": row.type,
                "hours": row.hours,
                "count": row.count
            }
        )
    return {"game": game, "hours": hours, "count": count, "trainings": formatted_result}
