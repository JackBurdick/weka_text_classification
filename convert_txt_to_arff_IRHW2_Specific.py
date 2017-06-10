#!/usr/bin/python3


# open file path (.txt), read information, return list of datasets
def read_in_file_return_data_list(file_input_path):
    data_line_list = []
    try:
        with open(file_input_path, 'r') as file_current:
            for data_line in file_current:
                data_line_list.append(data_line)
        return data_line_list
    except:
        error_message = "ERROR: input ( " + file_input_path + " ) not found"
        exit(error_message)


# create .arff file
def handle_data_write_arff(list_of_txt_entries, output_path):
    # will create file if not created
    with open(output_path, "w") as output_file:
        # write header information
        output_file.write("@relation 'WebKB Test'\n\n"
                          + "@attribute Text string\n"
                          + "@attribute class-att"
                          + "{student, faculty, project, course}\n\n"
                          + "@data\n\n")

        # write main data block
        for data_block in list_of_txt_entries:
            # split into classifier and data
            data_list = data_block.split('\t')  # .txt file is split by a "\t"
            class_name = data_list[0]
            data = data_list[1]
            data = data.rstrip('\n')   # remove trailing newline

            # write the main data
            output_file.write("'" + data + "'" + "," + class_name)
            output_file.write('\n')    # Move to newline to designate new entry


def convert_file(file_path, output_path):
    print("[START] Convert .txt to .arff")
    # read in data
    try:
        list_of_txt_entries = read_in_file_return_data_list(file_path)
    except:
        exit("ERROR: Unable to read input data - unsure what the error is")

    print("--update: ", len(list_of_txt_entries), "'datasets' were found")

    # convert and create .arff file
    try:
        handle_data_write_arff(list_of_txt_entries, output_path)
    except:
        exit("ERROR: Unable to create/write an .arff file - error uncertain")

    print("[END] Convert .txt to .arff: ", output_path)


def main():
    # convert_file(file_path, output_path)
    convert_file("./webkb-train-stemmed.txt", "webkb_train_stemmed.arff")
    convert_file("./webkb-test-stemmed.txt", "webkb_test_stemmed.arff")
    # NOTE: these will create this file path if it is not already created
    # Otherwise, if found, it will overwrite the previous information


if __name__ == "__main__":
    main()
