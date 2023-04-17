
def filter_id_linked_element_and_back (needs, results, **kwargs):

    verbose = False

    if len(kwargs) > 0:
        search_id = kwargs["arg1"].strip()
    else:
        raise("filter_id_linked_element_and_back was called without arguments (link types for filtering)!")

    links = []

    for i in range(2, len(kwargs)+1):
        links.append(kwargs["arg"+str(i)].strip())

    for need in needs:
        if need["id"] == search_id:
            results.append(need)
            link_destinations = []
            for link in links:
                link_destinations = link_destinations + need[link.strip()] + need[link.strip()+'_back']

            # remove doubles
            link_destinations = list(dict.fromkeys(link_destinations))

            for need2 in needs:
                for link_destination in link_destinations:
                    if need2["id"] == link_destination:
                        results.append(need2)
                        link_destinations.remove(link_destination)
                        break
                if len(link_destinations) == 0:
                    break
            break

    if len(results) == 0:
        raise("filter_id_linked_element_and_back was called but did not have a result. Arguments: " + str(kwargs))

