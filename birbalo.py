#                   1-masala
# def count_passing_students(grades:list[int],passing_grade:int) -> int:
#     count = 0
#     for i in grades:
#         if i >= passing_grade:
#             count += 1
#     return count

# lst = list(map(int,input(">>> ").split()))
# passing_grade = int(input("Passing grade: "))
# print(count_passing_students(lst, passing_grade))

#                   2-masala
# def ends_with_gram(words: list[str]) -> list[str]:
#     new = []
#     for i in words:
#         if i.lower().endswith("gram"):
#             new.append(i)
#     return new        
        

# lst = input(">>> ").split()
# natija = ends_with_gram(lst)
# print(natija)

#                   3-masala
# def find_top_three_numbers_sorted(data: list) -> list:
#     new = []
#     for i in data:
#         new.append(tuple(sorted(i[:3],reverse=True)))
#     return new
    
# data = [(10, 20, 30, 11), (5, 15), (40,), (7, 8, 50, 3)]
# print(find_top_three_numbers_sorted(data))

#                   4-masala
# def calculate_painting_time(pattern: list) -> int:
#     vaqt = 0
#     for i in range(len(pattern)):
#         vaqt += 2
#         if pattern[i] != pattern[i-1]:
#             vaqt += 1
#     return vaqt
        

# pattern =  ["Red", "Blue", "Red", "Blue", "Red"] 
# natija = calculate_painting_time(pattern)
# print(natija)

#                    5-masala
def find_nearest_vowel(letter: str) -> str:
    if letter.isalpha() and letter.islower():
        yaqin = ""
        kichik = 100
        for i in "aeiou":
            masofa = abs(ord(i) - ord(letter))
            if masofa < kichik:
                kichik = masofa
                yaqin = i
        return yaqin
    else:
        return "Faqat bitta kichik harf bo'lishi kerak"
            

natija = find_nearest_vowel(input(">>> "))
print(natija)