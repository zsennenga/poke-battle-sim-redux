# type: ignore
import csv
import random
import importlib.resources

import poke_battle_sim.conf.global_settings as gs


def load_pokemon_stats():
    pokemon_stats = []
    name_to_id = {}
    with open(importlib.resources.files(gs.DATA_DIR).joinpath(gs.POKEMON_STATS_CSV)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        for row in csv_reader:
            for num in gs.POKEMON_STATS_NUMS:
                row[num] = int(row[num])
            pokemon_stats.append(row)
            name_to_id[row[1]] = row[0]
    return pokemon_stats, name_to_id


def load_natures():
    natures = {}
    nature_list = []
    with open(importlib.resources.files(gs.DATA_DIR).joinpath(gs.NATURES_CSV)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        for row in csv_reader:
            natures[row[0]] = (int(row[1]), int(row[2]))
            nature_list.append(row[0])
    return natures, nature_list


def load_moves():
    move_list = []
    move_name_to_id = {}
    with open(importlib.resources.files(gs.DATA_DIR).joinpath(gs.MOVES_CSV)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        for row in csv_reader:
            for num in gs.MOVES_NUM:
                if row[num]:
                    row[num] = int(row[num])
            move_list.append(row)
            move_name_to_id[row[1]] = row[0]
    return move_list, move_name_to_id


def load_types():
    type_to_id = {}
    type_effectives = []
    with open(importlib.resources.files(gs.DATA_DIR).joinpath(gs.TYPE_EF_CSV)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        line_count = 0
        for row in csv_reader:
            type_to_id[row[0]] = line_count
            row = [float(row[i]) for i in range(1, len(row))]
            type_effectives.append(row)
            line_count += 1
    return type_to_id, type_effectives


def load_abilities():
    abilities = {}
    ability_list = []
    with open(importlib.resources.files(gs.DATA_DIR).joinpath(gs.ABILITIES_CSV)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        for row in csv_reader:
            abilities[row[1]] = (row[0], row[2])
            ability_list.append(row[1])
    return abilities, ability_list


def load_items():
    items = {}
    item_list = []
    with open(importlib.resources.files(gs.DATA_DIR).joinpath(gs.ITEMS_CSV)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        for row in csv_reader:
            items[row[1]] = (row[0], row[2])
            item_list.append(row[1])
    return items, item_list


class PokeSim:
    def __init__(
        self,
        pokemon_stats,
        name_to_id,
        natures,
        nature_list,
        move_list,
        move_name_to_id,
        type_to_id,
        type_effectives,
        abilities,
        ability_list,
        items,
        item_list,
    ):
        self._pokemon_stats = pokemon_stats
        self._name_to_id = name_to_id
        self._natures = natures
        self._nature_list = nature_list
        self._move_list = move_list
        self._move_name_to_id = move_name_to_id
        self._type_to_id = type_to_id
        self._type_effectives = type_effectives
        self._abilities = abilities
        self._ability_list = ability_list
        self._items = items
        self._item_list = item_list

    def _convert_name_to_id(self, name: str) -> int:
        if name not in self._name_to_id:
            return -1
        return self._name_to_id[name]

    def get_valid_name_or_id(self, name_or_id: str | int) -> int | None:
        if not isinstance(name_or_id, (str, int)):
            return
        p_id = name_or_id
        if isinstance(name_or_id, str):
            p_id = self._convert_name_to_id(name_or_id)
        if 0 < p_id < len(self._pokemon_stats):
            return p_id
        return

    def get_pokemon(self, name_or_id: str | int) -> list | None:
        p_id = self.get_valid_name_or_id(name_or_id.lower())
        if not p_id:
            return
        return self._pokemon_stats[p_id - 1]

    def nature_conversion(self, nature: str) -> tuple[int, int] | None:
        if not isinstance(nature, str) or nature not in self._natures:
            return
        return self._natures[nature]

    def get_move_data(self, moves: [str]) -> list | None:
        if not isinstance(moves, list):
            return
        move_data = []
        move_ids = []
        for move in moves:
            if move not in self._move_name_to_id:
                return
            move_data.append(self._move_list[self._move_name_to_id[move] - 1])
            if move_data[-1][0] in move_ids:
                return
            move_ids.append(move_data[-1][0])
        return move_data

    def get_single_move(self, move: str):
        return self._move_list[self._move_name_to_id[move] - 1]

    def check_status(self, status: str):
        return

    def get_type_ef(self, move_type: str, def_type: str) -> float | None:
        if move_type not in self._type_to_id or def_type not in self._type_to_id:
            raise Exception
        return self._type_effectives[self._type_to_id[move_type]][
            self._type_to_id[def_type]
        ]

    def get_all_types(self) -> list:
        return list(self._type_to_id.keys())

    def is_valid_type(self, type: str) -> bool:
        return type in self._type_to_id

    def filter_valid_types(self, types: list[str]) -> list:
        return [type for type in types if type in self._type_to_id]

    def get_rand_move(self) -> list:
        return self._move_list[random.randrange(gs.COMPLETED_MOVES)]

    def get_rand_ability(self) -> str:
        return self._ability_list[random.randrange(len(self._ability_list))]

    def get_rand_item(self) -> str:
        return self._item_list[random.randrange(len(self._item_list))]

    def get_rand_poke_id(self) -> int:
        return random.randrange(1, len(self._pokemon_stats))

    def get_rand_stats(self) -> list[int]:
        return [random.randrange(gs.STAT_ACTUAL_MIN, gs.STAT_ACTUAL_MAX + 1) for _ in range(6)]

    def get_rand_gender(self) -> str:
        return gs.POSSIBLE_GENDERS[random.randrange(len(gs.POSSIBLE_GENDERS))]

    def get_rand_level(self) -> int:
        return random.randrange(gs.LEVEL_MIN, gs.LEVEL_MAX + 1)

    def get_rand_nature(self) -> str:
        return self._nature_list[random.randrange(len(self._nature_list))]

    def check_ability(self, ability: str) -> bool:
        return ability in self._abilities

    def check_item(self, item: str) -> bool:
        return item in self._items
