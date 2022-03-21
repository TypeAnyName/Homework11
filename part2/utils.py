import json


def load_candidate_from_json():
    file = open("candidates.json", encoding='UTF-8')
    candidates_list = json.load(file)
    file.close()
    return candidates_list


def get_candidate(id):
    candidate_list = load_candidate_from_json()
    for candidate in candidate_list:
        if candidate["id"] == id:
            return {
                'name': candidate["name"],
                'position': candidate['position'],
                'picture': candidate["picture"],
                "skills": candidate["skills"],
            }
    return {'not_found': "Ничего нет:("}


def get_candidates_by_name(name):
    candidate_list = load_candidate_from_json()
    candidate_found = []
    for candidate in candidate_list:
        if name.title() in candidate["name"].split(' '):
            candidate_found.append(candidate)
    return candidate_found


def get_candidates_by_skill(skill):
    candidate_list = load_candidate_from_json()
    candidate_skill = []
    for candidate in candidate_list:
        if skill in candidate["skills"].split(", "):
            candidate_skill.append(candidate)
    return candidate_skill

