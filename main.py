def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        text_array = file_contents.split( )
        num_of_words = (len(text_array))
        no_space = "".join(text_array)
        lowered = no_space.lower()
        alphas = ''.join(filter(str.isalpha, lowered))
        ordered = sorted(alphas)
        counted = {}
        number = 1
        if len(ordered) > 0:
            counted[ordered[0]] = 1
            for i in range(len(ordered)):
                if i + 1 < len(ordered):
                    if ordered[i] == ordered[i+1]:
                        number = number + 1
                        counted[ordered[i]] = number
                    else:
                        number = 1
                        counted[ordered[i+1]] = number
                
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{num_of_words} were found in the document.")
        print("\n")
        for key, value in counted.items():
            print(f"The '{key}' character was found {value} times")








main()