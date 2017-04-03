# keep class def in one file, and use class in another.
import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0%2C0%2C300%2C450",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://resizing.flixster.com/RekPVUC5CH4Vgulb0UaiXgYDbdM=/206x305/v1.bTsxMTE3Njc5MjtqOzE3MzY0OzEyMDA7ODAwOzEyMDA",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

american_psycho = media.Movie("American Psycho",
                              "A wall street psycho",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/6/63/Americanpsychoposter.jpg/220px-Americanpsychoposter.jpg",
                              "https://www.youtube.com/watch?v=5YnGhW4UEhc")

school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "http://static.rogerebert.com/uploads/movie/movie_poster/school-of-rock-2003/large_cREN222Yw78zvSQ9bg17Y9QZS0c.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

it = media.Movie("IT",
                 "We all float down here",
                 "https://images-na.ssl-images-amazon.com/images/M/MV5BY2I0ZGI0MzItN2RhZi00ZmQ3LWI5MmUtNWE2MTAxZmY5Njc1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                 "https://www.youtube.com/watch?v=FnCdOQsX5kc")

movies = [toy_story, avatar, american_psycho, school_of_rock, it]
fresh_tomatoes.open_movies_page(movies)
