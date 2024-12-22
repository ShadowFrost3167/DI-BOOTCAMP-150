import textwrap
print("")
article = """
New Bench Installed in Town Square\n
Shady Hollow \n

 Excitement quietly rippled through the sleepy town of Shady Hollow this week as a new bench was installed in the town square, replacing the previous bench that had stood for nearly 30 years.  

 The new bench, made of sturdy oak with a weatherproof finish, is located under the town's beloved oak tree, providing shade and a pleasant spot for residents to sit and watch the goings-on—or lack thereof—at the square.  

 Mayor Ruth Crenshaw presided over a brief ribbon-cutting ceremony on Tuesday afternoon. “This bench represents progress,” she stated to a modest crowd of seven people, including her nephew who brought a dog. “It’s a testament to our commitment to comfort and community.”  

 The old bench, which had grown wobbly and developed a creaky plank, has been relocated to the backyard of the public works office, where officials say it will serve as "an occasional resting spot for staff on break."  

 Local retiree Arnold Pickett, who frequents the square to feed pigeons, offered his thoughts. “It’s nice, I suppose. The wood smells fresh. But the old bench had character. This one feels a little…too new.”  

 The installation was funded by proceeds from last year’s annual Harvest Festival bake sale, which raised $178.43, precisely enough to cover the cost of the bench and a small commemorative plaque that reads: “Donated by the People of Shady Hollow.”

 Reports indicate that the bench has already seen light use. Teenager Maggie Olsen was spotted briefly sitting on it Wednesday while scrolling on her phone. "It's fine, I guess," she said, declining further comment.  

 The new bench is expected to serve Shady Hollow residents well into the foreseeable future, or at least until the town’s next bake sale generates enough funds for another civic improvement.
"""

# Split article into paragraphs wrap each 
paragraphs = article.strip().split("\n\n")
wrapped_paragraphs = [textwrap.fill(paragraph, width=90) for paragraph in paragraphs]

# Join wrapped paragraphs with double space (space = vert)
formatted_article = "\n\n".join(wrapped_paragraphs)

print(formatted_article)