#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "???"

import cProfile
import pstats
import timeit
import io


def profile(func):
    def wrapper(file):
        profile = cProfile.Profile()
        profile.enable()
        results = func(file)
        profile.disable()
        stats = pstats.Stats(profile).sort_stats('cumulative')
        print('Results from: %s' % func.__name__)
        stats.print_stats()
        return results
    return wrapper


# def profile(fnc):
    
#     """A function that can be used as a decorator to measure performance"""
#     def inner(*args, **kwargs):
#         pr = cProfile.Profile()
#         pr.enable()
#         retval = fnc(*args, **kwargs)
#         pr.disable()
#         s = io.StringIO()
#         sortby = 'cumulative'
#         ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
#         ps.print_stats()
#         print(s.getvalue())
#         return retval
#     return inner

   
# # def read_movies(src):
# #     """Returns a list of movie titles"""
# #     # print('Reading file: {}'.format(src))
# #     # with open(src, 'r') as f:
# #     #     return f.read().splitlines()
# #     return False


# def is_duplicate(title, movies):
#     """returns True if title is within movies list"""
#     for movie in movies:
#         if movie.lower() == title.lower():
#             return True
#     return False


# def read_movies(src):

#     with open(src) as fd:
#         return fd.read().splitlines()


# @profile
# def find_duplicate_movies(src='movies.txt'):

#     movies = read_movies(src)
#     movies = [movie.lower() for movie in movies]
#     movies.sort()
#     duplicates = [movie1 for movie1, movie2 in zip(
#         movies[:-1], movies[1:]) if movie1 == movie2]
#     return duplicates


# find_duplicate_movies()
# # @profile
# # def find_duplicate_movies(src):
# #     """Returns a list of duplicate movies from a src list"""
# #     movies = read_movies(src)
# #     duplicates = []
# #     while movies:
# #         movie = movies.pop()
# #         if is_duplicate(movie, movies):
# #             duplicates.append(movie)
# #     return duplicates


# def timeit_helper():
#     """Part A:  Obtain some profiling measurements using timeit"""
#     # number = 10
#     # repeat = 3
#     t = timeit.Timer(stmt=find_duplicate_movies('movies.txt'))
#     result = t.repeat(repeat=7, number=3)
#     mean = min([time / 3 for time in result])
#     print('Best time across 7 repeats of function 3 times is: %s' % mean)

# def main():
#     """Computes a list of duplicate movie entries"""
#     result = find_duplicate_movies('movies.txt')
#     print('Found {} duplicate movies:'.format(len(result)))
#     print('\n'.join(result))


# if __name__ == '__main__':
#     main()
