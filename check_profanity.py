import urllib.request

def read_text():
    quotes = open("movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    for text in text_to_check:
        query = urllib.parse.urlencode({'q': text_to_check})
        url = "http://www.wdylike.appspot.com/?"+query
        
        connection = urllib.request.urlopen(url)
        output = connection.read()
        print(output)
        connection.close()

read_text()
