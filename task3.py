import timeit
from search_substring_algs.boyer_moore import boyer_moore_search
from search_substring_algs.kmp_search import kmp_search
from search_substring_algs.rabin_karp import rabin_karp_search

def measure_time(algorithm, text, pattern):
    return timeit.timeit(lambda: algorithm(text, pattern), number=1)

def load_text(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()

article_1 = load_text("./texts/article-1.txt")
article_2 = load_text("./texts/article-2.txt")

existing_substring = "системи"
non_existing_substring = "Я тут просто побуду :)"

print("Стаття 1:")
print(f"Боєр-Мур, існуючий підрядок: {measure_time(boyer_moore_search, article_1, existing_substring)} секунд")
print(f"Боєр-Мур, вигаданий підрядок: {measure_time(boyer_moore_search, article_1, non_existing_substring)} секунд")
#
print(f"КМП, існуючий підрядок: {measure_time(kmp_search, article_1, existing_substring)} секунд")
print(f"КМП, вигаданий підрядок: {measure_time(kmp_search, article_1, non_existing_substring)} секунд")
#
print(f"Рабін-Карп, існуючий підрядок: {measure_time(rabin_karp_search, article_1, existing_substring)} секунд")
print(f"Рабін-Карп, вигаданий підрядок: {measure_time(rabin_karp_search, article_1, non_existing_substring)} секунд")
#
#
print("\nСтаття 2:")
print(f"Боєр-Мур, існуючий підрядок: {measure_time(boyer_moore_search, article_2, existing_substring)} секунд")
print(f"Боєр-Мур, вигаданий підрядок: {measure_time(boyer_moore_search, article_2, non_existing_substring)} секунд")
#
print(f"КМП, існуючий підрядок: {measure_time(kmp_search, article_2, existing_substring)} секунд")
print(f"КМП, вигаданий підрядок: {measure_time(kmp_search, article_2, non_existing_substring)} секунд")
#
print(f"Рабін-Карп, існуючий підрядок: {measure_time(rabin_karp_search, article_2, existing_substring)} секунд")
print(f"Рабін-Карп, вигаданий підрядок: {measure_time(rabin_karp_search, article_2, non_existing_substring)} секунд")
