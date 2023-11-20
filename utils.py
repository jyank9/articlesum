import requests
from bs4 import BeautifulSoup
import ipywidgets as widgets



def scrape_news_article(url):
    try:
        # Send an HTTP request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Check for a paywall by looking for common elements
        paywall_elements = soup.find_all(class_='paywall')

        if paywall_elements:
            print("Paywall encountered. Unable to access the full article.")
            return None
        else:
            # Extract text from the article
            article_text = ""
            for paragraph in soup.find_all('p'):
                article_text += paragraph.get_text() + "\n"

            return article_text.strip()

    except requests.exceptions.RequestException as e:
        print(f"Error accessing the URL: {e}")
        return None

def get_user_input():
    # Create a text box widget for user input
    input_text = widgets.Text(value='', placeholder='Enter text...', description='Input:', disabled=False)

    # Create a button widget
    button = widgets.Button(description="Submit")

    # Output widget to display the result
    output_result = widgets.Output()

    # Function to handle button click event
    def on_button_click(b):
        user_input = input_text.value
        with output_result:
            print("Key received, beginning processing")

    # Assign the function to the button click event
    button.on_click(on_button_click)

    # Display the widgets
    display(widgets.VBox([input_text, button, output_result]))
    return input_text.value


