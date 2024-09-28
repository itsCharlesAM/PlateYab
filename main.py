import flet as ft
import asyncio  # For handling the delay
import data  # Import the data from data.py


# Function to find the city based on the entered number
def get_city_by_plate_number(plate_number):
    plate_number_str = str(plate_number)  # Convert number to string for lookup
    for province, cities in data.plate_data.items():
        for city, plates in cities.items():
            if plate_number_str in plates:
                return f"{province}، {city}"
    return "منطقه نامشخص"


# Function that runs when the button is clicked
def on_search(e):
    try:
        # Get the entered number and convert it to an integer
        plate_number = int(plate_input.value)
        # Get the corresponding city
        result_text.value = get_city_by_plate_number(plate_number)
    except ValueError:

        # If input is not a valid number, show an error message
        result_text.value = "لطفا یک شماره دو رقمی وارد کنید."

    # Update the result text to show the city name
    result_text.update()


# Function to restrict the input to 2 digits only
def on_input_change(e):
    if len(e.control.value) > 2:
        e.control.value = e.control.value[:2]  # Limit to 2 characters
    if not e.control.value.isdigit():  # Ensure the input is only digits
        e.control.value = ''.join([i for i in e.control.value if i.isdigit()])
    e.control.update()


# Main app function
async def main(page: ft.Page):
    # Set the background color for the entire app
    page.bgcolor = "#2964cc"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Splash Screen
    splash_text = ft.Text(
        "PlateYab!",
        size=40,
        color="white",
        text_align=ft.TextAlign.CENTER,
    )

    splash_container = ft.Container(
        content=ft.Column(
            controls=[splash_text],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        bgcolor="#2964cc",
        alignment=ft.alignment.center
    )

    page.add(splash_container)

    # Delay for 3 seconds before showing the main content
    await asyncio.sleep(1)

    # Fade out effect for splash screen
    for opacity in range(100, -1, -10):  # Decrease opacity from 100 to 0
        splash_text.opacity = opacity / 100  # Set opacity
        splash_container.update()
        await asyncio.sleep(0.025)  # Short delay for the fade effect

    # Clear the splash screen
    page.clean()

    # Define the plate number input field with 2-digit limit
    global plate_input
    plate_input = ft.TextField(
        label="شماره پلاک را وارد کنید",
        width=200,
        text_align=ft.TextAlign.CENTER,
        on_change=on_input_change  # Trigger validation on input change
    )

    # Define the result text element
    global result_text
    result_text = ft.Text(
        value="",
        color="white",
        size=20,
        text_align=ft.TextAlign.RIGHT,  # Set text alignment to RIGHT for RTL
    )

    # Define the card with input and button
    card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    plate_input,
                    ft.Container(
                        content=ft.ElevatedButton(
                            text="جستوجو",
                            on_click=on_search,
                            style=ft.ButtonStyle(
                                bgcolor=ft.colors.LIGHT_BLUE,  # Brighter button color
                                color="white",  # Text color on the button
                                shape=ft.RoundedRectangleBorder(
                                    radius=20),  # Rounded corners
                            )
                        ),
                        border_radius=20,  # Set border radius
                        padding=10
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            ),
            padding=20,
        ),
        opacity=0  # Set initial opacity to 0
    )

    # Add the card and result text to the page
    page.add(ft.Column(
        controls=[card, result_text],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20
    ))

    # Fade-in effect for the main content
    for opacity in range(0, 101, 10):  # Increase opacity from 0 to 100
        card.opacity = opacity / 100  # Set opacity
        card.update()  # Update the card to reflect the change
        await asyncio.sleep(0.025)  # Short delay for the fade effect

# Run the app
ft.app(target=main)
