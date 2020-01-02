#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "Imraj423"

import cProfile
import pstats
import timeit


def profile(func):
    def inner(file):
        pr = cProfile.Profile()
        pr.enable()
        results = func(file)
        pr.disable()
        stats = pstats.Stats(pr).sort_stats('cumulative')
        print('Results from: %s' % func.__name__)
        stats.print_stats()
        return results
    return inner


def read_movies(src):
    return False


# @profile
# def find_duplicate_movies(src):
#     movies = read_movies(src)
#     return duplicates


@profile
def find_duplicate_movies(src='movies.txt'):

    movies = read_movies(src)
    movies = [movie.lower() for movie in movies]
    movies.sort()
    duplicates = [movie1 for movie1, movie2 in zip(
        movies[:-1], movies[1:]) if movie1 == movie2]
    return duplicates


find_duplicate_movies()




# @profile
# def find_duplicate_movies_with_in(src):
#     movies = read_movies(src)
#     duplicates = []
#     while movies:
#         movie = movies.pop()
#         if movie in movies:
#             duplicates.append(movie)
#     return duplicates


# @profile
# def find_duplicate_movies_for_loop(src):
#     movies = read_movies(src)
#     duplicates = []
#     for idx, movie in enumerate(movies):
#         if movie in movies[idx + 1:]:
#             duplicates.append(movie)

#     return duplicates


# @profile
# def find_duplicate_movies_hash(src):
#     movies = read_movies(src)
#     duplicates = []
#     movie_hash = {}

#     for movie in movies:
#         if movie not in movie_hash:
#             movie_hash[movie] = 1
#         else:
#             duplicates.append(movie)

#     return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer(lambda: find_duplicate_movies('movies.txt'))
    result = t.repeat(repeat=7, number=3)
    mean = min([time / 3 for time in result])
    print('Best time across 7 repeats of function 3 times is: %s' % mean)


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    main()
