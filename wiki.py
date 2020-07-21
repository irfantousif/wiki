import wikipedia
def get_wiki(query):
	title=wikipedia.search(query)[1]
	page=wikipedia.page(title)
	return page.content
text=input(str("what do you want from wiki??:"))
if "pavan kalyan" in text:
	print(get_wiki(text))
if "virat kohli" in text:
	print(get_wiki(text))
if "lockie ferguson" in text:
	print(get_wiki(text))
if "ben stokes" in text:
	print(get_wiki(text))