def unformatted_months(month):
    dict = {
        "Janeiro": "01/2024",
        "Fevereiro": "02/2024",
        "Março": "03/2024",
        "Abril": "04/2024",
        "Maio": "05/2024",
        "Junho": "06/2024",
        "Julho": "07/2024",
        "Agosto": "08/2024",
        "Setembro": "09/2024",
        "Outubro": "10/2024",
        "Novembro": "11/2024",
        "Dezembro": "12/2024",
    }

    return dict[month]


def formatted_month(month):
    dict = {
        "01/2024": "Janeiro",
        "02/2024": "Fevereiro",
        "03/2024": "Março",
        "04/2024": "Abril",
        "05/2024": "Maio",
        "06/2024": "Junho",
        "07/2024": "Julho",
        "08/2024": "Agosto",
        "09/2024": "Setembro",
        "10/2024": "Outubro",
        "11/2024": "Novembro",
        "12/2024": "Dezembro",
    }

    return dict[month]

def formatted_months(months):
    return [formatted_month(month) for month in sorted(months)]