import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that came to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://youtube.com/watch?v=-9ceBgWV8io")

the_last_jedi = media.Movie("Star Wars: The Last Jedi",
                            "Rey develops her newly discovered abilities with the guidance of Luke Skywalker",
                            "https://upload.wikimedia.org/wikipedia/en/7/7f/Star_Wars_The_Last_Jedi.jpg",
                            "https://www.youtube.com/watch?v=Q0CbN8sfihY")

shawshank = media.Movie("The Shawshank Redemption",
                        "Banker, sentenced to life for a murder, despite his claims of innocence",
                        "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco")

arrival = media.Movie("Arrival",
                      "A linguist, enlisted by the Army to help translate communications from extraterrestrial craft.",
                      "https://upload.wikimedia.org/wikipedia/en/d/df/Arrival%2C_Movie_Poster.jpg",
                      "https://www.youtube.com/watch?v=tFMo3UJ4B4g")

wonder = media.Movie("Wonder",
                     "A kid who has a rare medical facial deformity",
                     "https://upload.wikimedia.org/wikipedia/en/6/67/Wonder_%28film%29.png",
                     "https://www.youtube.com/watch?v=ngiK1gQKgK8")

movies = [arrival, wonder, avatar, the_last_jedi, shawshank]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
