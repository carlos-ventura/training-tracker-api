from enum import Enum


class TrainingGame(str, Enum):
    # RocketLeague = "rocket_league"
    # LeagueOfLegends = "league_of_legends"
    Skate = "skate"


class TrainingType(str, Enum):
    # SKATE
    Ground = "ground"
    Rails = "rails"
    Bowl = "bowl"

    # ROCKET LEAGUE
    # AirRoll = "air_roll"
    # Flips = "flips"
    # Control = "control"
    # Dash = "dash"

class TrainingSubType(str, Enum):
    # SKATE
    ShoveIt = "shove_it"

    # ROCKET LEAGUE
    # # AirRoll
    # Q1 = "q1"
    # Q2 = "q2"
    # Q3 = "q3"
    # Q4 = "q4"
    # Shot = "shot"
    # TornadoSping = "tornado_spin"

    # # Flips
    # HalfFlip = "half_flip"
    # SpeedFlip = "speed_flip"

    # # Control
    # GroundControl = "ground_control"
    # Flicks = "flicks"

    # # Dash
    # WallDash = "wall_dash"
    # ZapDash = "zap_dash"
    # WaveDash = "wave_dash"

