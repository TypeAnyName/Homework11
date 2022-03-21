import json


def load_candidate_from_json():
    file = open("candidates.json", encoding='UTF-8')
    candidates_list = json.load(file)
    file.close()
    return candidates_list


def get_candidate(id):
    candidate_list = load_candidate_from_json()
    candidate_id = []
    for candidate in candidate_list:
        if candidate["id"] == id:
            candidate_id.append(candidate)
    return candidate_id


def get_candidates_by_name(name):
    candidate_list = load_candidate_from_json()
    candidate_name = []
    for candidate in candidate_list:
        if candidate["name"] == name.title():
            candidate_name.append(candidate)
    return candidate_name


def get_candidates_by_skill(skill):
    candidate_list = load_candidate_from_json()
    candidate_skill = []
    for candidate in candidate_list:
        if skill in candidate["skills"].split(", "):
            candidate_skill.append(candidate)
    return candidate_skill



