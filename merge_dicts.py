"""
merge_dicts - Given dictionaries are merge into a new dict.
"""

__version__ = "0.2.0"

def merge_dicts(*dict_args: [{}]) -> [{}, bool]:
    """
    merge_dicts: Given dictionaries are merge into a new dict.

    :param dict_args: Optional "dict_args" as list of dict.
    :type dict_args: dict or list(dict) or None
    :raise AttributeError: If the dict_args is invalid.
    :return: merged dict and list of merge conflicts.
    :rtype: list(dict, list)
    """

    result = {}
    merge_conflict = False
    merge_conflict_lists = []

    for dictionary in dict_args:
        current_list_of_merge_conflicts = []
        for key, value in dictionary.items():
            # Evaluate if two input dict have the same key, but different value.
            # If so, add key to current_list_of_merge_conflicts.
            if key in result:
                if value == result[key]:
                    pass
                else:
                    current_list_of_merge_conflicts.append(key)
                    merge_conflict = True
            else:
                # Add key and value to the dict.
                result[key] = value
        merge_conflict_lists.append(current_list_of_merge_conflicts)
    return [result, merge_conflict]
