from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

def resolve_url(url):
    """
    Attempts to follow HTTP redirects to find the final destination URL.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        # We use a session to handle cookies if the redirect requires them
        session = requests.Session()
        response = session.get(url, headers=headers, allow_redirects=True, timeout=10)
        
        # The 'url' attribute of the response contains the final URL after redirects
        return response.url
    except Exception as e:
        return str(e)

@app.route('/', methods=['GET', 'POST'])
def index():
    final_url = None
    error = None

    if request.method == 'POST':
        original_url = request.form.get('url')
        if original_url:
            final_url = resolve_url(original_url)
        else:
            error = "Please provide a valid URL."

    return f'''
    <!doctype html>
    <title>Link Resolver</title>
    <h1>Direct Link Generator</h1>
    <form method=post>
      <input type=text name=url placeholder="Paste ad-link here" style="width: 300px;">
      <input type=submit value="Resolve">
    </form>
    {f'<h3>Final Link: <a href="{final_url}">{final_url}</a></h3>' if final_url else ""}
    {f' <p style="color:red;">{error}</p>' if error else ""}
    '''

if __name__ == '__main__':
    app.run(debug=True)
    
