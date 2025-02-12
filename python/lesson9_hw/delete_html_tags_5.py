"""Module with function that deletes html tags from text"""

import re


def delete_html_tags(inp_text: str) -> str:
    """Function that deletes html tags from text"""
    clean_text = re.sub(r"<.*?>", "", inp_text)
    clean_text = re.sub(r"\s+", " ", clean_text).strip()
    clean_text = re.sub(r"\n+", "\n", clean_text)
    return clean_text


if __name__ == "__main__":
    IN_TEXT = """
        <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, 
                initial-scale=1.0">
                <title>Sample HTML</title>
            </head>
            <body>
                <header>
                    <h1>Welcome to My Website</h1>
                </header>
                
                <section>
                    <h2>Introduction</h2>
                    <p>This is a simple example of a webpage with various 
                    HTML tags. Here are some of the most common HTML 
                    elements:</p>
                    
                    <ul>
                        <li><strong>Bold Text</strong> – You can make text 
                        bold using the <code>&lt;strong&gt;</code> tag.</li>
                        <li><em>Italic Text</em> – To italicize text, 
                        use the <code>&lt;em&gt;</code> tag.</li>
                        <li>Links: <a href="https://www.example.com" 
                        target="_blank">Click here</a> to visit an example 
                        website.</li>
                    </ul>
                </section>
                
                <section>
                    <h2>Images</h2>
                    <p>Here is an example of an image:</p>
                    <img src="https://via.placeholder.com/150" 
                    alt="Placeholder Image">
                </section>
                
                <section>
                    <h2>Form Example</h2>
                    <form action="/submit" method="POST">
                        <label for="name">Name:</label>
                        <input type="text" id="name" name="name" 
                        required><br><br>
                        
                        <label for="email">Email:</label>
                        <input type="email" id="email" name="email" 
                        required><br><br>
                        
                        <input type="submit" value="Submit">
                    </form>
                </section>
                
                <footer>
                    <p>© 2025 My Website</p>
                </footer>
            </body>
            </html>
    """

    result = delete_html_tags(IN_TEXT)
    print(result)
