from enum import Enum


class TrainingGame(str, Enum):
    RocketLeague = "rocket_league"
    LeagueOfLegends = "league_of_legends"


class TrainingType(str, Enum):
    AirRoll = "air_roll"
    Flips = "flips"
    Control = "control"
    Dash = "dash"


class TrainingSubType(str, Enum):
    # AirRoll
    Q1 = "q1"
    Q2 = "q2"
    Q3 = "q3"
    Q4 = "q4"

    # Flips
    HalfFlip = "half_flip"
    SpeedFlip = "speed_flip"

    # Control
    GroundControl = "ground_control"
    Flicks = "flicks"

    # Dash
    WallDash = "wall_dash"
    ZapDash = "zap_dash"
    WaveDash = "wave_dash"
