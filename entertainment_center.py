import media
import fresh_tomatoes


# Instance of Movie Avatar
avatar = media.Movie(
    'Avatar',
    'A marine on an alient planet',
    2009,
    2,
    'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
    'https://www.youtube.com/watch?v=5PSNL1qE6VY')

# Instance of Movie - Avatar
interstellar = media.Movie(
    'Interstellar',
    'A father and astronaut tried to save his child and save the world',
    2014,
    2,
    'https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg',
    'https://www.youtube.com/watch?v=0vxOhd4qlnA')

# Instance of Movie - Moulin Rouge
moulin_rough = media.Movie(
    'Moulin Rouge',
    'A love story about a famous singer and a poor musician',
    2001,
    2,
    'https://upload.wikimedia.org/wikipedia/en/9/9f/Moulin_rouge_poster.jpg',
    'https://www.youtube.com/watch?v=2PpgPxjzbkA')

# Instance of Movie - Pride and Prejudice
pride_and_prejudice = media.Movie(
    'Pride and Prejudice',
    'A love story about two young people who had misunderstanding at first',
    2005,
    1,
    'https://images-na.ssl-images-amazon.com/images/M/MV5BMTA1NDQ3NTcyOTNeQTJeQWpwZ15BbWU3MDA0MzA4MzE@._V1_SY1000_CR0,0,674,1000_AL_.jpg',
    'https://www.youtube.com/watch?v=1dYv5u6v55Y')

# Instance of Movie - X-Men: Apocalypse
x_men_apocalypse = media.Movie(
    'X-Men: Apocalypse',
    'A story about a group of people of special ability to guard the world',
    2016,
    2,
    'https://upload.wikimedia.org/wikipedia/en/0/04/X-Men_-_Apocalypse.jpg',
    'https://www.youtube.com/watch?v=PfBVIHgQbYk')

# Instance of Movie - The Hunger Games
hunger_games = media.Movie(
    'The Hunger Games',
    'A really real reality show',
    2012,
    2,
    'https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg',
    'https://www.youtube.com/watch?v=MkvUNfySGQU')

# Instance of Movie - Wonder Woman
wonder_woman = media.Movie(
    'Wonder Woman',
    'A woman trained to be a warrior from youth tries to defend the world',
    2017,
    2,
    'https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg',
    'https://www.youtube.com/watch?v=95a2aqEAbo8')

# Instance of Movie - Dawn of the Planet of the Apes
the_apes = media.Movie(
    'Dawn of the Planet of the Apes',
    'A story of apes against human',
    2014,
    2,
    'https://upload.wikimedia.org/wikipedia/en/7/77/Dawn_of_the_Planet_of_the_Apes.jpg',
    'https://www.youtube.com/watch?v=DpSaTrW4leg')

# Set the Movie array movies to be displayed
movies = [
    avatar,
    interstellar,
    moulin_rough,
    pride_and_prejudice,
    x_men_apocalypse,
    hunger_games,
    wonder_woman,
    the_apes
    ]

# Generate the HTML file, and open the HTML file on web browser
fresh_tomatoes.open_movies_page(movies)
