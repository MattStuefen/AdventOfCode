import textwrap
import urllib2
import traceback
import re
import json

# This is a sample web-scraper which downloads all of the coding challenges from "adventofcode.com"

url_template = "http://adventofcode.com/day/"
content_start = "<article class=\"day-desc\">"
content_end = "<p class=\"day-success\">"
num_to_text = {int(key): value for key, value in json.load(open("./num_to_text.json")).items()}
session_id = ""  # Need to fill in session id to get part 2

for day in range(1, 26):
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie', 'session=' + session_id))

    try:
        # Download code challenge text
        response = opener.open(url_template + str(day))
    except:
        traceback.print_exc()
        print "Retrying..."
        response = opener.open(url_template + str(day))

    page_data = response.read().decode('utf-8')

    # Isolate and clean up challenge content
    puzzle_content = page_data[page_data.find(content_start) + len(content_start): page_data.rfind(content_end)]
    puzzle_content = re.sub('<[^<]+?>', '', puzzle_content)
    puzzle_content = puzzle_content.replace("---", "\n---\n").strip()  # Put title on it's own line
    text_wrapper = textwrap.TextWrapper(replace_whitespace=False, width=120)
    puzzle_content = [text_wrapper.fill(paragraph) for paragraph in puzzle_content.split("\n") if paragraph]
    puzzle_content = "\n\n".join(puzzle_content)

    # Write challenge.txt to that day's folder
    file_name = '../Day' + num_to_text[day] + "/challenge.txt"
    file_handle = open(file_name, 'w')
    file_handle.write(puzzle_content)
    file_handle.close()
    print 'Created: ' + file_name
