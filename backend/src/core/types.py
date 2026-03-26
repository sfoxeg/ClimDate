from enum import Enum


class BanStatus(Enum):
    NOT_BANNED = "not_banned"
    READ_ONLY = "read_only"
    TEMPORARY = "temporary"
    PERMANENT = "permanent"