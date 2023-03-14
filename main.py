with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    file_modified = file_contents.lower()
    words = file_modified.split()
    word_dict = {} 
    l_char ={}
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    K = max(zip(word_dict.values(),word_dict.keys()))[1]
    for l in file_modified:
        if l.isalpha():
            if l in l_char:
              l_char[l]+=1
            else:
             l_char[l]=1
    sort_list = []
    for l_ch in l_char:
        sort_list.append({"char": l_ch, "num": l_char[l_ch]})
  
    print(f"--- Begin report of {'books/frankenstein.txt'} ---")
    print(f"{K} words found in the document")
    print()

    for item in sort_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")





  
