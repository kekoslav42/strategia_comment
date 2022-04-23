from django.conf import settings


def generate_comment(queryset):
    """
    Рекурсивно строим дерево комментариев
    """
    result = []
    max_level = settings.MAX_LEVEL

    def get_line(query, queryset):
        query['children'] = []
        for comment in queryset:
            if (comment['parent'] == query['id']
                    and (max_level is None or comment['level'] <= max_level)):
                query['children'].append(comment)
                get_line(query['children'][-1], queryset)

    for query in queryset:
        if query['parent'] is None:
            result.append(query)
            get_line(query, queryset)

    return result
