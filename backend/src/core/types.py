from enum import Enum


class BanStatus(Enum):
    not_banned = 0
    read_only = 1
    temporary = 2
    permanent = 3