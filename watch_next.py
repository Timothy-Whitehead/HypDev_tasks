import spacy
nlp = spacy.load("en_core_web_md")

class Film:
    def __init__(self, name, description):
        self.name = name
        self.description = description

# gets film info from file and turns it into a Film class object, then appends to list
def get_films():
    with open("movies.txt", "r") as film_file:
        for line in film_file:
            film_split =  line.strip("\n").split(" :")
            film = Film(film_split[0], film_split[1])
            film_list.append(film)

# compares each film.description in the list with the hulk_film.description
# returns film with most similar description
def compare_films(hulk_film, film_list):
    watch_next = ""
    sim_to_hulk = 0
    for film in film_list:
        sameness = nlp(hulk_film.description).similarity(nlp(film.description))
        if sameness > sim_to_hulk:
            sim_to_hulk = sameness
            watch_next = film
    return watch_next
        


hulk_film = Film("Planet Hulk", "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminatiti trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.")

film_list = []

get_films()

watch_next = compare_films(hulk_film, film_list)

print(f"""Because you watched: {hulk_film.name}
We thought you might also like: {watch_next.name}
Synopsis: {watch_next.description}""")
