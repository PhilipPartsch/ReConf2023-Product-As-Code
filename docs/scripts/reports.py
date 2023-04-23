
def stake_req_without_satisfied_by(needs, results, **kwargs):
    for need in needs:
        if need["type"] == "stake_req":
            if len(satisfies_back) == 0:
                results.append(need)
