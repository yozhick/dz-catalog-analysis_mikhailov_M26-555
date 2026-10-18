import math


movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


def average_rating(movies):
    return round(sum(movie["rating"] for movie in movies) / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - movie["year"] for movie in movies]
    return max(ages), min(ages), math.ceil(sum(ages) / len(ages))


def duration_in_hours(minutes):
    return f"{minutes // 60}ч {minutes % 60}м"


def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"


def print_non_comedy_movies(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_masterpiece(movies):
    index = 0
    while index < len(movies):
        if movies[index]["rating"] > 9.0:
            break
        index += 1
    else:
        return "Шедевров не найдено"
    return movies[index]["title"]


def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


def normalize_title(title):
    words = title.split()
    return " ".join(word[0].upper() + word[1:] for word in words)


def make_slug(title):
    return normalize_title(title).lower().replace(" ", "-")


def format_report_line(movie):
    title = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return (
        f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, '
        f"{duration}, жанры: {genres}"
    )


def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]


def count_by_genre(movies):
    counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts


def actor_filmography(movies):
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            filmography[actor] = filmography.get(actor, [])
            filmography[actor].append(movie["title"])
    return filmography


def ratings_above_average(movies):
    if not movies:
        return {}
    average = average_rating(movies)
    return {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > average
    }


def all_genres(movies):
    genres = set()
    for movie in movies:
        genres.update(movie["genres"])
    return genres


def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    return all_genres(movies_a) - all_genres(movies_b)


def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def total_duration(movies, min_rating=7):
    return sum(
        movie["duration_min"] for movie in movies if movie["rating"] > min_rating
    )


movie = movies[0]
other_movie = movies[3]

print("average_rating:", average_rating(movies))
print("----------")
print("catalog_age_stats:", catalog_age_stats(movies))
print("----------")
print(
    f"duration_in_hours({movie['duration_min']}):",
    duration_in_hours(movie["duration_min"]),
)
print("----------")
print(f"rating_tier({movie['rating']}):", rating_tier(movie["rating"]))
print("----------")
print(f"decade_label({movie['year']}):", decade_label(movie["year"]))
print("----------")
print("print_non_comedy_movies:")
print_non_comedy_movies(movies)
print("----------")
print("find_masterpiece:", find_masterpiece(movies))
print("----------")
print(
    "find_masterpiece (без шедевров):",
    find_masterpiece([movie for movie in movies if movie["rating"] <= 9.0]),
)
print("----------")
print("count_long_movies:", count_long_movies(movies))
print("----------")
print(f"normalize_title({movie['title']!r}):", normalize_title(movie["title"]))
print("----------")
print(f"make_slug({movie['title']!r}):", make_slug(movie["title"]))
print("----------")
print(
    f"format_report_line (фильм {movie['title']!r}):",
    format_report_line(movie),
)
print("----------")
print("titles_sorted_by_rating:", titles_sorted_by_rating(movies))
print("----------")
print("top_n_by_rating(n=3):", top_n_by_rating(movies))
print("----------")
print("count_by_genre:", count_by_genre(movies))
print("----------")
print("actor_filmography:", actor_filmography(movies))
print("----------")
print("ratings_above_average:", ratings_above_average(movies))
print("----------")
print("all_genres:", all_genres(movies))
print("----------")
print(
    f"common_actors({movie['title']!r}, {other_movie['title']!r}):",
    common_actors(movie, other_movie),
)
print("----------")
print(
    "genres_only_in_one(movies[5:6], movies[:5]):",
    genres_only_in_one(movies[5:6], movies[:5]),
)
print("----------")
print("iter_high_rated(min_rating=8.0):")
for high_rated_movie in iter_high_rated(movies):
    print(format_report_line(high_rated_movie))
print("----------")
print("total_duration(min_rating=7):", total_duration(movies))
