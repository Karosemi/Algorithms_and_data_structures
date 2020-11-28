
def checking_HTML_correctness(filename: str):
    """
    Funkcja ma za zadanie sprawdzać poprawność składni dokumentu HTML.
    Jako argument przyjmuje nazwę pliku, który ma sprawdzić.
    Zwraca True jeśli dokument jest poprawny składniowo i False jeśli nie jest.
    """
    balanced = True
    open_tags, close_tags = find_tags(filename)
    for open_tag in open_tags:
        close_tag = open_tag.replace('<', '</')
        if close_tag in close_tags:
            close_tags.remove(close_tag)
        else:
            balanced = False
    return balanced

def find_tags(filename: str):
    file_obj = open(filename, 'r')
    text = file_obj.read()
    return find_element(text, '<', '>')


def find_element(text: str, left_sign: str, right_sign: str):
    text = text.replace("\n", '')
    i = 0
    open_elements = []
    close_elements = []
    while i < len(text):
        left = text.find(left_sign, i)
        if text[left + 1:left + 9] == '!DOCTYPE':  # DOCTYPE> declaration is not an HTML tag
            left += 16
            i = left
            continue
        elif text[left + 1] != '/':
            right, open_elements = add_element_to_list(text, left, right_sign, open_elements)
            i = right + 1
        else:
            right, close_elements = add_element_to_list(text, left, right_sign, close_elements)
            i = right + 1
    return remove_self_closing_tags(tags_list_checker(open_elements)), tags_list_checker(close_elements)


def add_element_to_list(text: str, left: int, right_sign: str, element_list: list):
    space = text.find(' ', left)
    right = text.find(right_sign, left)
    if right < space and space:
        element_list.append(text[left: right + 1])
    elif space:
        element_list.append(text[left:space] + text[right])
    else:
        element_list.append(text[left: right + 1])
    return right, element_list


def tags_list_checker(tags: list):
    copy_tags = tags
    for tag in copy_tags:
        close = tag.find('>')
        if tag.find('<', close + 1) != -1:
            first_tag = tag[:close + 1]
            second_tag = tag[close + 1:]
            index = copy_tags.index(tag)
            copy_tags.remove(tag)
            copy_tags.insert(index, first_tag)
            copy_tags.insert(index + 1, second_tag)
    return copy_tags


def remove_self_closing_tags(tags: list):
    self_closing_tags = ['<area>', '<base>', '<br>', '<embed>', '<hr>',
                       '<iframe>', '<img>', '<input>', '<link>', '<meta>',
                       '<param>', '<source>', '<track>', '<!-->']
    to_remove = []
    for tag in tags:
        if tag in self_closing_tags:
            to_remove.append(tag)
    for tag in to_remove:
        tags.remove(tag)
    return tags


if __name__ == '__main__':
    filename = 'L4_ZAD4_sampleHTML_3.txt'
    print(checking_HTML_correctness(filename))