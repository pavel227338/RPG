def is_pangram(st):
    spisochek = []
    for char in st.lower():
        if char not in [',','.','!','@','"',"'",'%','*','(',')','?','<','>','`',' ']:
            spisochek.append(char)
    st_set = set(spisochek)
    alph = {'w', 's', 'b', 'v', 'x', 'h', 'm', 'o', 'g', 'u', 'r', 'n', 'q', 'l', 'z', 'y', 'i', 'f', 'k', 'd', 't', 'e', 'j', 'a', 'c', 'p'}
    if st_set == alph:
        return  True
    return False