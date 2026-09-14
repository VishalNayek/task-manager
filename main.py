book = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "available": True
}

if book["available"]:
    print(f'{book["title"]} is available.')
else:
    print(f'{book["title"]} is currently borrowed.')