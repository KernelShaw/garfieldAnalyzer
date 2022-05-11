def decoy_method(what):
    return

class GarfieldBase:

    def __int__(self):
        self.strip_info = dict()
        self.strip_list = list()

        n = open("counts.txt", 'r')
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

    # def data_entry(self, strip, joke_id):
        # Submit it to google drive.
        # Edit the entry count dictionary using the index
        # Edit and save entry count file using index
        # If count == 10, then delete strip entry

    def update_entry_details(self, strip):
        total_number_of_responses = self.strip_info[strip][0]
        index = self.strip_info[strip][1]

        # Google Drive Here

        n = open("counts.txt", 'r')
        count_list = n.readlines()
        count_list[index] = str(total_number_of_responses + 1)

        n = open("counts.txt", 'w')
        n.writelines(count_list)
        n.close()

        if total_number_of_responses + 1 == 10:  # Once a strip reaches 10 responses, it's retired.
            n = open("strip_list.txt", 'r')
            strips = n.readlines()
            strips[index] = "COMPLETED " + strips[index]

            n = open("strip_list.txt", 'w')
            n.writelines(strips)
            n.close()

            del self.strip_list[index]
