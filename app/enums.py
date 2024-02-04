from enum import Enum


class TrainingGame(str, Enum):
    RocketLeague = "rocket_league"
    LeagueOfLegends = "league_of_legends"


class TrainingType(str, Enum):
    AirRoll = "air_roll"
    Flips = "flips"
    Control = "control"


class TrainingSubType(str, Enum):
    # AirRoll
    Q1 = "q1"
    Q2 = "q2"
    Q3 = "q3"
    Q4 = "q4"

    # Flips
    HalfFlip = "half_flip"
    SpeedFlip = "speed_flip"
    WallDash = "wall_dash"

    # Control
    GroundControl = "ground_control"
    Flicks = "flicks"
