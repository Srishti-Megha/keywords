############## To Extract Keywords from pdf file.


import PyPDF2 
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


#Function to remove same strings from list
def remove(words_list):
    f_list = []
    for word in words_list:
        if word not in f_list:
            f_list.append(word) 
    return(f_list)
    
    

# name of pdf file
filename = "JavaBasics-notes.pdf"


file = open(filename, 'rb')

# "read_file" is a PdfFileReader object
read_file = PyPDF2.PdfFileReader(file)

#get the number of pages in the file
num_pages = read_file.getNumPages()


#List of symbols to be ignored
del_symb = string.punctuation

del_words = stopwords.words('english')
   
#list of ascii words         
letters = string.ascii_letters

#list of digits
digits = string.digits

keywords = []
#noise = []

#loop through the pages and extract the keywords.
for i in range(num_pages):
    words_string = read_file.getPage(i).extractText()
    # change string to lower_case.
    words_string = words_string.lower()
    
    words_list = word_tokenize(words_string)
    
    #Remove same strings from list
    words_list = remove(words_list)
    # append the list of words in the page to "words" ignoring the punctuations, letters, digits.
    words = [words for words in words_list if not words in del_symb and not words in del_words and not words in digits and not words in letters and not words in keywords]
    
    #Remove characters like: 1996-2003, ``, '', /*, */, //, ...,  /**,  1+1=2, --, ++, ==, ||, *=, /=, +=, -=, ^=
    for text in words:
        if all(j.isdigit() or j in del_symb for j in text):
#            noise.append(text)
            continue
        
        else:
            keywords.append(text)
    


        
    
    
# Only noun using nltk.POS_tag
noun = nltk.pos_tag(keywords)
    
final_keywords = []

for i in noun:
    if i[1] == 'NN':
        final_keywords.append(i[0])

    

        
################################
##%%## Save the keyword in text file
with open('keywords', 'w') as txt_file:
    for words in final_keywords:
        txt_file.write("%s\n"% words)


        
        
