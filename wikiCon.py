import wikipedia

wikipedia.set_lang("ru")

def print_paragraphs(article, start=0):
    paragraphs = article.content.split('\n\n')
    for i in range(start, len(paragraphs)):
        print(paragraphs[i])
        user_input = input("\nВведите 'д' для продолжения или 'н' для остановки: ")
        if user_input.lower() != 'д':
            break

def navigate_links(article):
    links = article.links
    for i, link in enumerate(links):
        print(f"{i+1}. {link}")
    user_choice = input("\nВведите номер связанной статьи, чтобы перейти к ней, или 'н' для возврата: ")
    if user_choice.lower() == 'н':
        return None
    try:
        selected_index = int(user_choice) - 1
        if selected_index >= 0 and selected_index < len(links):
            return wikipedia.page(links[selected_index])
        else:
            print("Некорректный номер. Попробуйте снова.")
    except ValueError:
        print("Некорректный ввод. Попробуйте снова.")
    return None

def main():
    initial_query = input("Введите запрос для поиска на Википедии: ")
    try:
        article = wikipedia.page(initial_query)
        print(f"\nСтатья: {article.title}\n")
        while True:
            print("\nВыберите действие:")
            print("1. Листать параграфы текущей статьи")
            print("2. Перейти на одну из связанных страниц")
            print("3. Выйти из программы")
            user_choice = input("Ваш выбор: ")

            if user_choice == '1':
                print_paragraphs(article)
            elif user_choice == '2':
                new_article = navigate_links(article)
                if new_article:
                    article = new_article
                    print(f"\nСтатья: {article.title}\n")
            elif user_choice == '3':
                print("Выход из программы.")
                break
            else:
                print("Некорректный выбор. Попробуйте снова.")
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Запрос неоднозначен. Возможные варианты: {e.options}")
    except wikipedia.exceptions.PageError:
        print("Статья не найдена. Попробуйте другой запрос.")

if __name__ == "__main__":
    main()