from drive_methods import drive_update


class GarfieldBase:
    def __init__(self):
        self.strip_info = dict()
        self.strip_list = list()

        n = open("data/counts.txt", 'r')
        with open("data/strip_list.txt", 'r') as t:
            lines = t.readlines()
            count_list = n.readlines()
            count_index = 0

            for comic in lines:
                self.strip_info[(comic.split(".")[0])] = [int(count_list[count_index]), count_index]
                # So YOU don't forget, this line basically:
                # DICT [ "strip_date.gif".split(".")[0] -> strip_date
                # VALUE int(count_list[ same_index_as_comic ]) , count_index
                count_index = count_index + 1
        n.close()
        for comic in lines:
            self.strip_list.append(comic.split(".")[0])

    def random_strip(self):
        import random
        return random.choice(self.strip_list)

    def update_entry_details(self, strip, joke, laugh_bool=None):
        total_number_of_responses = self.strip_info[strip][0]
        index = self.strip_info[strip][1]

        n = open("data/counts.txt", 'r')
        count_list = n.readlines()
        if len(count_list[index]) == 2:
            count_list[index] = str(total_number_of_responses + 1) + "\n"
        else:
            count_list[index] = str(total_number_of_responses + 1)  # The ONE edge case

        n = open("data/counts.txt", 'w')
        n.writelines(count_list)
        n.close()

        if total_number_of_responses + 1 == 10:  # Once a strip reaches 10 responses, it's retired.
            n = open("data/strip_list.txt", 'r')
            strips = n.readlines()
            if len(strips[index]) == 15:
                strips[index] = "COMPLETED " + strips[index] + "\n"
            else:
                strips[index] = "COMPLETED " + strips[index]  # The ONE edge case

            n = open("data/strip_list.txt", 'w')
            n.writelines(strips)
            n.close()

            del self.strip_list[index]

        drive_update(index, joke, laugh_bool)
