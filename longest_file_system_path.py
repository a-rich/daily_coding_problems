def longest_path(string):
    lengths = []
    last_level = -1
    length_dict = {}
    running_length = 0

    for l in [(h.count("\t"), h.strip("\t")) for h in string.split('\n')]:
        if l[0] > last_level:
            running_length += len(l[1])
        elif l[0] == last_level:
            running_length -= length_dict[l[0]]
            running_length += len(l[1])
        else:
            for i in reversed(range(l[0], last_level+1)):
                running_length -= length_dict[i]
            running_length += len(l[1])


        length_dict[l[0]] = len(l[1])
        last_level = l[0]

        if '.' in l[1]:
            lengths.append(running_length + last_level)

    return max(lengths)

if __name__ == '__main__':
    string = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    assert longest_path(string) == 20

    string = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    assert longest_path(string) == 32
