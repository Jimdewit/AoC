import re


def get_input():
    with open('./test_input.txt', 'r') as file:
        return [x[:-1] for x in file]


def find_containing_bags(list_of_bags, bag_colour='shiny gold', containing_bags=None, total_containers=0):
    found_bags = []
    if not containing_bags:
        containing_bags = [bag_colour]
    for bag_colour in containing_bags:
        for x in list_of_bags:
            if re.match('.+?(?=bags contain .*{}.*)'.format(bag_colour), x):
                print("GOTCHA! {} should contain {}".format(x, bag_colour))
                found_bags += [re.match('.+?(?=bags contain .*{}.*)'.format(bag_colour), x).group()]
                total_containers += 1
        containing_bags.pop(containing_bags.index(bag_colour))

    return found_bags, total_containers


def finder_wrapper(baglist, containing_bags=None, total_containers=0, reference_bags=None):
    if not reference_bags:
        reference_bags=[]
    containing_bags, extra_containers = find_containing_bags(baglist, 'shiny gold', containing_bags)
    total_containers += extra_containers
    if len(containing_bags) > 0:
        reference_bags += [x for x in containing_bags if x not in reference_bags]
        return finder_wrapper(baglist, containing_bags, total_containers, reference_bags)
    else:
        return total_containers, reference_bags


def main():
    bag_data = get_input()
    total_containers, reference_bags = finder_wrapper(bag_data)
    print("Here's a list of reference bags:\n{}".format(reference_bags))
    print("This is the refbag length: {}".format(len(reference_bags)))
    print("I found this much bags: {}".format(total_containers))


if __name__ == "__main__":
    main()