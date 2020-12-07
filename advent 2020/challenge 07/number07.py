import re


def get_input():
    with open('./input.txt', 'r') as file:
        return [x[:-1] for x in file]


def find_containing_bags(list_of_bags, containing_bags=None, total_containers=0, bags_dict=None):
    # Definitely not OK code, but after finding unique values in the returned list it does add up to the correct amount.
    # Today's lesson: don't code whilst utterly hungover.

    found_bags = []
    if not containing_bags:
        containing_bags = ['shiny gold']
    for bag_colour in containing_bags:
        if bag_colour not in bags_dict:
            bags_dict[bag_colour] = [['Contained by'], ['Contains']]
        for x in list_of_bags:
            if re.match('.+?(?=bags contain .*{}.*)'.format(bag_colour), x):
                bags_dict[bag_colour][0] += [re.match('.+?(?=bags contain .*{}.*)'.format(bag_colour), x).group()]
                if bag_colour not in bags_dict[bag_colour][1]:
                    bags_dict[bag_colour][1] += [bag_colour]
                found_bags += [re.match('.+?(?=bags contain .*{}.*)'.format(bag_colour), x).group()]
                total_containers += 1

    return found_bags, total_containers, bags_dict


def finder_wrapper(baglist, containing_bags=None, total_containers=0, reference_bags=None, bags_dict=None):
    if not reference_bags:
        reference_bags = []
        bags_dict = {}
    containing_bags, extra_containers, bags_dict = find_containing_bags(baglist, containing_bags=containing_bags, bags_dict=bags_dict)
    total_containers += extra_containers
    if len(containing_bags) > 0:
        reference_bags += [x for x in containing_bags if x not in reference_bags]
        return finder_wrapper(baglist, containing_bags, total_containers, reference_bags, bags_dict)
    else:
        return total_containers, reference_bags, bags_dict


def find_hideousness(bag):
    # Shame. Plagiarised from /u/xelf :-(
    lines = re.findall('(.+) bags? contain (.*)\.', open('./input.txt').read())
    bags = {a: {n: int(q) for q, n in re.findall('\s*(\d+) (.*?) bags?', b)} for a, b in lines}
    rcount = lambda bag: 1 + sum(q * rcount(n) for n, q in bags.get(bag, {}).items())

    return rcount(bag)-1


def main():
    bag_data = get_input()
    total_containers, reference_bags, bags_dict = finder_wrapper(bag_data)
    total_bags = find_hideousness('shiny gold')
    print("I found this much bags: {}".format(len(set(reference_bags))))
    print("Also, I think they should contain {} bags".format(total_bags))


if __name__ == "__main__":
    main()