# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flet import *


def main(page: Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'

    categories_card = Row(
        scroll=ScrollMode.AUTO         # scroll='auto'
    )
    categories = ['Business', 'Family', 'Friends']
    for category in categories:
        categories_card.controls.append(
            Container(
                border_radius=20,
                bgcolor=BG, height=110, width=170, padding=15,
            )
        )

    first_page_contents = Container(
        content=Column(
            controls=[
                Row(
                    alignment='spaceBetween', controls=[
                        Container(
                            content=Icon(
                                icons.MENU)),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATIONS_OUTLINED)
                            ]
                        )
                    ]),
                Container(height=20),
                Text(
                    value='What\'s up, Olivia!'
                ),
                Text(
                    value='CATEGORIES'
                ),
                Container(
                    padding=padding.only(top=10, bottom=20, ),
                    content=categories_card
                )
            ]
        )
    )

    page_1 = Container()
    page_2 = Row(
        controls=[
            Container(
                width=400, height=850, bgcolor=FG, border_radius=35,
                padding=padding.only(top=50, left=20, right=20, bottom=5),
                content=Column(
                    controls=[
                        first_page_contents
                    ]
                )
            )
        ]
    )

    container = Container(
        width=400, height=850, bgcolor=BG, border_radius=35,
        content=Stack(
            controls=[
                page_1,
                page_2
            ]
        )
    )


    page.add(container)


app(target=main)

